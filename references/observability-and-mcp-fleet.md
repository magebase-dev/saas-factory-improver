# The $0 Observability Fleet and Complete MCP Integration Runbook

Use this reference during **Pass 1 (Observability)**, **Pass 2 (Billing & Mobile)**, and **Pass 3/4 (SEO & Growth)** to orchestrate live diagnostics and automated actions across the Model Context Protocol (MCP) fleet.

## 1. The $0 Modern Observability and Reliability Fleet

| Layer | Tool / Service | Free Quota & Guardrails | Implementation & Verification |
| :--- | :--- | :--- | :--- |
| **APM & Edge Logs** | **New Relic** | 100 GB/mo free ingest | Ingests APM metrics, spans, errors, and Cloudflare Logpush edge events. Watch `cpu_ms` and subrequest counts. |
| **Error Tracking** | **Sentry** | Release-tagged worker metadata | Configured in `apps/saas_kernel/observability.py`. Must tag every event with worker version and `tenant_id`. |
| **Uptime & Heartbeats** | **Better Stack** | External ping & gateway probes | Monitors apex domains, health endpoints, and cron/workflow heartbeats. |
| **Product Analytics** | **PostHog** | 1M events/mo free (strictly guarded) | Reserved ONLY for high-value semantic business events: `user_signed_up`, `lead_submitted`, `quote_accepted`. Never enable autocapture or session replay here. |
| **UX & Session Replay** | **Microsoft Clarity** | Unlimited free recordings & heatmaps | Captures rage-clicks, dead-clicks, and scroll heatmaps without burning PostHog quotas. |
| **Browser Synthetics** | **Cloudflare Browser Run + `@cloudflare/playwright`** | Scheduled headless assertions | Tests live hot-paths (`app.example.com`, etc.). Signs requests with `X-Synthetic-Run` HMAC-SHA256 header and routes side-effects to `SYNTHETIC_EMAIL_SINK` (`synthetic-sink@example.com`). |
| **Self-Healing Incident Bus** | **`ops_router.py` + `alerting.py`** | 300s cooldown deduplication | Normalizes alerts across Better Stack, Grafana, Sentry, New Relic, and PostHog. Dispatches Sev-1 (Critical) and Sev-2 (High) emails to `alerts@example.com` (forwarded to `admin@example.com`). |

## 2. Complete MCP Fleet Integration Matrix

Always prefer invoking the dedicated MCP server over manual guesswork or raw curl scripts when auditing or operating a service.

### A. Billing, Subscriptions, and App Store Monetization MCPs

- **Stripe MCP (`stripe-mcp`)**:
  - **Use for**: Auditing products, prices, Checkout Sessions, Customer Portal configs, webhook endpoints, MRR/churn metrics, and failed payment recovery across web SaaS properties.
  - **Architecture Rule**: Ensure Stripe webhook handlers verify cryptographic signatures, enforce idempotency in D1, and update tenant capability records evaluated via `entitlements.can(subject, 'feature')`.
- **RevenueCat MCP (`revenuecat-mcp`)**:
  - **Use for**: Managing cross-platform entitlements, offerings, packages, and paywalls bridging Web (Stripe) and Mobile (Google Play Billing via Capacitor/TWA).
  - **Architecture Rule**: Map RevenueCat entitlement identifiers 1:1 with `entitlements.can(subject, 'feature')` capabilities and synchronize webhook events (`INITIAL_PURCHASE`, `RENEWAL`, `CANCELLATION`, `BILLING_ISSUE`) into D1.
- **Google Play Developer MCP (`play-store-mcp`)**:
  - **Use for**: Automating Play Developer API operations via service account credentials (`play-store-service-account.json`), including AAB/APK uploads, release track promotions (`internal` -> `alpha` -> `beta` -> `production`), store listing metadata/screenshots, in-app subscription products, and Android vitals/ANR crash triage.

### B. Edge Infrastructure and Code Intelligence MCPs

- **Cloudflare MCP (`cloudflare-mcp`)**:
  - **Use for**: Direct management and inspection of Cloudflare Workers, D1 SQL query execution and PITR checks, KV namespaces, R2 buckets, Queues/DLQs, Workflows, Durable Objects, and Browser Rendering instances.
- **Codebase Memory MCP (`codebase-memory-mcp`) & `lean-ctx`**:
  - **Use for**: Knowledge graph AST indexing (`search_graph`, `trace_path`, `get_code_snippet`) combined with `lean-ctx` real-time token compression to navigate large multi-product repositories with minimal context overhead.

### C. Observability, Telemetry, and Incident MCPs

- **Sentry MCP (`sentry-mcp`)**: Pull unresolved stack traces, release regressions, and verify `apps/saas_kernel/observability.py` telemetry tags.
- **New Relic MCP (`newrelic-mcp`)**: Run NRQL queries against Cloudflare Logpush edge events and APM spans to catch 5xx spikes, slow D1 queries, or isolate memory pressure.
- **Better Stack MCP (`betterstack-mcp`)**: Inspect uptime monitors, heartbeat checks, and incident timelines feeding `ops_router.py`.
- **PostHog MCP (`posthog-mcp`)**: Query conversion funnels across `user_signed_up`, `lead_submitted`, and `quote_accepted`, inspect feature flags, and verify event volume stays under the 1M/mo ceiling.
- **Microsoft Clarity MCP (`clarity-mcp`)**: Retrieve rage-click diagnostics, dead-click selectors, and mobile layout friction metrics.
- **Grafana MCP (`grafana-mcp`)**: Audit unified alert rules and thresholds routed into `ops_router.py` and `alerting.py`.
- **Gmail MCP (`https://gmailmcp.googleapis.com/mcp/v1`)**:
  - Native Streamable HTTP integration. Use to verify end-to-end delivery of synthetic test emails in `synthetic-sink@example.com` and confirm Sev-1/Sev-2 alert formatting in `alerts@example.com` / `admin@example.com`.

### D. SEO, Search Discovery, and Growth Engine MCPs

- **Google Search Console MCP (`suganthan-gsc-mcp`)**:
  - Provides 29 tools via `GSC_KEY_FILE` or OAuth: site snapshot, quick-win keywords (positions 4-15 with high impressions), content decay detection, keyword cannibalization checks, image search SEO, URL inspection, and Indexing API batch submission.
- **GA4 & SEO Diagnostics MCP (`seo mcp serve`)**:
  - Runs automated technical site audits, crawl diffs, search performance correlation, traffic anomaly detection, and Core Web Vitals (CWV) diagnostics.
- **Autogrowth Directory MCP**:
  - Invoked directly from AI coding editors (Antigravity, Cursor, Claude Code) to compile canonical product kits, trigger automated browser playbooks across 100+ SaaS directories, and audit `data/autogrowth/ledger.jsonl`.
- **Paid Acquisition & Media MCPs**:
  - **Google Ads MCP**: Interfaces with `arbitrage_campaigns.py` and `ad_optimizer.py` for search term reports, dynamic CPC bid adjustments, and negative keyword armor synchronization.
  - **Meta / TikTok CAPI & Ads MCPs**: Audits server-side Conversions API event match quality (EMQ) and short-form vertical ad performance.
  - **YouTube Data API & Google Flow MCPs**: Manages `yt-hybrid-funnel` uploads, `relatedVideoId` linking between Shorts and Long-Form anchors, Composite Winner Score ($S_w$) analytics, and Nano Banana 2 + Veo 3.1 asset pipelines.
