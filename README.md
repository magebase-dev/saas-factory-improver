# SaaS Factory Improver (`saas-factory-improver`)

An orchestrator skill and audit suite for AI coding agents (Antigravity, Cursor, Claude Code) to audit, debug, harden, and scale modern micro-SaaS and SaaS Factory repositories built on **Cloudflare Python Workers (Python 3.14 via Pyodide / WebAssembly)**, **Django 6.1 (WSGI)**, **Cloudflare D1**, **Cloudflare R2**, **HTMX**, **Capacitor / TWA**, and the **MCP (Model Context Protocol) fleet**.

---

## Architecture Overview

Instead of overwhelming LLM context windows by injecting entire encyclopedic runbooks at once, `saas-factory-improver` uses **progressive disclosure** across four sequential execution passes:

1. **Pass 1: Edge Runtime, Reliability & Security Triage**
   - 128 MB Pyodide isolate memory ceiling & `cpu_ms = 1000` / `subrequests = 100` caps.
   - Cloudflare D1 SQL query optimization (eliminating N+1 table scans) & PITR validation.
   - Zero-buffer direct client-to-R2 presigned uploads.
   - Cloudflare Queues with Dead-Letter Queues (`*-dlq`) & idempotency keys.
   - Host-only session cookies (`__Host-`) & strict multi-tenant `tenant_id` boundaries.
   - Unified alert routing (`ops_router.py` + `alerting.py`) with 300s cooldown deduplication.

2. **Pass 2: Frontend, Mobile PWA/TWA & Monetization Audit**
   - Django Templates + Native Template Partials + HTMX (zero heavy client JS bundles).
   - Canonical 1440px desktop grid (`padding: 0 48px;`) scaling to mobile `<=768px` (`0 24px/16px`).
   - 100% Vector SVG icons via IconKit (strict ban on Unicode emojis in UI).
   - WAI-ARIA 1.2 Combobox with server-side proxied Google Places Autocomplete (New).
   - Trusted Web Activity (TWA) & Capacitor packaging for Google Play Store delivery.
   - Capability-based entitlements (`entitlements.can(subject, 'feature')`) unifying Stripe (web) and RevenueCat / Google Play Billing (mobile).

3. **Pass 3: Technical SEO, Programmatic SEO (pSEO) & Instant Indexing**
   - Google Search Console MCP (`suganthan-gsc-mcp`) & GA4/SEO Diagnostics (`seo mcp serve`).
   - Rule 20 Strict Anti-Doorway Standard: pSEO pages must provide real utility (interactive calculators, live directory aggregations, API testers).
   - Sub-10ms Cloudflare Edge Workers Caching with granular `cache-tags`.
   - Private IndexNow service bindings pushing new/updated URLs to Bing, Yandex, and Seznam.

4. **Pass 4: Autonomous Distribution & Growth Engines**
   - Autogrowth Free MCP developer acquisition funnel (5 free directory submissions/mo Scout tier).
   - Competitor-intent Google Ads search arbitrage enforcing a 3:1 LTV:CAC floor & negative keyword armor.
   - YouTube AI Hybrid Funnel (discovery Shorts + high-RPM long-form anchor videos).
   - Server-Side Conversions API (Meta CAPI & TikTok Events API) via Cloudflare Workers.

---

## Quick Start & Installation

### Option 1: Install into Google Antigravity CLI (`agy`)

To install into your global Antigravity skills directory:

```bash
# Clone the repository
git clone https://github.com/magebase-dev/saas-factory-improver.git ~/.gemini/antigravity-cli/skills/saas-factory-improver

# Or use antigravity CLI:
antigravity use saas-factory-improver
```

### Option 2: Project-Level Installation

Drop the skill directly into your repository's `.agents/skills/` directory:

```bash
mkdir -p .agents/skills/
git clone https://github.com/magebase-dev/saas-factory-improver.git .agents/skills/saas-factory-improver
```

---

## Static Compliance Auditor

Run the included compliance script against any product workspace or Django repository:

```bash
python3 scripts/audit_factory_repo.py /path/to/your/saas-repo
```

The script audits:
- `wrangler.toml` / `wrangler.jsonc` configs for `workers_dev = false`, `cpu_ms = 1000`, and queue DLQ pairs.
- Python codebase for hardcoded plan strings (`user.plan == 'pro'`) vs `entitlements.can()`.
- Django settings for `SESSION_COOKIE_SECURE = True`, strict `__Host-` cookie prefixes, and absence of wildcard domains.
- HTML templates for banned Unicode emojis and absence of the canonical 1440px grid standard.

---

## Repository Structure

```
saas-factory-improver/
├── SKILL.md                                 # Main Antigravity skill definition & orchestrator prompt
├── README.md                                # Public documentation & quickstart
├── LICENSE                                  # MIT License
├── scripts/
│   └── audit_factory_repo.py                # Static compliance validator
└── references/
    ├── core-edge-django.md                  # Pass 1: Cloudflare Workers, Django 6.1 WSGI, D1, R2, Queues
    ├── frontend-mobile-ui.md                # Pass 2: HTMX, 1440px grid, IconKit, TWA, Play Store
    ├── growth-seo-paid-funnels.md           # Pass 3 & 4: Free MCP, pSEO, Google Ads arbitrage, CAPI
    └── observability-and-mcp-fleet.md       # Complete MCP integration matrix & $0 Observability fleet
```

---

## License

MIT License. Free to use, adapt, and distribute across commercial and open-source projects.
