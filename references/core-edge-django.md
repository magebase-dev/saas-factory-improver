# Core Runtime, Serverless Edge, Storage, and Security Standards

Use this reference during **Pass 1** when auditing or modifying backend code, `wrangler.toml` / `wrangler.jsonc` configs, database queries, async workers, or authentication flows.

## 1. Core Runtime and Serverless Edge

- **Framework**: Django 6.1.x running synchronously via WSGI, dedicated to Cloudflare D1 and Durable Object backends via `django-cf`.
- **Execution Environment**: Cloudflare Python Workers (Python 3.14 compiled to WebAssembly via Pyodide inside V8 isolates).
- **Package and Build Tooling**: Manage dependencies exclusively via `uv` and `pywrangler`.
- **Strict Resource Guardrails**:
  - **128 MB Isolate Memory Budget**: Avoid loading large datasets, pandas/numpy arrays, or file buffers into memory. Use `.iterator(chunk_size=200)` on querysets if iterating over rows, and offload heavy work to Cloudflare Queues or Workflows.
  - **Execution Caps**: Workers Paid allows up to 5 minutes CPU on background tasks, but HTTP requests must be capped at `cpu_ms = 1000` and `subrequests = 100` in Wrangler configuration to eliminate runaway loops and N+1 query storms.
- **Workspace and Domain Isolation**:
  - **Independent Product Workspaces**: Keep product-specific code strictly inside `products/<product>/`. Place shared cross-product primitives inside `packages/factory-*/`. Never import across sibling `products/` directories.
  - **Private Service Bindings**: Use zero-latency in-process RPC via Cloudflare Service Bindings (`env.SHARED_*`) for internal factory communication, bypassing public internet hops and auth overhead.
  - **Custom Apex Domains Only**: Ensure `workers_dev = false` is set in production configs. Never expose `*.workers.dev` endpoints in production.

## 2. Database, Storage, and Async Queues

- **Cloudflare D1 (Primary Relational DB)**:
  - Accessed via `django-cf` SQLite-compatible serverless SQL.
  - Verify minute-level 30-Day Point-in-Time Recovery (PITR) is active and scheduled portable `.sql` exports are written to Cloudflare R2.
  - Eliminate N+1 queries using `select_related` and `prefetch_related` so HTTP endpoints stay well below the 100-subrequest limit.
- **Cloudflare R2 (Object and Asset Storage)**:
  - All user or pipeline uploads must use **direct client-side presigned URLs**.
  - Zero Worker isolate memory buffering is allowed on file uploads or downloads.
  - Use R2 event notifications to push object-creation events into downstream Cloudflare Queues.
- **Cloudflare KV (Edge Cache and Feature Flags)**:
  - Use KV for sub-millisecond read-heavy configuration, rate limits, feature flags, and tenant routing tables.
- **Cloudflare Queues (Async Processing)**:
  - Every queue consumer must have a paired Dead-Letter Queue (`*-dlq`), process messages via batch consumers, and enforce strict idempotency keys before mutating state or sending external requests.
- **Cloudflare Workflows and Durable Objects**:
  - Use **Cloudflare Workflows** for multi-step durable saga execution (such as onboarding sequences, directory submission runs, or multi-stage media generation).
  - Use **Durable Objects** for strongly consistent distributed state coordination, distributed locks, and per-tenant rate limiting.

## 3. Authentication, Security, and Tenant Isolation

- **Authentication (Rule 34)**:
  - Use direct email/password authentication via Django `auth` + `allauth` with vaulted credentials in `.env.credentials`.
  - Keep social OAuth strictly optional so automated browser synthetics and AI coding agents never hit brittle third-party session breaks.
- **Session Security**:
  - Enforce strict host-only `__Host-` session cookies:
    ```python
    SESSION_COOKIE_NAME = "__Host-sessionid"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_DOMAIN = None  # Never use wildcard domains like .example.com
    SESSION_COOKIE_PATH = "/"
    ```
- **Strict Tenant Isolation**:
  - Every multi-tenant model must include an explicit `tenant_id` foreign key.
  - Every database query, mutation, and R2 object key must enforce explicit `tenant_id` boundary checks. Never rely on implicit session state without scoping the queryset.
- **Capability Entitlements**:
  - Evaluate all feature gates and permissions through capability checks:
    ```python
    if not entitlements.can(subject, "feature_slug"):
        raise PermissionDenied()
    ```
  - Never hardcode plan strings (such as `if tenant.plan == "agency":`) in views, templates, or APIs.

## Verification Checklist for Pass 1

- [ ] `wrangler.toml` / `wrangler.jsonc` enforces `workers_dev = false`, `cpu_ms = 1000`, and `subrequests = 100`.
- [ ] All Queues declare a matching `*-dlq` dead-letter queue and idempotency check.
- [ ] Zero file uploads pass through Django/Worker request bodies; all use R2 presigned URLs.
- [ ] All ORM queries filter explicitly by `tenant_id` and avoid N+1 subrequest spikes.
- [ ] All feature checks use `entitlements.can(subject, 'feature')`.
