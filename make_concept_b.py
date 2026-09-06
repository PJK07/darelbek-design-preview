import os

css_content = """/* ==========================================================================
   DAR EL BEK — CONCEPT B: MINIMAL FINE DINING ("HAUTE CUISINE")
   Swiss Architectural Minimalism · Zero Border-Radius · Strict Tabular Grid
   ========================================================================== */

:root {
  --color-black: #000000;
  --color-white: #FFFFFF;
  --color-gray-dark: #121212;
  --color-gray-mid: #666666;
  --color-gray-light: #E0E0E0;
  --color-gray-subtle: #F6F6F6;
  
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'Space Grotesk', monospace, sans-serif;
  
  /* Universal Zero-Radius Constraint */
  --radius-zero: 0px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  border-radius: 0 !important; /* Strict Swiss geometric discipline */
  -webkit-tap-highlight-color: transparent;
}

html {
  scroll-behavior: smooth;
  background-color: var(--color-white);
  color: var(--color-black);
}

body {
  font-family: var(--font-sans);
  font-size: 14px;
  line-height: 1.5;
  color: var(--color-black);
  background-color: var(--color-white);
  -webkit-font-smoothing: antialiased;
  font-variant-numeric: tabular-nums;
  overflow-x: hidden;
}

.mono {
  font-family: var(--font-mono);
}

/* Master Grid Container */
.b-container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding-left: clamp(16px, 3vw, 40px);
  padding-right: clamp(16px, 3vw, 40px);
}

/* Header */
.b-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--color-white);
  border-bottom: 1px solid var(--color-black);
}

.b-header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.b-brand {
  font-family: var(--font-mono);
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-black);
  text-decoration: none;
}

.b-header-status {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-gray-mid);
}

.b-header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.b-btn-cart {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--color-black);
  color: var(--color-white);
  border: 1px solid var(--color-black);
  padding: 8px 16px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: none; /* Instant Swiss interaction */
}

.b-btn-cart:hover {
  background: var(--color-white);
  color: var(--color-black);
}

/* Layout: Left Navigation Rail + Right Scrolling Catalog */
.b-layout-split {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0;
  border-left: 1px solid var(--color-gray-light);
  border-right: 1px solid var(--color-gray-light);
}

@media (min-width: 1024px) {
  .b-layout-split {
    grid-template-columns: 320px 1fr;
  }
}

/* Sticky Left Rail */
.b-rail {
  display: none;
}

@media (min-width: 1024px) {
  .b-rail {
    display: block;
    position: sticky;
    top: 65px;
    height: calc(100vh - 65px);
    overflow-y: auto;
    padding: 36px 28px;
    border-right: 1px solid var(--color-gray-light);
    background: var(--color-white);
  }
}

.b-rail-section-title {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--color-gray-mid);
  margin-bottom: 24px;
}

.b-rail-nav-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.b-rail-link {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 600;
  color: var(--color-gray-mid);
  padding: 8px 0;
  border-bottom: 1px solid transparent;
  cursor: pointer;
}

.b-rail-link:hover,
.b-rail-link.active {
  color: var(--color-black);
  border-bottom-color: var(--color-black);
}

.b-rail-count {
  font-size: 11px;
  color: var(--color-gray-mid);
}

/* Mobile Sticky Category Strip */
.b-mobile-categories {
  display: flex;
  overflow-x: auto;
  border-bottom: 1px solid var(--color-black);
  background: var(--color-white);
  position: sticky;
  top: 64px;
  z-index: 40;
  scrollbar-width: none;
}

@media (min-width: 1024px) {
  .b-mobile-categories {
    display: none;
  }
}

.b-mobile-cat-link {
  flex-shrink: 0;
  padding: 12px 18px;
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-gray-mid);
  text-decoration: none;
  border-right: 1px solid var(--color-gray-light);
}

.b-mobile-cat-link.active {
  color: var(--color-black);
  background: var(--color-gray-subtle);
}

/* Right Content Stream */
.b-catalog-stream {
  padding: 0;
}

/* Manifesto / Architecture Intro */
.b-manifesto {
  padding: 48px clamp(20px, 4vw, 48px);
  border-bottom: 1px solid var(--color-gray-light);
  background: var(--color-white);
}

.b-manifesto-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

@media (min-width: 860px) {
  .b-manifesto-grid {
    grid-template-columns: 1.4fr 0.6fr;
  }
}

.b-manifesto-headline {
  font-family: var(--font-mono);
  font-size: clamp(24px, 3.2vw, 38px);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.b-manifesto-body {
  font-size: 15px;
  color: var(--color-gray-mid);
  line-height: 1.6;
  max-width: 600px;
}

.b-manifesto-specs {
  border-top: 1px solid var(--color-black);
  padding-top: 16px;
  font-family: var(--font-mono);
  font-size: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

/* Category Sections */
.b-section {
  border-bottom: 2px solid var(--color-black);
}

.b-section-header {
  padding: 24px clamp(20px, 4vw, 48px);
  background: var(--color-white);
  border-bottom: 1px solid var(--color-gray-light);
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.b-section-code {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
}

.b-section-title {
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

/* Feature Architectural Spread */
.b-feature-spread {
  display: grid;
  grid-template-columns: 1fr;
  border-bottom: 1px solid var(--color-gray-light);
  cursor: pointer;
}

@media (min-width: 860px) {
  .b-feature-spread {
    grid-template-columns: 1fr 1fr;
  }
}

.b-feature-img-cell {
  position: relative;
  aspect-ratio: 16 / 11;
  background: var(--color-gray-light);
  overflow: hidden;
  border-bottom: 1px solid var(--color-gray-light);
}

@media (min-width: 860px) {
  .b-feature-img-cell {
    border-bottom: none;
    border-right: 1px solid var(--color-gray-light);
  }
}

.b-feature-img-cell img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.b-feature-data-cell {
  padding: 36px clamp(20px, 4vw, 48px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.b-feature-item-code {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.14em;
  color: var(--color-gray-mid);
  margin-bottom: 8px;
}

.b-feature-item-name {
  font-size: 22px;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 12px;
}

.b-feature-item-desc {
  font-size: 14px;
  color: var(--color-gray-mid);
  line-height: 1.6;
  margin-bottom: 24px;
}

.b-feature-action-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-gray-light);
  padding-top: 20px;
}

.b-feature-price {
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 700;
}

.b-btn-action {
  background: var(--color-black);
  color: var(--color-white);
  border: 1px solid var(--color-black);
  padding: 10px 20px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

.b-btn-action:hover {
  background: var(--color-white);
  color: var(--color-black);
}

/* Architectural Data Rows */
.b-data-table {
  width: 100%;
}

.b-data-row {
  display: grid;
  grid-template-columns: 64px 1fr auto;
  gap: 16px;
  align-items: center;
  padding: 18px clamp(20px, 4vw, 48px);
  border-bottom: 1px solid var(--color-gray-light);
  cursor: pointer;
  transition: background-color 0.05s;
}

.b-data-row:hover {
  background-color: var(--color-gray-subtle);
}

.b-data-thumb {
  width: 64px;
  height: 64px;
  object-fit: cover;
  background: var(--color-gray-light);
}

.b-data-title {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 4px;
}

.b-data-desc {
  font-size: 13px;
  color: var(--color-gray-mid);
}

.b-data-price-cell {
  text-align: right;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
}

.b-data-price {
  font-family: var(--font-mono);
  font-size: 15px;
  font-weight: 700;
}

.b-data-usd {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--color-gray-mid);
}

/* Floating Bottom Trigger for Mobile */
.b-floating-cart {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: var(--color-black);
  color: var(--color-white);
  padding: 16px clamp(16px, 4vw, 40px);
  z-index: 45;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  border-top: 1px solid var(--color-black);
}

/* Slide-Over Drawer */
.b-drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 100;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.15s ease;
}

.b-drawer-backdrop.active {
  opacity: 1;
  pointer-events: auto;
}

.b-drawer-panel {
  position: fixed;
  top: 0;
  right: 0;
  width: 100%;
  max-width: 460px;
  height: 100%;
  background: var(--color-white);
  border-left: 1px solid var(--color-black);
  z-index: 101;
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.b-drawer-backdrop.active .b-drawer-panel {
  transform: translateX(0);
}

.b-drawer-head {
  padding: 24px;
  border-bottom: 1px solid var(--color-black);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.b-drawer-head h3 {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.b-drawer-close {
  background: none;
  border: none;
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
}

.b-drawer-body {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
}

.b-drawer-foot {
  padding: 24px;
  border-top: 1px solid var(--color-black);
  background: var(--color-gray-subtle);
}

.b-cart-item {
  display: grid;
  grid-template-columns: 50px 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid var(--color-gray-light);
}

.b-cart-thumb {
  width: 50px;
  height: 50px;
  object-fit: cover;
  background: var(--color-gray-light);
}

/* Modal for Customization */
.b-modal-panel {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 90%;
  max-width: 540px;
  background: var(--color-white);
  border: 1px solid var(--color-black);
  z-index: 110;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
}

/* Checkout View */
.b-checkout-view {
  position: fixed;
  inset: 0;
  background: var(--color-white);
  z-index: 120;
  overflow-y: auto;
  display: none;
}

.b-checkout-view.active {
  display: block;
}

.b-checkout-nav {
  height: 64px;
  border-bottom: 1px solid var(--color-black);
  display: flex;
  align-items: center;
  padding: 0 clamp(16px, 3vw, 40px);
}

.b-checkout-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0;
  max-width: 1400px;
  margin: 0 auto;
}

@media (min-width: 960px) {
  .b-checkout-grid {
    grid-template-columns: 1.1fr 0.9fr;
  }
}

.b-checkout-left {
  padding: 40px clamp(16px, 4vw, 48px);
  border-right: 1px solid var(--color-gray-light);
}

.b-checkout-right {
  padding: 40px clamp(16px, 4vw, 48px);
  background: var(--color-gray-subtle);
}

.b-field-group {
  margin-bottom: 20px;
}

.b-field-label {
  display: block;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.b-input, .b-select {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid var(--color-black);
  background: var(--color-white);
  font-family: var(--font-sans);
  font-size: 14px;
  outline: none;
}

.b-receipt-table {
  width: 100%;
  border-collapse: collapse;
}

.b-receipt-table td {
  padding: 10px 0;
  border-bottom: 1px solid var(--color-gray-light);
}

.b-receipt-table tr.total-row td {
  border-top: 2px solid var(--color-black);
  border-bottom: none;
  font-family: var(--font-mono);
  font-size: 16px;
  font-weight: 700;
  padding-top: 16px;
}
"""

with open('/root/dar-el-bek/design-preview/concept-b/style.css', 'w') as f:
    f.write(css_content)
print("Concept B style.css written successfully!")
