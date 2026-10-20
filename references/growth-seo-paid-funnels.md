# Growth, Acquisition, Programmatic SEO, and Paid Funnel Playbooks

Use this reference during **Pass 3 (Technical SEO & pSEO)** and **Pass 4 (Autonomous Growth & Paid Funnels)** to audit, build, and optimize customer acquisition engines across the SaaS Factory.

## 1. Autogrowth and The Free MCP Growth Magnet

- **Core Product**: Directory Autopublisher for SaaS (`products/autogrowth.yaml`).
- **The "Free MCP" Developer Acquisition Loop**:
  - Expose an MCP server that developers and founders connect directly inside AI coding editors (Antigravity, Cursor, Claude Code).
  - **Scout Tier ($0 Free Magnet)**: Grants 5 free automated directory submissions/month + canonical product kit compilation + backlink ledger tracking.
  - **Upgrade Path**: When users exhaust their 5 monthly submissions or add a second product, prompt an immediate self-serve upgrade (via Stripe/RevenueCat) to **Autopilot ($49/mo)** or **Agency ($99/mo)** checked via `entitlements.can(subject, 'directory_autopilot')`.
- **Autonomous Directory Execution**:
  - Compile a single canonical product kit: taglines (short/medium/long), category mappings, feature matrix, screenshot evidence, and competitor alternatives.
  - Execute headless browser automation playbooks using vaulted email/password credentials (`.env.credentials`) to submit to 100+ directories (SaaSHub, Uneed, Product Hunt, Toolify, AlternativeTo, etc.).
  - Record every attempt, live URL, and verification timestamp in an append-only JSONL ledger (`data/autogrowth/ledger.jsonl`) to guarantee idempotency and power scheduled monthly listing re-verification.

## 2. Incumbent-Arbitrage Paid Search (Google Ads Engine)

- **Targeting Strategy (`arbitrage_campaigns.py`)**:
  - Bid exclusively on high-intent competitor switching and comparison queries: `"<competitor> alternative"`, `"<competitor> pricing"`, `"<competitor> vs"`.
  - Route clicks to dedicated, edge-cached competitor comparison landing pages showing concrete feature/price superiority against overpriced legacy incumbents (such as $99/mo legacy tools).
- **Automated Unit Economic Formulas (`ad_optimizer.py`)**:
  - **LTV Calculation**:
    $$\text{LTV} = \text{Monthly Price} \times 0.75 \text{ (Gross Margin)} \times 8 \text{ (Lifespan in months)}$$
  - **Allowable CAC (Strict 3:1 LTV:CAC Floor)**:
    $$\text{Allowable CAC} = \frac{\text{LTV}}{3}$$
  - **Maximum Rational CPC**:
    $$\text{Max CPC} = \text{Allowable CAC} \times \text{Click-to-Paid Conversion Rate}$$
  - **Weekly Scorecard Rules**: Evaluate contribution margin per owner-hour every week and automatically classify each campaign into `INCREASE SPEND`, `HOLD`, or `KILL`.
- **Negative Keyword Armor**:
  - Enforce all 26+ hardened negative keyword lists (`crack`, `torrent`, `free download`, `login`, `support`, `customer service`, `jobs`, `salary`, `careers`, `github`, `source code`, `tutorial`, `pdf`, etc.) before enabling any campaign spend.

## 3. YouTube AI Hybrid Mass-Production Funnel (`yt-hybrid-funnel`)

- **Fleet Architecture**:
  - Operate faceless media channels mapped to the 36 proven templates (`references/proven-channel-templates.md`, including 3D Isometric Forensics, Noir Corporate Collapses, and Sardonic Wealth Charts).
- **The Hybrid Funnel Flywheel**:
  - **Top of Funnel (Discovery)**: Publish 3 to 5 algorithmic YouTube Shorts per week featuring 1.8s to 2.5s cut pacing and strict visual motion resets.
  - **Middle/Bottom of Funnel (High RPM & SaaS Conversions)**: Publish 1 weekly Long-Form anchor video (10+ minutes) and link every Short directly to the anchor video via the YouTube Data API `relatedVideoId` field.
  - **Creative Engine**: Use Gemini (`thinking_level: high`) for scriptwriting and 100-point retention critiques, paired with Google Flow (Nano Banana 2 for visual consistency + Veo 3.1 for video generation).
- **Evolutionary Loop ("Promote the Winners, Kill the Losers")**:
  - Score every video weekly using the Composite Winner Score ($S_w$).
  - **Alpha Winners ($S_w >= 75$)**: Automatically double credit/budget allocation and spawn 3 mutated sequel angles.
  - **Losers ($S_w < 45$)**: Deprecate after 3 consecutive cycles and rotate the slot to an alternative channel template.

## 4. Meta and TikTok Paid Social & Short-Form Video

- **Deterministic Code-Driven Video (`HyperFrames` & `media-use`)**:
  - Render product motion graphics deterministically via GSAP, HTML5 canvas, and Remotion ports.
  - Structure every ad with: (1) a 3-second visual scroll-stopper, (2) a concrete problem/solution product demonstration, and (3) a direct CTA.
- **Multi-Platform 9:16 Repurposing**:
  - Auto-adapt top-performing Shorts into 9:16 vertical videos with burned-in kinetic typography for TikTok Spark Ads, Instagram Reels, and YouTube Shorts.
- **Server-Side Conversions API (CAPI)**:
  - Fire all conversion events (`user_signed_up`, `lead_submitted`, `quote_accepted`, `purchase_completed`) from Cloudflare Workers via server-side Meta CAPI and TikTok Events API with hashed first-party identifiers to ensure 100% signal capture across ad-blockers and iOS Safari ITP.

## 5. Programmatic SEO (pSEO) and Real-Utility Tooling

- **Strict Anti-Doorway Standard (Rule 20)**:
  - Never generate low-value, generic AI text articles.
  - Every programmatic page must execute real server/edge calculations, interactive client-side tests, or live directory aggregations (examples: dynamic pricing calculators, SMS segment/PDU calculators, webhook payload validators, real-time benchmarks).
- **Sub-10ms Edge Caching**:
  - Cache all public pSEO tools and competitor comparison pages at the Cloudflare Edge using Workers Caching with explicit `cache-tags` (such as `product:123`, `category:seo`) so repeat visitors achieve sub-10ms TTFB without invoking the Python isolate.
- **Instant Edge Indexing**:
  - Upon page publish or dataset update, invoke private IndexNow service bindings (`env.SHARED_INDEXNOW`) to push URLs immediately to Bing, Yandex, and Seznam edge bots, and submit high-priority URLs via `suganthan-gsc-mcp`.
