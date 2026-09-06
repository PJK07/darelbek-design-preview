import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Dar El Bek (دار البيك) — Concept C: Modern High-Contrast</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>

  <!-- Top Announcement Bar -->
  <aside style="background:#111; color:#fff; text-align:center; padding:8px 16px; font-family:var(--font-display); font-size:11px; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #222;">
    Dar El Bek · Design Direction C · Modern High-Contrast Hospitality · For Client Approval
  </aside>

  <!-- Header -->
  <header class="c-header">
    <div class="c-container">
      <div class="c-header-inner">
        <a href="#" class="c-brand">
          <div class="c-brand-title">DAR EL BEK</div>
          <div class="c-brand-sub">دار البيك // NOCTURNAL HEARTH</div>
        </a>
        <div style="font-size:12px; color:var(--c-gray-mid); font-weight:600;" class="hidden-mobile">
          MTAYLEB KITCHEN // 11:30–23:00 // LIVE ORDERS
        </div>
        <button class="c-btn-cart" onclick="openCart()">
          <span>SELECTION</span>
          <span id="c-cart-count" style="background:#000; color:#fff; padding:2px 7px; font-size:11px; font-weight:800;">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Category Nav -->
  <nav class="c-cat-rail">
    <div class="c-container">
      <div class="c-cat-track">
        <a href="#sec-c-grill" class="c-cat-link active" onclick="setActiveNav(this)">// 01 CHARCOAL</a>
        <a href="#sec-c-broasted" class="c-cat-link" onclick="setActiveNav(this)">// 02 BROASTED</a>
        <a href="#sec-c-machawi" class="c-cat-link" onclick="setActiveNav(this)">// 03 MACHAWI</a>
        <a href="#sec-c-mezze" class="c-cat-link" onclick="setActiveNav(this)">// 04 MEZZE</a>
        <a href="#sec-c-wraps" class="c-cat-link" onclick="setActiveNav(this)">// 05 WRAPS</a>
        <a href="#sec-c-hpc" class="c-cat-link" onclick="setActiveNav(this)">// 06 HIGH PROTEIN</a>
      </div>
    </div>
  </nav>

  <main class="c-container">
    <!-- Hero Section -->
    <section class="c-hero">
      <div class="c-hero-grid">
        <div>
          <div class="c-hero-tag">CHIAROSCURO CULINARY STAGE // BEIRUT</div>
          <h1 class="c-hero-title">FIRED IN CHARCOAL. BORN IN BEIRUT.</h1>
          <p class="c-hero-desc">
            Natural lump oak embers searing heritage poultry at 900°. Pure cold-whipped mountain toum. Hand-stretched flatbreads charred directly on iron grids.
          </p>
          <div style="display:flex; gap:32px; font-size:12px; font-family:var(--font-display); font-weight:700; letter-spacing:0.1em; color:var(--c-gray-mid); text-transform:uppercase;">
            <div>[ OAK WOOD FIRED ]</div>
            <div>[ COLD WHIPPED TOUM ]</div>
            <div>[ 100% FARM CHICKEN ]</div>
          </div>
        </div>
        <div class="c-hero-img-box">
          <img src="../assets/chargrilled-boneless-chicken.jpg" alt="Charcoal Chicken"/>
        </div>
      </div>
    </section>

    <!-- SECTION 01: CHARCOAL -->
    <section id="sec-c-grill" class="c-section">
      <div class="c-section-head">
        <div>
          <span class="c-section-num">DIVISION // 01</span>
          <h2 class="c-section-title">THE CHARCOAL HEARTH</h2>
        </div>
        <div style="font-size:13px; color:var(--c-gray-mid);">Deboned &amp; whole birds blistered over natural oak</div>
      </div>

      <!-- Inverted High-Contrast Burst Dish -->
      <article class="c-burst-dish" onclick="openDetail('farrouj-fahem-msahab', 'Farrouj Fahem Msahab', 'فروج مسحّب عالفحم', '2,058,500 L.L.', '$23.00', 'Deboned whole chicken steeped for 24 hours in garlic brine and wild thyme, slow-roasted over oak embers. Served with scratch toum, Lebanese pickles, and blistered flatbread.', '../assets/chargrilled-boneless-chicken.jpg')">
        <div class="c-burst-photo">
          <img src="../assets/chargrilled-boneless-chicken.jpg" alt="Farrouj Fahem Msahab"/>
        </div>
        <div class="c-burst-info">
          <div>
            <div class="c-burst-tag">SIGNATURE SPECIFICATION // SERVES 2</div>
            <h3 class="c-burst-title">FARROUJ FAHEM MSAHAB</h3>
            <p class="c-burst-desc">Deboned whole chicken steeped for 24 hours in mountain garlic emulsion and wild thyme, blistered slowly over glowing citrus coals. Accompanied by fresh toum, pickled turnip, and hand-stretched bread.</p>
          </div>
          <div>
            <div class="c-burst-price">2,058,500 L.L. <span style="font-size:14px; color:#666; font-weight:500;">(~$23.00 USD)</span></div>
            <button class="c-btn-burst" onclick="event.stopPropagation(); quickAdd('Farrouj Fahem Msahab', 2058500, '$23.00', '../assets/chargrilled-boneless-chicken.jpg')">
              + ADD TO SELECTION
            </button>
          </div>
        </div>
      </article>

      <!-- Dark Rows -->
      <div class="c-row-table">
        <div class="c-row-dish" onclick="openDetail('farrouj-fahem', 'Farrouj Fahem (Whole)', 'فروج عالفحم', '1,745,250 L.L.', '$19.50', 'Whole bone-in chicken slow-roasted on the spit over natural oak charcoal. Served with whipped toum and pickles.', '../assets/chargrilled-chicken.jpg')">
          <div class="c-row-main">
            <img src="../assets/chargrilled-chicken.jpg" class="c-row-thumb" alt="Farrouj Fahem"/>
            <div>
              <h4 class="c-row-title">FARROUJ FAHEM (WHOLE) // فروج عالفحم</h4>
              <p class="c-row-desc">Whole bone-in chicken caramelized over natural embers. Toum &amp; bread.</p>
            </div>
          </div>
          <div class="c-row-right">
            <span class="c-row-price">1,745,250 L.L.</span>
            <button class="c-btn-mini" onclick="event.stopPropagation(); quickAdd('Farrouj Fahem (Whole)', 1745250, '$19.50', '../assets/chargrilled-chicken.jpg')">+</button>
          </div>
        </div>

        <div class="c-row-dish" onclick="openDetail('half-farrouj', 'Half Farrouj Fahem', 'نصف فروج عالفحم', '1,163,500 L.L.', '$13.00', 'Half chargrilled bird with garlic paste, wild cucumber pickles, and fresh flatbread.', '../assets/chargrilled-chicken.jpg')">
          <div class="c-row-main">
            <img src="../assets/chargrilled-chicken.jpg" class="c-row-thumb" alt="Half Farrouj"/>
            <div>
              <h4 class="c-row-title">HALF FARROUJ FAHEM // نصف فروج عالفحم</h4>
              <p class="c-row-desc">Half bird charred over citrus coals. Garlic paste and flatbread.</p>
            </div>
          </div>
          <div class="c-row-right">
            <span class="c-row-price">1,163,500 L.L.</span>
            <button class="c-btn-mini" onclick="event.stopPropagation(); quickAdd('Half Farrouj Fahem', 1163500, '$13.00', '../assets/chargrilled-chicken.jpg')">+</button>
          </div>
        </div>

        <div class="c-row-dish" onclick="openDetail('wings-fahem', 'Wings Fahem (6 pcs)', 'جوانح عالفحم', '1,163,500 L.L.', '$13.00', 'Six crispy charred chicken wings brushed with fresh lemon-garlic emulsion.', '../assets/wings-garlic-sauce.jpg')">
          <div class="c-row-main">
            <img src="../assets/wings-garlic-sauce.jpg" class="c-row-thumb" alt="Wings Fahem"/>
            <div>
              <h4 class="c-row-title">WINGS FAHEM (6 PIECES) // جوانح عالفحم</h4>
              <p class="c-row-desc">Oak-charred wings basted in cold garlic emulsion and lemon juice.</p>
            </div>
          </div>
          <div class="c-row-right">
            <span class="c-row-price">1,163,500 L.L.</span>
            <button class="c-btn-mini" onclick="event.stopPropagation(); quickAdd('Wings Fahem (6 pcs)', 1163500, '$13.00', '../assets/wings-garlic-sauce.jpg')">+</button>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 02: BROASTED -->
    <section id="sec-c-broasted" class="c-section">
      <div class="c-section-head">
        <div>
          <span class="c-section-num">DIVISION // 02</span>
          <h2 class="c-section-title">GOLDEN BROASTED CRISP</h2>
        </div>
        <div style="font-size:13px; color:var(--c-gray-mid);">18-spice pressure-fried heritage poultry</div>
      </div>

      <article class="c-burst-dish" onclick="openDetail('full-broasted', 'Full Broasted Chicken', 'فروج بروستد كامل', '1,879,500 L.L.', '$21.00', 'Whole chicken cut into 8 pieces, pressure-crisped to golden perfection. Served with coleslaw, garlic toum, and fries.', '../assets/full-broasted-chicken.jpg')">
        <div class="c-burst-photo">
          <img src="../assets/full-broasted-chicken.jpg" alt="Full Broasted Chicken"/>
        </div>
        <div class="c-burst-info">
          <div>
            <div class="c-burst-tag">HERITAGE CRUST // 8 PIECES</div>
            <h3 class="c-burst-title">FULL BROASTED CRISP CHICKEN</h3>
            <p class="c-burst-desc">Pressure-fried in pure golden oil with an ultra-crisp aromatic crust. Accompanied by house coleslaw, hand-cut potatoes, and scratch garlic toum.</p>
          </div>
          <div>
            <div class="c-burst-price">1,879,500 L.L. <span style="font-size:14px; color:#666; font-weight:500;">(~$21.00 USD)</span></div>
            <button class="c-btn-burst" onclick="event.stopPropagation(); quickAdd('Full Broasted Chicken', 1879500, '$21.00', '../assets/full-broasted-chicken.jpg')">
              + ADD TO SELECTION
            </button>
          </div>
        </div>
      </article>
    </section>

    <!-- SECTION 03: MACHAWI -->
    <section id="sec-c-machawi" class="c-section">
      <div class="c-section-head">
        <div>
          <span class="c-section-num">DIVISION // 03</span>
          <h2 class="c-section-title">MACHAWI &amp; SKEWERS</h2>
        </div>
        <div style="font-size:13px; color:var(--c-gray-mid);">Tawook, Kafta, and Lamb fillet over white oak</div>
      </div>

      <article class="c-burst-dish" onclick="openDetail('mixed-grill', 'Grand Mixed Grill Platter', 'مشاوي مشكلة', '2,416,500 L.L.', '$27.00', 'Skewers of Tawook, Kafta Meshwiye, and Lahme Meshwiye with grilled onions, tomatoes, and biwaz parsley salad.', '../assets/mixed-grilled-platter.jpg')">
        <div class="c-burst-photo">
          <img src="../assets/mixed-grilled-platter.jpg" alt="Mixed Grill"/>
        </div>
        <div class="c-burst-info">
          <div>
            <div class="c-burst-tag">TRIPLE SKEWER PLATTER</div>
            <h3 class="c-burst-title">GRAND MIXED GRILL PLATTER</h3>
            <p class="c-burst-desc">A curated selection of grain-fed Tawook breast, minced spiced Kafta, and tender lamb fillet skewers, charred with sweet onions and sumac biwaz flatbread.</p>
          </div>
          <div>
            <div class="c-burst-price">2,416,500 L.L. <span style="font-size:14px; color:#666; font-weight:500;">(~$27.00 USD)</span></div>
            <button class="c-btn-burst" onclick="event.stopPropagation(); quickAdd('Grand Mixed Grill', 2416500, '$27.00', '../assets/mixed-grilled-platter.jpg')">
              + ADD TO SELECTION
            </button>
          </div>
        </div>
      </article>
    </section>

    <!-- SECTION 04: MEZZE -->
    <section id="sec-c-mezze" class="c-section">
      <div class="c-section-head">
        <div>
          <span class="c-section-num">DIVISION // 04</span>
          <h2 class="c-section-title">LEVANTINE MEZZE &amp; GREENS</h2>
        </div>
        <div style="font-size:13px; color:var(--c-gray-mid);">Stone-ground tahini and fresh garden salads</div>
      </div>

      <div class="c-row-table">
        <div class="c-row-dish" onclick="quickAdd('Hommos Bi Tahineh', 447500, '$5.00', '../assets/hommos.jpg')">
          <div class="c-row-main">
            <img src="../assets/hommos.jpg" class="c-row-thumb" alt="Hommos"/>
            <div>
              <h4 class="c-row-title">HOMMOS BI TAHINEH // حمص بطحينة</h4>
              <p class="c-row-desc">Bekaa chickpeas, stone-ground tahini, cold-pressed olive oil.</p>
            </div>
          </div>
          <div class="c-row-right">
            <span class="c-row-price">447,500 L.L.</span>
            <button class="c-btn-mini">+</button>
          </div>
        </div>

        <div class="c-row-dish" onclick="quickAdd('Fattoush Salad', 626500, '$7.00', '../assets/fattoush.jpg')">
          <div class="c-row-main">
            <img src="../assets/fattoush.jpg" class="c-row-thumb" alt="Fattoush"/>
            <div>
              <h4 class="c-row-title">FATTOUSH SALAD // فتوش</h4>
              <p class="c-row-desc">Purslane, heirloom tomatoes, sumac flatbread crisps, pomegranate molasses.</p>
            </div>
          </div>
          <div class="c-row-right">
            <span class="c-row-price">626,500 L.L.</span>
            <button class="c-btn-mini">+</button>
          </div>
        </div>

        <div class="c-row-dish" onclick="quickAdd('Hand-Cut Fries', 358000, '$4.00', '../assets/french-fries.jpg')">
          <div class="c-row-main">
            <img src="../assets/french-fries.jpg" class="c-row-thumb" alt="Fries"/>
            <div>
              <h4 class="c-row-title">HAND-CUT FRENCH FRIES // بطاطا مقلية</h4>
              <p class="c-row-desc">Crisp golden mountain potatoes with sea salt and garlic toum.</p>
            </div>
          </div>
          <div class="c-row-right">
            <span class="c-row-price">358,000 L.L.</span>
            <button class="c-btn-mini">+</button>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 06: HPC -->
    <section id="sec-c-hpc" class="c-section" style="border-bottom:none; margin-bottom:80px;">
      <div class="c-section-head">
        <div>
          <span class="c-section-num">DIVISION // 06</span>
          <h2 class="c-section-title">HIGH PROTEIN CLUB // THE WHOLE BIRD</h2>
        </div>
        <div style="font-size:13px; color:var(--c-gray-mid);">158g pure protein · 980 kcal · 0g sugar</div>
      </div>

      <article class="c-burst-dish" onclick="openDetail('the-whole-hpc', 'The Whole Bird (High Protein)', 'وجبة الرياضيين', '2,150,000 L.L.', '$24.00', '158g Protein · 980 kcal · 1000g lean boneless breast, steamed sweet potato, wild greens, cold toum.', '../assets/the-whole.webp')">
        <div class="c-burst-photo">
          <img src="../assets/the-whole.webp" alt="High Protein Club"/>
        </div>
        <div class="c-burst-info">
          <div>
            <div class="c-burst-tag">ATHLETE PERFORMANCE SPECIFICATION</div>
            <h3 class="c-burst-title">THE WHOLE BIRD // 158G PROTEIN</h3>
            <p class="c-burst-desc">One kilogram of pure boneless grilled chicken breast, grilled sweet potatoes, and pure lemon-herb toum. Macro-verified for performance athletes.</p>
          </div>
          <div>
            <div class="c-burst-price">2,150,000 L.L. <span style="font-size:14px; color:#666; font-weight:500;">(~$24.00 USD)</span></div>
            <button class="c-btn-burst" onclick="event.stopPropagation(); quickAdd('The Whole Bird (High Protein)', 2150000, '$24.00', '../assets/the-whole.webp')">
              + ADD TO SELECTION
            </button>
          </div>
        </div>
      </article>
    </section>
  </main>

  <!-- Floating Bottom Capsule -->
  <div class="c-float-cart-bar" id="c-floating-cart" style="display:none;">
    <div class="c-float-pill" onclick="openCart()">
      <div style="display:flex; align-items:center; gap:12px;">
        <span id="c-pill-count" style="background:#000; color:#fff; padding:3px 9px; font-weight:800; font-size:12px;">0</span>
        <span style="font-family:var(--font-display); font-size:13px; font-weight:800; text-transform:uppercase;">REVIEW SELECTION</span>
      </div>
      <div style="font-family:var(--font-display); font-size:15px; font-weight:800;" id="c-pill-total">0 L.L.</div>
    </div>
  </div>

  <!-- Cart Drawer -->
  <div class="c-drawer-backdrop" id="c-drawer" onclick="closeCart(event)">
    <div class="c-drawer-panel" onclick="event.stopPropagation()">
      <div class="c-drawer-head">
        <h3>YOUR SELECTION // MTAYLEB</h3>
        <button class="c-drawer-close" onclick="closeCart()">&times;</button>
      </div>
      <div class="c-drawer-body" id="c-cart-list"></div>
      <div class="c-drawer-foot">
        <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-family:var(--font-display); font-size:14px; font-weight:800;">
          <span>SUBTOTAL</span>
          <span id="c-subtotal">0 L.L.</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:16px; font-size:12px; color:var(--c-gray-mid);">
          <span>ESTIMATED USD</span>
          <span id="c-usd">$0.00</span>
        </div>
        <button class="c-btn-burst" style="width:100%; text-align:center; padding:16px;" onclick="openCheckout()">PROCEED TO CHECKOUT &rarr;</button>
      </div>
    </div>
  </div>

  <!-- Detail Modal -->
  <div class="c-drawer-backdrop" id="c-modal" onclick="closeDetail(event)">
    <div class="c-drawer-panel" onclick="event.stopPropagation()">
      <div class="c-drawer-head">
        <h3 id="c-m-title">CUSTOMIZE</h3>
        <button class="c-drawer-close" onclick="closeDetail()">&times;</button>
      </div>
      <div class="c-drawer-body">
        <div style="aspect-ratio:16/9; overflow:hidden; background:#111; margin-bottom:20px;">
          <img id="c-m-img" src="" style="width:100%; height:100%; object-fit:cover;" alt=""/>
        </div>
        <p id="c-m-desc" style="font-size:14px; color:var(--c-gray-light); line-height:1.6; margin-bottom:24px;"></p>

        <div class="c-field">
          <label class="c-field-label">SALAD SELECTION (INCLUDED)</label>
          <select class="c-select">
            <option>Fresh Fattoush with Sumac Crisps</option>
            <option>Traditional Parsley Tabbouleh</option>
          </select>
        </div>

        <div class="c-field">
          <label class="c-field-label">CHEF DIRECTIVE (OPTIONAL)</label>
          <input type="text" class="c-input" id="c-m-note" placeholder="e.g. Well-done charcoal char, extra toum on side..."/>
        </div>
      </div>
      <div class="c-drawer-foot">
        <div style="display:flex; justify-content:space-between; margin-bottom:16px; font-family:var(--font-display); font-size:18px; font-weight:800;">
          <span>ITEM TOTAL</span>
          <span id="c-m-price">0 L.L.</span>
        </div>
        <button class="c-btn-burst" style="width:100%; text-align:center; padding:16px;" onclick="confirmDetailAdd()">ADD TO SELECTION</button>
      </div>
    </div>
  </div>

  <!-- Checkout View -->
  <div class="c-checkout-overlay" id="c-checkout-view">
    <div class="c-container">
      <div class="c-checkout-top">
        <button class="c-btn-burst" onclick="closeCheckout()">&larr; BACK TO MENU</button>
      </div>
      <div class="c-checkout-grid">
        <div>
          <h2 style="font-family:var(--font-display); font-size:24px; font-weight:800; text-transform:uppercase; margin-bottom:24px; border-bottom:1px solid #333; padding-bottom:12px;">LOGISTICS &amp; DESTINATION</h2>

          <div class="c-field">
            <label class="c-field-label">FULFILLMENT DISCIPLINE</label>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
              <button class="c-btn-burst" style="background:#fff; color:#000;" onclick="setMode(this)">DOOR DELIVERY</button>
              <button class="c-btn-burst" style="background:#000; color:#fff;" onclick="setMode(this)">MTAYLEB PICKUP</button>
            </div>
          </div>

          <div class="c-field">
            <label class="c-field-label">GUEST FULL NAME</label>
            <input type="text" class="c-input" value="Anthony Bassil"/>
          </div>

          <div class="c-field">
            <label class="c-field-label">MOBILE TELEPHONE</label>
            <input type="tel" class="c-input" value="+961 03 482 915"/>
          </div>

          <div class="c-field">
            <label class="c-field-label">STREET &amp; BUILDING ADDRESS</label>
            <input type="text" class="c-input" value="Rabieh, Rue 14, Bâtiment Cèdres, 3e Étage"/>
          </div>

          <div class="c-field">
            <label class="c-field-label">PAYMENT METHOD</label>
            <select class="c-select">
              <option>Cash on Delivery (Lebanese Pounds)</option>
              <option>Cash on Delivery (USD)</option>
              <option>Credit Card Machine on Delivery (POS)</option>
              <option>Whish Money Transfer</option>
            </select>
          </div>
        </div>

        <div>
          <div class="c-summary-box">
            <h3 class="c-summary-title">ORDER REQUISITION SUMMARY</h3>
            <div id="c-receipt-lines"></div>
            <div style="display:flex; justify-content:space-between; padding:12px 0; border-top:1px solid #333; margin-top:16px; font-size:14px;">
              <span>Thermal Courier Dispatch</span>
              <span>150,000 L.L.</span>
            </div>
            <div style="display:flex; justify-content:space-between; padding-top:16px; border-top:2px solid #fff; font-family:var(--font-display); font-size:20px; font-weight:800; margin-top:16px;">
              <span>TOTAL</span>
              <span id="c-final-total">0 L.L.</span>
            </div>
            <button class="c-btn-burst" style="width:100%; text-align:center; padding:18px; margin-top:28px; font-size:14px;" onclick="placeOrder()">TRANSMIT ORDER TO HEARTH &rarr;</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Confirmation Screen -->
  <div class="c-drawer-backdrop" id="c-confirm-modal">
    <div style="position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); background:#111; border:1px solid #333; padding:44px 32px; text-align:center; max-width:480px; width:90%; z-index:150;">
      <div style="font-family:var(--font-display); font-size:36px; margin-bottom:12px;">✓</div>
      <h2 style="font-family:var(--font-display); font-size:20px; font-weight:800; text-transform:uppercase; margin-bottom:8px;">ORDER TRANSMITTED #DEB-9941</h2>
      <p style="font-size:13px; color:var(--c-gray-light); line-height:1.6; margin-bottom:28px;">
        Your order is roasting over oak embers at Mtayleb Kitchen. Live courier tracking is activated. Estimated arrival in 35 minutes.
      </p>
      <button class="c-btn-burst" style="width:100%; text-align:center; padding:14px;" onclick="closeConfirm()">RETURN TO DIRECTORY</button>
    </div>
  </div>

  <script>
    const RATE = 89500;
    let cCart = [];
    let cModalItem = null;

    function formatLL(val) {
      return val.toLocaleString('en-US') + ' L.L.';
    }

    function formatUSD(val) {
      return '$' + (val / RATE).toFixed(2);
    }

    function setActiveNav(el) {
      document.querySelectorAll('.c-cat-link').forEach(l => l.classList.remove('active'));
      el.classList.add('active');
    }

    function quickAdd(name, price, usd, img) {
      const exist = cCart.find(i => i.name === name);
      if (exist) {
        exist.qty += 1;
      } else {
        cCart.push({ name, price, usd, img, qty: 1, note: '' });
      }
      updateCUI();
    }

    function openDetail(id, name, ar, priceStr, usd, desc, img) {
      const numPrice = parseInt(priceStr.replace(/[^0-9]/g, ''));
      cModalItem = { id, name, ar, price: numPrice, usd, desc, img };
      document.getElementById('c-m-title').textContent = name;
      document.getElementById('c-m-desc').textContent = desc;
      document.getElementById('c-m-img').src = img;
      document.getElementById('c-m-price').textContent = formatLL(numPrice) + ' (' + usd + ')';
      document.getElementById('c-m-note').value = '';
      document.getElementById('c-modal').classList.add('active');
    }

    function closeDetail(e) {
      if (e && e.target !== e.currentTarget && !e.target.classList.contains('c-drawer-close')) return;
      document.getElementById('c-modal').classList.remove('active');
    }

    function confirmDetailAdd() {
      if (!cModalItem) return;
      const note = document.getElementById('c-m-note').value.trim();
      const exist = cCart.find(i => i.name === cModalItem.name && i.note === note);
      if (exist) {
        exist.qty += 1;
      } else {
        cCart.push({ name: cModalItem.name, price: cModalItem.price, usd: cModalItem.usd, img: cModalItem.img, qty: 1, note });
      }
      document.getElementById('c-modal').classList.remove('active');
      updateCUI();
    }

    function updateCUI() {
      const totalCount = cCart.reduce((sum, i) => sum + i.qty, 0);
      const subtotal = cCart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      document.getElementById('c-cart-count').textContent = totalCount;
      document.getElementById('c-pill-count').textContent = totalCount;
      document.getElementById('c-pill-total').textContent = formatLL(subtotal);
      document.getElementById('c-subtotal').textContent = formatLL(subtotal);
      document.getElementById('c-usd').textContent = formatUSD(subtotal);

      const bar = document.getElementById('c-floating-cart');
      bar.style.display = totalCount > 0 ? 'flex' : 'none';

      const list = document.getElementById('c-cart-list');
      if (cCart.length === 0) {
        list.innerHTML = '<div style="color:var(--c-gray-mid); text-align:center; padding:40px 0;">SELECTION IS EMPTY</div>';
      } else {
        list.innerHTML = cCart.map((item, idx) => `
          <div class="c-cart-row">
            <img src="${item.img}" class="c-cart-thumb" alt="${item.name}"/>
            <div>
              <div style="font-family:var(--font-display); font-size:13px; font-weight:700; text-transform:uppercase;">${item.name}</div>
              ${item.note ? `<div style="font-size:11px; color:var(--c-gray-mid);">Note: ${item.note}</div>` : ''}
              <div style="margin-top:4px;">
                <button onclick="changeCQty(${idx}, -1)" style="background:#222; color:#fff; border:none; padding:1px 7px; cursor:pointer;">-</button>
                <span style="padding:0 8px; font-size:12px; font-weight:700;">${item.qty}</span>
                <button onclick="changeCQty(${idx}, 1)" style="background:#222; color:#fff; border:none; padding:1px 7px; cursor:pointer;">+</button>
              </div>
            </div>
            <div style="font-family:var(--font-display); font-size:13px; font-weight:700;">
              ${formatLL(item.price * item.qty)}
            </div>
          </div>
        `).join('');
      }
    }

    function changeCQty(idx, delta) {
      cCart[idx].qty += delta;
      if (cCart[idx].qty <= 0) cCart.splice(idx, 1);
      updateCUI();
    }

    function openCart() {
      document.getElementById('c-drawer').classList.add('active');
    }

    function closeCart(e) {
      if (e && e.target !== e.currentTarget && !e.target.classList.contains('c-drawer-close')) return;
      document.getElementById('c-drawer').classList.remove('active');
    }

    function openCheckout() {
      if (cCart.length === 0) return;
      closeCart();
      const subtotal = cCart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const delivery = 150000;
      const total = subtotal + delivery;

      let html = '';
      cCart.forEach(item => {
        html += `
          <div style="display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #222; font-size:13px;">
            <span>${item.qty}x ${item.name}</span>
            <span style="font-family:var(--font-display); font-weight:700;">${formatLL(item.price * item.qty)}</span>
          </div>
        `;
      });
      document.getElementById('c-receipt-lines').innerHTML = html;
      document.getElementById('c-final-total').textContent = formatLL(total) + ' (' + formatUSD(total) + ')';
      document.getElementById('c-checkout-view').classList.add('active');
    }

    function closeCheckout() {
      document.getElementById('c-checkout-view').classList.remove('active');
    }

    function setMode(btn) {
      const parent = btn.parentElement;
      parent.querySelectorAll('button').forEach(b => {
        b.style.background = '#000';
        b.style.color = '#fff';
      });
      btn.style.background = '#fff';
      btn.style.color = '#000';
    }

    function placeOrder() {
      closeCheckout();
      document.getElementById('c-confirm-modal').classList.add('active');
      cCart = [];
      updateCUI();
    }

    function closeConfirm() {
      document.getElementById('c-confirm-modal').classList.remove('active');
    }

    // Initialize with one item
    quickAdd('Farrouj Fahem Msahab', 2058500, '$23.00', '../assets/chargrilled-boneless-chicken.jpg');
  </script>
</body>
</html>"""

with open('/root/dar-el-bek/design-preview/concept-c/index.html', 'w') as f:
    f.write(html_content)
print("Concept C index.html written successfully!")
