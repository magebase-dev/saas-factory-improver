---
name: saas-factory-improver
description: Comprehensive orchestrator skill to audit, debug, optimize, and grow SaaS Factory repositories built on Cloudflare Python Workers, Django 6.1, D1, R2, HTMX, Capacitor/TWA, and the MCP growth and observability fleet. Use whenever the user asks to "improve a repo", audit a product workspace, fix production defects, optimize unit economics, boost SEO/pSEO, wire Stripe/RevenueCat/Play Store billing, or scale organic and paid growth.
---
# SaaS Factory Improver

This skill acts as a VP of Engineering and Growth orchestrator for the SaaS Factory fleet. Instead of loading every domain rule at once and diluting attention, it uses progressive disclosure across four sequential execution passes to diagnose defects, harden edge infrastructure, refine UI/mobile experiences, and scale organic and paid acquisition loops.

## When to Use

- Auditing or improving a SaaS product workspace (`products/<product>/`) or shared factory package (`packages/factory-*/`)
- Triaging production incidents, memory budget overruns, or slow queries across Cloudflare Python Workers, Django 6.1, and D1
- Wiring or auditing MCP integrations including Stripe MCP, RevenueCat MCP, Google Play Developer MCP (`play-store-mcp`), Cloudflare MCP, GSC MCP, GA4/SEO MCP, Sentry, New Relic, PostHog, Better Stack, and Gmail MCP
- Reviewing frontend templates, HTMX interactions, Unfold admin views, or Capacitor/TWA mobile builds against canonical UI standards
- Launching or optimizing growth engines: Autogrowth Free MCP funnel, Incumbent-Arbitrage Google Ads, Programmatic SEO utility tools, YouTube AI Hybrid Funnels, or Meta/TikTok CAPI video pipelines

## Core Workflow: The 4-Pass Execution Engine

When asked to improve, audit, or scale a repository, do not attempt all changes in a single unfocused pass. Execute the workflow below in order, loading only the reference files needed for the current pass.

### Step 1: Context Discovery and Static Audit

Before reading full files, map the codebase efficiently to preserve context budget:

1. Use `codebase-memory-mcp` (`search_graph`, `trace_path`, `get_code_snippet`) and `lean-ctx` to locate product boundaries under `products/<product>/` and shared modules under `packages/factory-*/`.
2. Run the automated static compliance script if local execution is available:
   ```bash
   python3 scripts/audit_factory_repo.py <path-to-product-or-repo>
   ```
3. Classify the highest-leverage bottlenecks into four pass queues: Edge & Reliability, UI & Mobile, Billing & Entitlements, and Growth & Distribution.

### Step 2: Pass 1 - Edge Runtime, Security, and Observability Triage

Read `references/core-edge-django.md` and `references/observability-and-mcp-fleet.md` before executing this pass.

1. Query live telemetry via **Sentry MCP**, **New Relic MCP**, and **Better Stack MCP** to identify active Sev-1/Sev-2 errors, slow D1 queries, or Worker invocations approaching the 128 MB Pyodide isolate memory limit or `cpu_ms = 1000` / `subrequests = 100` caps.
2. Verify that `ops_router.py` and `alerting.py` enforce the 300-second cooldown deduplication and route Sev-1/Sev-2 escalations to `alerts@yourdomain.com`.
3. Confirm Cloudflare Browser Run + `@cloudflare/playwright` synthetics validate hot-paths using HMAC-SHA256 (`X-Synthetic-Run`) and route test emails to `synthetic-sink@yourdomain.com` (verified via **Gmail MCP**).
4. Audit every Django view and D1 query for explicit `tenant_id` isolation, `__Host-` session cookies (`SESSION_COOKIE_SECURE = True`), and direct email/password auth via `allauth` (Rule 34).

### Step 3: Pass 2 - Frontend, Mobile PWA/TWA, and Monetization Audit

Read `references/frontend-mobile-ui.md` and `references/observability-and-mcp-fleet.md` before executing this pass.

1. Inspect **Microsoft Clarity** heatmaps/rage-clicks and **PostHog MCP** semantic conversion funnels (`user_signed_up`, `lead_submitted`, `quote_accepted`) to spot onboarding drop-offs.
2. Enforce UI layout rules: 1440px canonical grid (`max-width: 1440px; margin: 0 auto; padding: 0 48px;` on desktop, `0 24px` or `0 16px` at `<=768px`), 100% vector SVG icons via IconKit (zero Unicode emojis), WAI-ARIA 1.2 Combobox with server-proxied Google Places Autocomplete (New), and SSR Django Templates + Template Partials + HTMX.
3. Audit monetization and cross-platform entitlements using **Stripe MCP**, **RevenueCat MCP**, and **Google Play Developer MCP** (`play-store-mcp`):
   - Verify all permission checks use `entitlements.can(subject, 'feature')` rather than hardcoded plan strings.
   - Ensure Stripe webhooks and RevenueCat mobile subscription events synchronize cleanly into D1 tenant capability records.
   - Validate Capacitor and Trusted Web Activity (TWA) configurations and release track promotions via `play-store-mcp`.

