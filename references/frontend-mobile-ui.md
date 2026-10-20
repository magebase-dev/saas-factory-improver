# Frontend, UI Layout, and Mobile Platform Standards

Use this reference during **Pass 2** when auditing or building templates, stylesheets, HTMX interactions, back-office admin screens, or mobile PWA/Capacitor/TWA packages.

## 1. Server-Side Rendering and Asset Delivery

- **SSR Stack**: Build user interfaces with **Django Templates + Native Template Partials + HTMX**.
- **Zero Heavy Client JS Bundles**: Do not introduce React, Vue, or heavy SPA bundlers for standard SaaS views. Use HTMX attributes (`hx-get`, `hx-post`, `hx-target`, `hx-swap`) paired with Django partial template rendering for fast, low-memory interactivity.
- **Edge Static Assets**: Serve all CSS, SVGs, fonts, and static JS directly from the Cloudflare CDN edge via **Cloudflare Static Assets**, bypassing Python Worker isolate execution completely.
- **Back-Office UI**: All internal administration interfaces must use **Django Admin + Unfold design system** for a unified, modern operator experience.

## 2. Canonical UI and Layout Standard

- **1440px Canonical Grid**:
  - Desktop container standard:
    ```css
    .canonical-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 48px;
    }
    ```
  - Mobile breakpoint standard (`<=768px`):
    ```css
    @media (max-width: 768px) {
      .canonical-container {
        padding: 0 24px; /* or 0 16px for dense data views */
      }
    }
    ```
- **Vector Icons Only (Strict Emoji Ban)**:
  - Unicode emojis are strictly banned across all UI templates, buttons, badges, empty states, and notifications.
  - Render 100% crisp vector SVG icons via **IconKit**.
- **Smart Inputs & Autocomplete**:
  - Implement accessible **WAI-ARIA 1.2 Combobox** autocomplete dropdowns (`role="combobox"`, `aria-expanded`, `aria-controls`, `aria-activedescendant`, keyboard arrow navigation).
  - For location and address fields, route queries through a **server-side proxied Google Places Autocomplete (New)** endpoint cached in Cloudflare KV to protect API keys, lower latency, and reduce per-keystroke billing.

## 3. Mobile SaaS Delivery (PWA, Capacitor, and TWA)

- **Web / PWA First**:
  - Every product must ship a valid `manifest.json`, touch-optimized tap targets (`>=44x44px`), viewport safe-area insets (`env(safe-area-inset-*)`), and offline-resilient service workers that never cache authenticated `__Host-` HTML responses improperly.
- **App Stores and Portals**:
  - Package web/PWA properties into native Android distributions using **Trusted Web Activities (TWA)** (`assetlinks.json` digital asset links verified at `/.well-known/assetlinks.json`) and **Capacitor** wrappers.
  - Automate AAB/APK builds, store listings, and release track promotions to the Google Play Store using `play-store-mcp` (`play-store-service-account.json`).
  - Synchronize in-app Play Store subscriptions and web Stripe subscriptions into unified D1 tenant entitlements via **RevenueCat MCP**.

## 4. Simulated User Critique Protocol

When running a "Simulated User Feedback" or "SaaS Critique" pass on the frontend:

1. **First-Impression Clarity (5-Second Test)**: Does the hero section state the exact problem solved, the concrete utility, and a friction-free primary CTA above the fold on both 1440px desktop and 390px mobile viewports?
2. **Time-to-Value (Aha! Moment)**: Count the number of clicks and form fields between landing and experiencing live utility. Eliminate unnecessary pre-activation fields.
3. **HTMX State Completeness**: Verify every HTMX partial swap includes loading indicators (`hx-indicator`), graceful error states, and zero layout shift (CLS).
4. **Paywall & Upgrade Friction**: Check that hitting a free-tier limit (such as the 5 free directory submissions/mo in Scout Tier) triggers an inline, contextual upgrade path powered by Stripe or RevenueCat without losing the user's current input state.
