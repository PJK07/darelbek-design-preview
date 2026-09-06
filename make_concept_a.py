import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Dar El Bek (دار البيك) — Concept A: Editorial Luxury</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>

  <!-- Top Announcement Bar -->
  <aside style="background:#000; color:#fff; text-align:center; padding:8px 16px; font-size:11px; letter-spacing:0.16em; text-transform:uppercase;">
    Dar El Bek · Design Direction A · Editorial Luxury Atelier · For Client Approval
  </aside>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="site-container">
      <div class="header-inner">
        <a href="#" class="brand-block">
          <span class="brand-title">Dar El Bek</span>
          <span class="brand-subtitle">دار البيك · Beirut Hearth</span>
        </a>
        <div class="header-actions">
          <span style="font-size:12px; color:var(--color-gray-mid); letter-spacing:0.06em;" class="hidden-mobile">Mtayleb Kitchen · Open Daily 11:30–23:00</span>
          <button class="btn-header-cart" onclick="openCartDrawer()">
            <span>Selection</span>
            <span class="cart-count-badge" id="cart-badge">0</span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Category Navigation Bar -->
  <nav class="category-nav-bar">
    <div class="site-container">
      <div class="category-nav-track">
        <a href="#chapter-grilled" class="category-nav-link active" onclick="setActiveNav(this)">01 / Charcoal Grill</a>
        <a href="#chapter-broasted" class="category-nav-link" onclick="setActiveNav(this)">02 / Golden Broasted</a>
        <a href="#chapter-machawi" class="category-nav-link" onclick="setActiveNav(this)">03 / Machawi Skewers</a>
        <a href="#chapter-mezze" class="category-nav-link" onclick="setActiveNav(this)">04 / Levantine Mezze</a>
        <a href="#chapter-sandwiches" class="category-nav-link" onclick="setActiveNav(this)">05 / Sandwiches</a>
        <a href="#chapter-hpc" class="category-nav-link" onclick="setActiveNav(this)">06 / High Protein Club</a>
      </div>
    </div>
  </nav>

  <main class="site-container">
    <!-- Hero Editorial Section -->
    <section class="hero-editorial">
      <div class="hero-grid">
        <div>
          <div class="hero-lead-kicker">Heritage Fire &amp; Craftsmanship</div>
          <h1 class="hero-heading">The Hearth of Beirut, <em>Slow-Spit Fired.</em></h1>
          <p class="hero-description">
            Farm-fresh heritage poultry marinated for twenty-four hours in mountain garlic, wild sumac, and sea salt. Roasted patiently over natural oak embers and served with scratch-whipped toum.
          </p>
          <div class="hero-meta-row">
            <div><strong>Wood:</strong> Oak &amp; Citrus Coals</div>
            <div><strong>Garlic:</strong> 100% Cold-Whipped</div>
            <div><strong>Origin:</strong> Mtayleb &amp; Beirut</div>
          </div>
        </div>
        <div class="hero-image-frame">
          <img src="../assets/chargrilled-boneless-chicken.jpg" alt="Dar El Bek Charcoal Grill" fetchpriority="high"/>
        </div>
      </div>
    </section>

    <!-- CHAPTER 01: CHARCOAL GRILL -->
    <section id="chapter-grilled" class="menu-chapter">
      <div class="chapter-header">
        <div>
          <div class="chapter-number">Collection 01</div>
          <h2 class="chapter-title">Charcoal Rotisserie &amp; Hearth</h2>
        </div>
        <p class="chapter-desc">Deboned and whole heritage birds blistered over natural wood coals, served with freshly baked bread and pure toum.</p>
      </div>

      <!-- Feature Signature Dish -->
      <article class="dish-feature" onclick="openProductDetail('farrouj-fahem-msahab', 'Farrouj Fahem Msahab', 'فروج مسحّب عالفحم', '2,058,500 L.L.', '$23.00', 'Deboned whole chicken steeped for 24 hours in mountain garlic emulsion and wild thyme, blistered slowly over glowing citrus coals. Accompanied by fresh toum, pickled turnip, and hand-stretched bread.', '../assets/chargrilled-boneless-chicken.jpg')">
        <div class="dish-feature-photo">
          <img src="../assets/chargrilled-boneless-chicken.jpg" alt="Farrouj Fahem Msahab"/>
        </div>
        <div class="dish-feature-content">
          <div>
            <div class="dish-feature-tag">Chef's Signature · Serves 2</div>
            <h3 class="dish-feature-title">Farrouj Fahem Msahab <span style="font-weight:400; font-size:0.85em; color:var(--color-gray-mid);">فروج مسحّب عالفحم</span></h3>
            <p class="dish-feature-desc">Deboned whole chicken steeped for 24 hours in mountain garlic emulsion and wild thyme, blistered slowly over glowing citrus coals. Accompanied by fresh toum, pickled turnip, and hand-stretched bread.</p>
          </div>
          <div>
            <div class="dish-price-lockup">
              <span class="price-primary">2,058,500 L.L.</span>
              <span class="price-secondary">(~$23.00 USD)</span>
            </div>
            <button class="btn-editorial-add" onclick="event.stopPropagation(); quickAdd('Farrouj Fahem Msahab', 2058500, '$23.00', '../assets/chargrilled-boneless-chicken.jpg')">
              + Add to Selection
            </button>
          </div>
        </div>
      </article>

      <!-- Standard Editorial Rows -->
      <div class="dish-row-list">
        <div class="dish-row-item" onclick="openProductDetail('farrouj-fahem', 'Farrouj Fahem (Whole)', 'فروج عالفحم', '1,745,250 L.L.', '$19.50', 'Whole bone-in chicken slow-roasted on the spit over natural oak charcoal. Served with whipped toum and pickles.', '../assets/chargrilled-chicken.jpg')">
          <div class="dish-row-info">
            <img src="../assets/chargrilled-chicken.jpg" class="dish-row-thumb" alt="Farrouj Fahem"/>
            <div>
              <h4 class="dish-row-title">Farrouj Fahem (Whole) · فروج عالفحم</h4>
              <p class="dish-row-subtext">Whole bone-in chicken slowly caramelized over natural embers. Served with whipped toum &amp; bread.</p>
            </div>
          </div>
          <div class="dish-row-pricing">
            <span class="price-primary">1,745,250 L.L.</span>
            <span class="price-secondary">$19.50</span>
            <button class="btn-row-add" onclick="event.stopPropagation(); quickAdd('Farrouj Fahem (Whole)', 1745250, '$19.50', '../assets/chargrilled-chicken.jpg')">+</button>
          </div>
        </div>

        <div class="dish-row-item" onclick="openProductDetail('half-farrouj-fahem', 'Half Farrouj Fahem', 'نصف فروج عالفحم', '1,163,500 L.L.', '$13.00', 'Half chargrilled bird with garlic paste, wild cucumber pickles, and fresh flatbread.', '../assets/chargrilled-chicken.jpg')">
          <div class="dish-row-info">
            <img src="../assets/chargrilled-chicken.jpg" class="dish-row-thumb" alt="Half Farrouj"/>
            <div>
              <h4 class="dish-row-title">Half Farrouj Fahem · نصف فروج عالفحم</h4>
              <p class="dish-row-subtext">Half chargrilled bird with garlic paste, wild cucumber pickles, and fresh flatbread.</p>
            </div>
          </div>
          <div class="dish-row-pricing">
            <span class="price-primary">1,163,500 L.L.</span>
            <span class="price-secondary">$13.00</span>
            <button class="btn-row-add" onclick="event.stopPropagation(); quickAdd('Half Farrouj Fahem', 1163500, '$13.00', '../assets/chargrilled-chicken.jpg')">+</button>
          </div>
        </div>

        <div class="dish-row-item" onclick="openProductDetail('wings-fahem', 'Wings Fahem (6 pcs)', 'جوانح عالفحم', '1,163,500 L.L.', '$13.00', 'Six crispy charred chicken wings brushed with fresh lemon-garlic emulsion.', '../assets/wings-garlic-sauce.jpg')">
          <div class="dish-row-info">
            <img src="../assets/wings-garlic-sauce.jpg" class="dish-row-thumb" alt="Wings Fahem"/>
            <div>
              <h4 class="dish-row-title">Wings Fahem (6 pieces) · جوانح عالفحم</h4>
              <p class="dish-row-subtext">Oak-charred wings basted in cold garlic emulsion, lemon juice, and mountain oregano.</p>
            </div>
          </div>
          <div class="dish-row-pricing">
            <span class="price-primary">1,163,500 L.L.</span>
            <span class="price-secondary">$13.00</span>
            <button class="btn-row-add" onclick="event.stopPropagation(); quickAdd('Wings Fahem (6 pcs)', 1163500, '$13.00', '../assets/wings-garlic-sauce.jpg')">+</button>
          </div>
        </div>
      </div>
    </section>

    <!-- CHAPTER 02: GOLDEN BROASTED -->
    <section id="chapter-broasted" class="menu-chapter">
      <div class="chapter-header">
        <div>
          <div class="chapter-number">Collection 02</div>
          <h2 class="chapter-title">Golden Broasted Poultry</h2>
        </div>
        <p class="chapter-desc">Pressure-fried heritage chicken with our proprietary eighteen-spice crust, crisp skin, and tender succulence.</p>
      </div>

      <article class="dish-feature" onclick="openProductDetail('full-broasted', 'Full Broasted Chicken', 'فروج بروستد كامل', '1,879,500 L.L.', '$21.00', 'Whole chicken cut into 8 pieces, pressure-crisped to golden perfection. Served with coleslaw, garlic toum, and fries.', '../assets/full-broasted-chicken.jpg')">
        <div class="dish-feature-photo">
          <img src="../assets/full-broasted-chicken.jpg" alt="Full Broasted Chicken"/>
        </div>
        <div class="dish-feature-content">
          <div>
            <div class="dish-feature-tag">Crisp Heritage · 8 Pieces</div>
            <h3 class="dish-feature-title">Full Broasted Chicken <span style="font-weight:400; font-size:0.85em; color:var(--color-gray-mid);">بروستد مقرمش كامل</span></h3>
            <p class="dish-feature-desc">Pressure-fried in pure golden oil with an ultra-crisp aromatic crust. Accompanied by house coleslaw, hand-cut potatoes, and scratch garlic toum.</p>
          </div>
          <div>
            <div class="dish-price-lockup">
              <span class="price-primary">1,879,500 L.L.</span>
              <span class="price-secondary">(~$21.00 USD)</span>
            </div>
            <button class="btn-editorial-add" onclick="event.stopPropagation(); quickAdd('Full Broasted Chicken', 1879500, '$21.00', '../assets/full-broasted-chicken.jpg')">
              + Add to Selection
            </button>
          </div>
        </div>
      </article>

      <div class="dish-row-list">
        <div class="dish-row-item" onclick="openProductDetail('half-broasted', 'Half Broasted Chicken', 'نصف بروستد', '1,253,000 L.L.', '$14.00', 'Four pieces of crispy broasted chicken with fries, coleslaw, and toum.', '../assets/half-broasted-chicken.jpg')">
          <div class="dish-row-info">
            <img src="../assets/half-broasted-chicken.jpg" class="dish-row-thumb" alt="Half Broasted"/>
            <div>
              <h4 class="dish-row-title">Half Broasted Chicken · نصف فروج بروستد</h4>
              <p class="dish-row-subtext">Four pieces of golden broasted chicken with hand-cut fries and fresh garlic sauce.</p>
            </div>
          </div>
          <div class="dish-row-pricing">
            <span class="price-primary">1,253,000 L.L.</span>
            <span class="price-secondary">$14.00</span>
            <button class="btn-row-add" onclick="event.stopPropagation(); quickAdd('Half Broasted Chicken', 1253000, '$14.00', '../assets/half-broasted-chicken.jpg')">+</button>
          </div>
        </div>
      </div>
    </section>

    <!-- CHAPTER 03: MACHAWI SKEWERS -->
    <section id="chapter-machawi" class="menu-chapter">
      <div class="chapter-header">
        <div>
          <div class="chapter-number">Collection 03</div>
          <h2 class="chapter-title">Machawi &amp; Artisanal Skewers</h2>
        </div>
        <p class="chapter-desc">Prime cuts grilled over white oak charcoal, scented with sumac, grilled scallions, and charred tomatoes.</p>
      </div>

      <article class="dish-feature" onclick="openProductDetail('mixed-grill-platter', 'Mixed Grilled Platter', 'مشاوي مشكلة', '2,416,500 L.L.', '$27.00', 'Skewers of Tawook, Kafta Meshwiye, and Lahme Meshwiye with grilled onions, tomatoes, and biwaz parsley salad.', '../assets/mixed-grilled-platter.jpg')">
        <div class="dish-feature-photo">
          <img src="../assets/mixed-grilled-platter.jpg" alt="Mixed Grilled Platter"/>
        </div>
        <div class="dish-feature-content">
          <div>
            <div class="dish-feature-tag">Prime Butchery · Triple Skewer</div>
            <h3 class="dish-feature-title">Grand Mixed Grill Platter <span style="font-weight:400; font-size:0.85em; color:var(--color-gray-mid);">صحن مشاوي مشكل</span></h3>
            <p class="dish-feature-desc">A curated selection of grain-fed Tawook breast, minced spiced Kafta, and tender lamb fillet skewers, charred with sweet onions and sumac biwaz flatbread.</p>
          </div>
          <div>
            <div class="dish-price-lockup">
              <span class="price-primary">2,416,500 L.L.</span>
              <span class="price-secondary">(~$27.00 USD)</span>
            </div>
            <button class="btn-editorial-add" onclick="event.stopPropagation(); quickAdd('Mixed Grilled Platter', 2416500, '$27.00', '../assets/mixed-grilled-platter.jpg')">
              + Add to Selection
            </button>
          </div>
        </div>
      </article>
    </section>

    <!-- CHAPTER 04: MEZZE & SALADS -->
    <section id="chapter-mezze" class="menu-chapter">
      <div class="chapter-header">
        <div>
          <div class="chapter-number">Collection 04</div>
          <h2 class="chapter-title">The Levantine Table (Mezze)</h2>
        </div>
        <p class="chapter-desc">Stone-ground sesame tahini, crisp Bekaa valley greens, and hand-rolled pastries.</p>
      </div>

      <!-- Bistro Dotted Table -->
      <div class="bistro-table-grid">
        <div>
          <div class="bistro-line-item" onclick="quickAdd('Hommos Bi Tahineh', 447500, '$5.00', '../assets/hommos.jpg')">
            <div>
              <span class="bistro-item-name">Hommos Bi Tahineh · حمص بطحينة</span>
              <span class="bistro-item-desc">Slow-cooked Bekaa chickpeas, stone-ground tahini, cold-pressed olive oil</span>
            </div>
            <span class="bistro-item-price">447,500 L.L.</span>
          </div>

          <div class="bistro-line-item" onclick="quickAdd('Moutabbal Eggplant', 492250, '$5.50', '../assets/moutabbal.jpg')">
            <div>
              <span class="bistro-item-name">Moutabbal · متبل باذنجان</span>
              <span class="bistro-item-desc">Charred smoky eggplant puree with virgin sesame tahini and pomegranate</span>
            </div>
            <span class="bistro-item-price">492,250 L.L.</span>
          </div>

          <div class="bistro-line-item" onclick="quickAdd('Cheese Rolls (4 pcs)', 447500, '$5.00', '../assets/cheese-rolls.jpg')">
            <div>
              <span class="bistro-item-name">Cheese Rolls · رقاقات جبنة</span>
              <span class="bistro-item-desc">Crisp hand-rolled pastry filled with melted Akawi and mint</span>
            </div>
            <span class="bistro-item-price">447,500 L.L.</span>
          </div>
        </div>

        <div>
          <div class="bistro-line-item" onclick="quickAdd('Fattoush Salad', 626500, '$7.00', '../assets/fattoush.jpg')">
            <div>
              <span class="bistro-item-name">Fattoush Salad · فتوش بالدبس</span>
              <span class="bistro-item-desc">Wild purslane, heirloom tomatoes, sumac toasted flatbread &amp; pomegranate</span>
            </div>
            <span class="bistro-item-price">626,500 L.L.</span>
          </div>

          <div class="bistro-line-item" onclick="quickAdd('Tabbouleh Large', 895000, '$10.00', '../assets/tabbouleh-large.jpg')">
            <div>
              <span class="bistro-item-name">Tabbouleh Large · تبولة خضراء</span>
              <span class="bistro-item-desc">Hand-chopped flat parsley, mint, fresh tomato, bulgur, virgin olive oil</span>
            </div>
            <span class="bistro-item-price">895,000 L.L.</span>
          </div>

          <div class="bistro-line-item" onclick="quickAdd('Hand-Cut French Fries', 358000, '$4.00', '../assets/french-fries.jpg')">
            <div>
              <span class="bistro-item-name">Hand-Cut French Fries · بطاطا مقلية</span>
              <span class="bistro-item-desc">Golden mountain batata, sea salt, served with scratch toum jar</span>
            </div>
            <span class="bistro-item-price">358,000 L.L.</span>
          </div>
        </div>
      </div>
    </section>

    <!-- CHAPTER 05: SANDWICHES -->
    <section id="chapter-sandwiches" class="menu-chapter">
      <div class="chapter-header">
        <div>
          <div class="chapter-number">Collection 05</div>
          <h2 class="chapter-title">Charcoal Wraps &amp; Sandwiches</h2>
        </div>
        <p class="chapter-desc">Rolled in fresh markouk or Arabic pita, toasted lightly over coals.</p>
      </div>

      <div class="dish-row-list">
        <div class="dish-row-item" onclick="openProductDetail('taouk-sandwich', 'Tawook Charcoal Sandwich', 'ساندويش طاووق', '537,000 L.L.', '$6.00', 'Marinated chicken breast, toum garlic paste, pickles, french fries wrapped in pita.', '../assets/taouk-sandwich.jpg')">
          <div class="dish-row-info">
            <img src="../assets/taouk-sandwich.jpg" class="dish-row-thumb" alt="Tawook Sandwich"/>
            <div>
              <h4 class="dish-row-title">Tawook Sandwich · ساندويش طاووق عالفحم</h4>
              <p class="dish-row-subtext">Tender tawook cubes, cold-whipped garlic toum, wild pickles &amp; fries.</p>
            </div>
          </div>
          <div class="dish-row-pricing">
            <span class="price-primary">537,000 L.L.</span>
            <span class="price-secondary">$6.00</span>
            <button class="btn-row-add" onclick="event.stopPropagation(); quickAdd('Tawook Charcoal Sandwich', 537000, '$6.00', '../assets/taouk-sandwich.jpg')">+</button>
          </div>
        </div>
      </div>
    </section>

    <!-- CHAPTER 06: HIGH PROTEIN CLUB -->
    <section id="chapter-hpc" class="menu-chapter" style="border-bottom:none; margin-bottom:80px;">
      <div class="chapter-header">
        <div>
          <div class="chapter-number">Collection 06</div>
          <h2 class="chapter-title">High Protein Club (Athlete Focus)</h2>
        </div>
        <p class="chapter-desc">Macro-measured lean grilled poultry plates designed for rigorous training, with up to 158g pure clean protein.</p>
      </div>

      <article class="dish-feature" onclick="openProductDetail('the-whole-hpc', 'The Whole (High Protein)', 'وجبة البروتين الكاملة', '2,150,000 L.L.', '$24.00', '158g Protein · 980 kcal · 1000g lean boneless breast, steamed sweet potato, wild greens, cold toum.', '../assets/the-whole.webp')">
        <div class="dish-feature-photo">
          <img src="../assets/the-whole.webp" alt="High Protein Club"/>
        </div>
        <div class="dish-feature-content">
          <div>
            <div class="dish-feature-tag">158g Pure Protein · 980 kcal · 0g Sugar</div>
            <h3 class="dish-feature-title">The Whole Bird / HPC Edition <span style="font-weight:400; font-size:0.85em; color:var(--color-gray-mid);">وجبة الرياضيين</span></h3>
            <p class="dish-feature-desc">One kilogram of pure boneless grilled chicken breast, grilled sweet potatoes, and pure lemon-herb toum. Macro-verified for performance athletes.</p>
          </div>
          <div>
            <div class="dish-price-lockup">
              <span class="price-primary">2,150,000 L.L.</span>
              <span class="price-secondary">(~$24.00 USD)</span>
            </div>
            <button class="btn-editorial-add" onclick="event.stopPropagation(); quickAdd('The Whole (High Protein)', 2150000, '$24.00', '../assets/the-whole.webp')">
              + Add to Selection
            </button>
          </div>
        </div>
      </article>
    </section>
  </main>

  <!-- Floating Bottom Cart Anchor -->
  <div class="floating-cart-anchor" id="floating-cart-bar" style="display:none;">
    <div class="floating-cart-pill" onclick="openCartDrawer()">
      <div style="display:flex; align-items:center; gap:12px;">
        <span class="cart-count-badge" id="pill-badge">0</span>
        <span style="font-size:13px; font-weight:600; letter-spacing:0.08em; text-transform:uppercase;">Review Selection</span>
      </div>
      <div style="display:flex; align-items:baseline; gap:8px;">
        <span style="font-weight:700; font-size:15px;" id="pill-total">0 L.L.</span>
        <span style="font-size:12px; color:var(--color-gray-mid);" id="pill-usd">($0.00)</span>
      </div>
    </div>
  </div>

  <!-- Slide-Over Cart Drawer -->
  <div class="drawer-backdrop" id="cart-drawer" onclick="closeCartDrawer(event)">
    <div class="drawer-panel" onclick="event.stopPropagation()">
      <div class="drawer-header">
        <div>
          <h3>Your Dining Selection</h3>
          <p style="font-size:12px; color:var(--color-gray-mid);">Dar El Bek · Mtayleb Kitchen</p>
        </div>
        <button class="btn-drawer-close" onclick="closeCartDrawer()">&times;</button>
      </div>

      <div class="drawer-content" id="cart-items-container">
        <!-- Injected dynamically -->
      </div>

      <div class="drawer-footer">
        <div style="display:flex; justify-content:space-between; margin-bottom:8px; font-size:14px;">
          <span>Subtotal</span>
          <strong id="cart-subtotal">0 L.L.</strong>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:16px; font-size:12px; color:var(--color-gray-mid);">
          <span>Estimated USD</span>
          <span id="cart-subtotal-usd">$0.00</span>
        </div>
        <button class="btn-primary-block" onclick="openCheckoutView()">Proceed to Checkout &rarr;</button>
      </div>
    </div>
  </div>

  <!-- Product Customization Drawer -->
  <div class="drawer-backdrop" id="product-modal" onclick="closeProductDetail(event)">
    <div class="drawer-panel" onclick="event.stopPropagation()">
      <div class="drawer-header">
        <div>
          <h3 id="modal-title">Dish Customization</h3>
          <p id="modal-ar-title" style="font-size:13px; color:var(--color-gray-mid);"></p>
        </div>
        <button class="btn-drawer-close" onclick="closeProductDetail()">&times;</button>
      </div>

      <div class="drawer-content">
        <div style="aspect-ratio:16/9; overflow:hidden; margin-bottom:16px; background:#eee;">
          <img id="modal-image" src="" alt="" style="width:100%; height:100%; object-fit:cover;"/>
        </div>
        <p id="modal-desc" style="font-size:14px; color:var(--color-gray-mid); line-height:1.5; margin-bottom:20px;"></p>

        <div class="detail-option-group">
          <div class="detail-group-title">Choice of Fresh Salad (Included)</div>
          <div class="detail-choice-card selected" onclick="selectOption(this)">
            <span>Fresh Lebanese Fattoush with Sumac Crisps</span>
            <span style="font-size:12px; color:var(--color-gray-mid);">Included</span>
          </div>
          <div class="detail-choice-card" onclick="selectOption(this)">
            <span>Traditional Parsley Tabbouleh</span>
            <span style="font-size:12px; color:var(--color-gray-mid);">Included</span>
          </div>
        </div>

        <div class="detail-option-group">
          <div class="detail-group-title">Kitchen Accompaniments (Optional)</div>
          <label class="detail-choice-card">
            <span>Extra Whipped Garlic Toum Jar (100g)</span>
            <span>+180,000 L.L. ($2.00)</span>
          </label>
          <label class="detail-choice-card">
            <span>Extra Grilled Hot Markouk Bread</span>
            <span>+90,000 L.L. ($1.00)</span>
          </label>
        </div>

        <div class="form-group">
          <label class="form-label">Preparation Notes for the Chef</label>
          <input type="text" class="form-input" id="modal-kitchen-note" placeholder="e.g. Garlic on the side, well-charred crust..."/>
        </div>
      </div>

      <div class="drawer-footer">
        <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:16px;">
          <span style="font-size:12px; text-transform:uppercase; letter-spacing:0.1em; color:var(--color-gray-mid);">Item Price</span>
          <span style="font-size:18px; font-weight:700;" id="modal-price-display">0 L.L.</span>
        </div>
        <button class="btn-primary-block" onclick="confirmAddFromModal()">Add to Selection</button>
      </div>
    </div>
  </div>

  <!-- Full Checkout View (Overlay) -->
  <div class="checkout-overlay" id="checkout-overlay">
    <div class="site-container">
      <div class="checkout-top-bar">
        <button class="btn-back-link" onclick="closeCheckoutView()">&larr; Return to Menu</button>
      </div>

      <div class="checkout-grid">
        <div>
          <h2 class="checkout-section-title">Guest Logistics &amp; Fulfillment</h2>

          <div class="segment-toggle">
            <button class="segment-btn active" onclick="setFulfillment('delivery', this)">🛵 Delivery to Door</button>
            <button class="segment-btn" onclick="setFulfillment('pickup', this)">🥡 Branch Pickup (Mtayleb)</button>
          </div>

          <div class="form-group">
            <label class="form-label">Guest Full Name</label>
            <input type="text" class="form-input" id="co-name" value="Anthony Bassil" placeholder="Full Name"/>
          </div>

          <div class="form-group">
            <label class="form-label">Mobile Telephone Number</label>
            <input type="tel" class="form-input" id="co-phone" value="+961 03 482 915" placeholder="+961 03..."/>
          </div>

          <div class="form-group">
            <label class="form-label">Delivery Destination &amp; Street</label>
            <input type="text" class="form-input" id="co-address" value="Rabieh, Street 14, Cedar Residence, 3rd Floor" placeholder="Street, Building, Floor, Apt"/>
          </div>

          <div class="form-group">
            <label class="form-label">Payment Method</label>
            <select class="form-select" id="co-payment">
              <option value="cash-ll">Cash on Delivery (Lebanese Pounds)</option>
              <option value="cash-usd">Cash on Delivery (USD Dollars)</option>
              <option value="card">Credit Card on Delivery (POS Machine)</option>
              <option value="whish">Whish Money Electronic Transfer</option>
            </select>
          </div>
        </div>

        <div>
          <div class="order-receipt-box">
            <h3 class="receipt-title">Order Summary</h3>
            <div id="checkout-receipt-lines"></div>
            <div class="receipt-line" style="margin-top:12px;">
              <span>Delivery Dispatch (Mtayleb Kitchen)</span>
              <span>150,000 L.L.</span>
            </div>
            <div class="receipt-total">
              <span>Total Payable</span>
              <span id="co-final-total">0 L.L.</span>
            </div>
            <p style="font-size:12px; color:var(--color-gray-mid); margin:12px 0 24px;">Exchange rate locked at 89,500 LL/USD. Freshly prepared upon receipt.</p>
            <button class="btn-primary-block" onclick="submitOrder()">Authorize Order &rarr;</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Order Confirmation View -->
  <div class="confirmation-view" id="confirmation-view">
    <div class="confirmation-card">
      <div class="confirmation-badge">✓</div>
      <h2 class="confirmation-title">Order Received with Pleasure.</h2>
      <div class="confirmation-order-no">Ref: #DEB-9482 · Mtayleb Charcoal Kitchen</div>
      <p style="font-size:14px; color:var(--color-gray-mid); line-height:1.6;">
        Your skewers and birds have been assigned to our hearth master. Preparation is underway with mountain oak wood.
      </p>

      <div class="confirmation-stepper">
        <div class="step-row completed">
          <span class="step-marker"></span>
          <span>12:44 PM — Order Transmitted &amp; Accepted</span>
        </div>
        <div class="step-row active">
          <span class="step-marker"></span>
          <span>Now — Slow Spit-Roasting over Oak Embers</span>
        </div>
        <div class="step-row">
          <span class="step-marker"></span>
          <span>Pending — Courier Dispatch with Thermal Packaging</span>
        </div>
        <div class="step-row">
          <span class="step-marker"></span>
          <span>Estimated Delivery: ~30–40 Minutes (Rabieh Zone)</span>
        </div>
      </div>

      <button class="btn-primary-block" onclick="closeConfirmation()">Return to Menu</button>
      <button class="btn-outline-block" onclick="alert('Connecting to Mtayleb Kitchen hotline: +961 4 928 111')">Direct Line to Kitchen (+961 4 928 111)</button>
    </div>
  </div>

  <!-- JavaScript Interaction Logic -->
  <script>
    const RATE = 89500;
    let cart = [];
    let currentModalItem = null;

    function formatLL(val) {
      return val.toLocaleString('en-US') + ' L.L.';
    }

    function formatUSD(val) {
      return '$' + (val / RATE).toFixed(2);
    }

    function setActiveNav(el) {
      document.querySelectorAll('.category-nav-link').forEach(link => link.classList.remove('active'));
      el.classList.add('active');
    }

    function quickAdd(name, price, usd, image) {
      const existing = cart.find(i => i.name === name);
      if (existing) {
        existing.qty += 1;
      } else {
        cart.push({ name, price, usd, image, qty: 1, note: '' });
      }
      updateCartUI();
      showToast('Added to selection: ' + name);
    }

    function openProductDetail(id, name, arName, priceStr, usdStr, desc, image) {
      const numericPrice = parseInt(priceStr.replace(/[^0-9]/g, ''));
      currentModalItem = { id, name, arName, price: numericPrice, usd: usdStr, desc, image };
      
      document.getElementById('modal-title').textContent = name;
      document.getElementById('modal-ar-title').textContent = arName;
      document.getElementById('modal-desc').textContent = desc;
      document.getElementById('modal-image').src = image;
      document.getElementById('modal-price-display').textContent = formatLL(numericPrice) + ' (' + usdStr + ')';
      document.getElementById('modal-kitchen-note').value = '';
      
      document.getElementById('product-modal').classList.add('active');
    }

    function closeProductDetail(e) {
      if (e && e.target !== e.currentTarget && !e.target.classList.contains('btn-drawer-close')) return;
      document.getElementById('product-modal').classList.remove('active');
    }

    function selectOption(el) {
      el.parentElement.querySelectorAll('.detail-choice-card').forEach(c => c.classList.remove('selected'));
      el.classList.add('selected');
    }

    function confirmAddFromModal() {
      if (!currentModalItem) return;
      const note = document.getElementById('modal-kitchen-note').value.trim();
      const existing = cart.find(i => i.name === currentModalItem.name && i.note === note);
      if (existing) {
        existing.qty += 1;
      } else {
        cart.push({
          name: currentModalItem.name,
          price: currentModalItem.price,
          usd: currentModalItem.usd,
          image: currentModalItem.image,
          qty: 1,
          note: note
        });
      }
      document.getElementById('product-modal').classList.remove('active');
      updateCartUI();
      showToast('Added to selection: ' + currentModalItem.name);
    }

    function updateCartUI() {
      const totalCount = cart.reduce((sum, i) => sum + i.qty, 0);
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);

      document.getElementById('cart-badge').textContent = totalCount;
      document.getElementById('pill-badge').textContent = totalCount;
      document.getElementById('pill-total').textContent = formatLL(subtotal);
      document.getElementById('pill-usd').textContent = '(' + formatUSD(subtotal) + ')';
      document.getElementById('cart-subtotal').textContent = formatLL(subtotal);
      document.getElementById('cart-subtotal-usd').textContent = formatUSD(subtotal);

      const bar = document.getElementById('floating-cart-bar');
      if (totalCount > 0) {
        bar.style.display = 'flex';
      } else {
        bar.style.display = 'none';
      }

      // Render cart items
      const container = document.getElementById('cart-items-container');
      if (cart.length === 0) {
        container.innerHTML = '<p style="color:var(--color-gray-mid); text-align:center; padding:40px 0;">Your dining selection is currently empty.</p>';
      } else {
        let html = '';
        cart.forEach((item, idx) => {
          html += '<div class="cart-item-row">' +
            '<img src="' + item.image + '" class="cart-item-thumb" alt="' + item.name + '"/>' +
            '<div>' +
              '<div class="cart-item-title">' + item.name + '</div>' +
              (item.note ? '<div class="cart-item-note">Note: ' + item.note + '</div>' : '') +
              '<div class="cart-stepper">' +
                '<button class="cart-stepper-btn" onclick="changeQty(' + idx + ', -1)">&minus;</button>' +
                '<span class="cart-stepper-val">' + item.qty + '</span>' +
                '<button class="cart-stepper-btn" onclick="changeQty(' + idx + ', 1)">&plus;</button>' +
              '</div>' +
            '</div>' +
            '<div style="text-align:right; font-weight:600; font-size:14px;">' +
              formatLL(item.price * item.qty) +
            '</div>' +
          '</div>';
        });
        container.innerHTML = html;
      }
    }

    function changeQty(idx, delta) {
      cart[idx].qty += delta;
      if (cart[idx].qty <= 0) {
        cart.splice(idx, 1);
      }
      updateCartUI();
    }

    function openCartDrawer() {
      document.getElementById('cart-drawer').classList.add('active');
    }

    function closeCartDrawer(e) {
      if (e && e.target !== e.currentTarget && !e.target.classList.contains('btn-drawer-close')) return;
      document.getElementById('cart-drawer').classList.remove('active');
    }

    function openCheckoutView() {
      if (cart.length === 0) {
        alert('Please add dishes to your selection before checking out.');
        return;
      }
      closeCartDrawer();
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const deliveryFee = 150000;
      const total = subtotal + deliveryFee;

      const linesContainer = document.getElementById('checkout-receipt-lines');
      let linesHtml = '';
      cart.forEach(item => {
        linesHtml += '<div class="receipt-line">' +
          '<span>' + item.qty + 'x ' + item.name + '</span>' +
          '<span>' + formatLL(item.price * item.qty) + '</span>' +
        '</div>';
      });
      linesContainer.innerHTML = linesHtml;

      document.getElementById('co-final-total').textContent = formatLL(total) + ' (' + formatUSD(total) + ')';
      document.getElementById('checkout-overlay').classList.add('active');
    }

    function closeCheckoutView() {
      document.getElementById('checkout-overlay').classList.remove('active');
    }

    function setFulfillment(mode, el) {
      el.parentElement.querySelectorAll('.segment-btn').forEach(b => b.classList.remove('active'));
      el.classList.add('active');
    }

    function submitOrder() {
      document.getElementById('checkout-overlay').classList.remove('active');
      document.getElementById('confirmation-view').classList.add('active');
      cart = [];
      updateCartUI();
    }

    function closeConfirmation() {
      document.getElementById('confirmation-view').classList.remove('active');
    }

    function showToast(msg) {
      const toast = document.createElement('div');
      toast.style.cssText = 'position:fixed; top:88px; right:20px; background:#000; color:#fff; padding:10px 18px; font-size:12px; letter-spacing:0.06em; text-transform:uppercase; z-index:200; box-shadow:0 8px 24px rgba(0,0,0,0.2);';
      toast.textContent = msg;
      document.body.appendChild(toast);
      setTimeout(() => toast.remove(), 2200);
    }

    // Pre-populate with one signature item for demonstration
    quickAdd('Farrouj Fahem Msahab', 2058500, '$23.00', '../assets/chargrilled-boneless-chicken.jpg');
  </script>
</body>
</html>"""

with open('/root/dar-el-bek/design-preview/concept-a/index.html', 'w') as f:
    f.write(html_content)
print("Concept A index.html written successfully!")