### Step 4: Pass 3 - Technical SEO, pSEO Utility Pages, and IndexNow

Read `references/growth-seo-paid-funnels.md` before executing this pass.

1. Run **Google Search Console MCP** (`suganthan-gsc-mcp`) and **GA4 & SEO Diagnostics MCP** (`seo mcp serve`) to pull quick-win keywords, content decay, cannibalization issues, and Core Web Vitals regressions.
2. Audit Programmatic SEO (pSEO) routes against **Rule 20 (Strict Anti-Doorway Standard)**: every pSEO page must provide interactive utility (real calculators, live directory aggregations, or client-side testers) and never thin AI prose.
3. Verify pSEO and comparison pages use Cloudflare Workers Caching with granular `cache-tags` (such as `product:123`, `category:seo`) for sub-10ms TTFB without waking the Python isolate.
4. Confirm publish hooks trigger private IndexNow service bindings to push updated URLs immediately to Bing, Yandex, and Seznam.

### Step 5: Pass 4 - Autonomous Distribution and Paid Growth Engines

Read `references/growth-seo-paid-funnels.md` before executing this pass.

1. **Autogrowth Free MCP Funnel**: Verify the product has a canonical product kit in `products/autogrowth.yaml`, idempotent tracking in `data/autogrowth/ledger.jsonl`, and clear upgrade prompts from the Scout Tier ($0, 5 submissions/mo) to Autopilot ($49/mo) and Agency ($99/mo).
2. **Incumbent-Arbitrage Google Ads**: Audit `arbitrage_campaigns.py` and `ad_optimizer.py` to ensure competitor-switching campaigns (`"<competitor> alternative"`, `"<competitor> pricing"`, `"<competitor> vs"`) enforce the 3:1 LTV-to-CAC floor, dynamic Max CPC caps, and all 26+ negative keyword armor lists.
3. **Short-Form & Hybrid Video Funnels**: Align `yt-hybrid-funnel` scripts and HyperFrames/`media-use` renders with the Composite Winner Score ($S_w$) evolutionary loop (double down on $S_w >= 75$, kill $S_w < 45$ after 3 cycles) and verify Cloudflare Worker server-side Conversions API (CAPI) signal capture for Meta and TikTok.

## Reference Files

Load these files on demand during the corresponding pass:

- `references/core-edge-django.md`: Rules for Cloudflare Python Workers (Pyodide/WASM 128 MB budget), Django 6.1 WSGI, D1, R2 presigned uploads, KV, Queues/DLQs, Workflows, Durable Objects, and Security/Tenant Isolation.
- `references/frontend-mobile-ui.md`: Standards for Django Templates + HTMX, 1440px canonical grid, IconKit SVGs, WAI-ARIA 1.2 Combobox, Unfold Admin, and PWA/Capacitor/TWA Play Store delivery.
- `references/observability-and-mcp-fleet.md`: Complete runbook for the $0 Observability Fleet and every MCP integration (Stripe, RevenueCat, Google Play Developer, Cloudflare, GSC, SEO/GA4, Sentry, New Relic, PostHog, Better Stack, Clarity, Gmail, Codebase Memory).
- `references/growth-seo-paid-funnels.md`: Playbooks for Autogrowth Free MCP acquisition, Google Ads incumbent arbitrage unit economics, YouTube AI Hybrid Funnel, Meta/TikTok CAPI, and Rule 20 pSEO.

## Gotchas

- **Never buffer uploads in Worker memory**: Pyodide isolates have a strict 128 MB ceiling. Always route file uploads directly from client to Cloudflare R2 via presigned URLs and trigger downstream processing via R2 event notifications and Cloudflare Queues.
- **Never hardcode plan names**: Checking `user.plan == 'pro'` breaks cross-platform synchronization between Stripe and RevenueCat. Always evaluate `entitlements.can(subject, 'feature')`.
- **Never burn PostHog quota on noisy UI clicks**: Keep PostHog strictly below the 1M events/mo free tier by sending only high-value semantic business events (`user_signed_up`, `lead_submitted`, `quote_accepted`). Use Microsoft Clarity for session replays and rage-click diagnostics.
- **Never ship Unicode emojis in UI templates**: Replace all emoji characters with vector SVGs via IconKit.
