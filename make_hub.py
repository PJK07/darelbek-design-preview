import os

hub_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Dar El Bek (دار البيك) — Executive Redesign Showcase & Review Package</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --bg: #FFFFFF;
      --text: #000000;
      --muted: #666666;
      --border: #E5E5E5;
      --card-bg: #FBFBFB;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    .top-masthead {
      background: #000;
      color: #fff;
      padding: 16px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #222;
    }
    .top-brand {
      font-family: 'Playfair Display', serif;
      font-size: 20px;
      font-weight: 700;
      letter-spacing: 0.04em;
    }
    .top-tagline {
      font-size: 11px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #888;
    }
    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 48px clamp(20px, 4vw, 48px);
    }
    .hub-title {
      font-family: 'Playfair Display', serif;
      font-size: clamp(32px, 4.5vw, 52px);
      font-weight: 700;
      line-height: 1.15;
      margin-bottom: 16px;
    }
    .hub-subtitle {
      font-size: 18px;
      color: var(--muted);
      max-width: 820px;
      line-height: 1.6;
      margin-bottom: 40px;
    }

    /* Concept Selector Grid */
    .concept-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-bottom: 56px;
    }
    .c-card {
      border: 1px solid var(--border);
      padding: 32px;
      background: var(--card-bg);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      transition: all 0.2s ease;
    }
    .c-card:hover {
      border-color: #000;
      box-shadow: 0 12px 32px rgba(0,0,0,0.06);
    }
    .c-card.recommended {
      border: 2px solid #000;
      background: #FFF;
    }
    .badge-rec {
      position: absolute;
      top: -12px;
      right: 24px;
      background: #000;
      color: #fff;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      padding: 4px 12px;
    }
    .c-name {
      font-family: 'Playfair Display', serif;
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 8px;
    }
    .c-sub {
      font-size: 12px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 16px;
    }
    .c-desc {
      font-size: 14px;
      color: var(--muted);
      line-height: 1.6;
      margin-bottom: 24px;
    }
    .c-specs {
      font-size: 12px;
      border-top: 1px solid var(--border);
      padding-top: 16px;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .btn-launch {
      display: block;
      text-align: center;
      background: #000;
      color: #fff;
      text-decoration: none;
      padding: 12px 20px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      border: 1px solid #000;
      transition: all 0.15s ease;
    }
    .btn-launch:hover {
      background: #fff;
      color: #000;
    }

    /* Live Interactive Frame Previewer */
    .previewer-section {
      margin-top: 32px;
      margin-bottom: 64px;
      border: 1px solid #000;
      padding: 24px;
      background: #F9F9F9;
    }
    .previewer-controls {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }
    .control-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn-toggle {
      background: #fff;
      color: #000;
      border: 1px solid #000;
      padding: 8px 16px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      cursor: pointer;
    }
    .btn-toggle.active {
      background: #000;
      color: #fff;
    }
    .iframe-wrapper {
      display: flex;
      justify-content: center;
      background: #EFEFEF;
      padding: 20px;
      overflow-x: auto;
      border: 1px solid #DDD;
    }
    #preview-iframe {
      width: 100%;
      height: 820px;
      border: 1px solid #000;
      background: #fff;
      transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 16px 40px rgba(0,0,0,0.1);
    }

    /* Audit & Comparison Matrix */
    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: 28px;
      font-weight: 700;
      margin-top: 56px;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid #000;
    }
    .matrix-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 48px;
      font-size: 14px;
    }
    .matrix-table th, .matrix-table td {
      border: 1px solid var(--border);
      padding: 14px 18px;
      text-align: left;
    }
    .matrix-table th {
      background: #000;
      color: #fff;
      font-weight: 700;
      font-size: 12px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }
    .matrix-table tr:nth-child(even) td {
      background: #FDFDFD;
    }
    .pill-audit {
      display: inline-block;
      background: #000;
      color: #fff;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 2px 8px;
      margin-right: 6px;
    }
  </style>
</head>
<body>

  <header class="top-masthead">
    <div>
      <span class="top-brand">Dar El Bek (دار البيك)</span>
      <span class="top-tagline" style="margin-left:16px;">Comprehensive Customer UX Rethink · Phase 1 Exploration</span>
    </div>
    <div style="font-size:12px; font-weight:600; letter-spacing:0.06em;">
      STRICT BLACK &amp; WHITE DISCIPLINE · NO PRODUCTION CODE MODIFIED
    </div>
  </header>

  <main class="container">
    <h1 class="hub-title">The Three High-End Black &amp; White Directions</h1>
    <p class="hub-subtitle">
      The restaurant owner requested a complete departure from software-dashboard boxes, repetitive rounded cards, and colorful fast-food chips. Below are three genuinely distinct architectural directions, fully prototyped in standalone responsive HTML/CSS/JS.
    </p>

    <!-- 3 Cards -->
    <div class="concept-cards-grid">
      <!-- Concept A -->
      <div class="c-card recommended">
        <span class="badge-rec">Recommended</span>
        <div>
          <h2 class="c-name">Concept A: Editorial Luxury</h2>
          <div class="c-sub">"The Gastronomic Atelier"</div>
          <p class="c-desc">
            Evokes high-end culinary monographs and international gastronomic journals. High-contrast Playfair Display serif headings paired with clean Plus Jakarta Sans. Generous whitespace, asymmetric photo spreads, clean horizontal hairline rows, and dotted bistro tables for mezze.
          </p>
          <div class="c-specs">
            <div><strong>Typography:</strong> Playfair Display (Serif) + Plus Jakarta Sans</div>
            <div><strong>Layout:</strong> Asymmetric Magazine Spreads &amp; Hairline Rows</div>
            <div><strong>Interactions:</strong> Slide-over Order Drawer &amp; Bottom Capsule</div>
            <div><strong>Pacing:</strong> Gracious, contemplative, aristocratic</div>
          </div>
        </div>
        <div style="display:flex; gap:10px;">
          <button class="btn-launch" style="flex:1;" onclick="setPreview('concept-a/')">Preview Inside Hub</button>
          <a href="concept-a/" target="_blank" class="btn-launch" style="background:#fff; color:#000; flex:1;">Open Standalone &nearr;</a>
        </div>
      </div>

      <!-- Concept B -->
      <div class="c-card">
        <div>
          <h2 class="c-name">Concept B: Minimal Fine Dining</h2>
          <div class="c-sub">"Swiss Precision &amp; Haute Cuisine"</div>
          <p class="c-desc">
            Bauhaus discipline and Swiss architectural clarity. Zero border-radius (<code style="font-size:12px;">border-radius: 0px</code> across all elements). Permanent left-hand index rail on desktop, disciplined tabular matrix, monospaced category numbers, and instant hover state inversions.
          </p>
          <div class="c-specs">
            <div><strong>Typography:</strong> Inter + Space Grotesk (Tabular Figures)</div>
            <div><strong>Layout:</strong> Split Left Nav Rail + Architectural Tabular Rows</div>
            <div><strong>Geometry:</strong> 100% Sharp 0px Corners Throughout</div>
            <div><strong>Pacing:</strong> Clinical, ultra-pure, modern architectural</div>
          </div>
        </div>
        <div style="display:flex; gap:10px;">
          <button class="btn-launch" style="flex:1;" onclick="setPreview('concept-b/')">Preview Inside Hub</button>
          <a href="concept-b/" target="_blank" class="btn-launch" style="background:#fff; color:#000; flex:1;">Open Standalone &nearr;</a>
        </div>
      </div>

      <!-- Concept C -->
      <div class="c-card">
        <div>
          <h2 class="c-name">Concept C: Modern High-Contrast</h2>
          <div class="c-sub">"The Dark &amp; Stark Nocturnal Hearth"</div>
          <p class="c-desc">
            Takes direct inspiration from oak lump charcoal, white heat, and nocturnal Beirut energy. Pure pitch-black canvas interrupted by stark white bursts for signature dishes. Monumental Syne display typography and chiaroscuro food photography emerging from darkness.
          </p>
          <div class="c-specs">
            <div><strong>Typography:</strong> Syne (Monumental Extended) + Space Grotesk</div>
            <div><strong>Layout:</strong> Cinematic Midnight Canvas with White Inversion Bursts</div>
            <div><strong>Interactions:</strong> Luminous floating capsule + Dark slide-overs</div>
            <div><strong>Pacing:</strong> Theatrical, bold, nocturnal, visceral</div>
          </div>
        </div>
        <div style="display:flex; gap:10px;">
          <button class="btn-launch" style="flex:1;" onclick="setPreview('concept-c/')">Preview Inside Hub</button>
          <a href="concept-c/" target="_blank" class="btn-launch" style="background:#fff; color:#000; flex:1;">Open Standalone &nearr;</a>
        </div>
      </div>
    </div>

    <!-- Live Interactive Previewer Section -->
    <div class="previewer-section">
      <div class="previewer-controls">
        <div class="control-group">
          <span style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em;">Active Concept:</span>
          <button class="btn-toggle active" id="btn-con-a" onclick="switchConcept('concept-a/', this)">A: Editorial Luxury</button>
          <button class="btn-toggle" id="btn-con-b" onclick="switchConcept('concept-b/', this)">B: Minimal Fine Dining</button>
          <button class="btn-toggle" id="btn-con-c" onclick="switchConcept('concept-c/', this)">C: Modern High-Contrast</button>
        </div>

        <div class="control-group">
          <span style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.1em;">Viewport:</span>
          <button class="btn-toggle active" id="btn-vp-desk" onclick="setViewport('100%', this)">Desktop (100%)</button>
          <button class="btn-toggle" id="btn-vp-tab" onclick="setViewport('768px', this)">Tablet (768px)</button>
          <button class="btn-toggle" id="btn-vp-mob" onclick="setViewport('390px', this)">Mobile (390px)</button>
          <a href="concept-a/" target="_blank" id="btn-ext-link" class="btn-toggle" style="text-decoration:none;">Open Standalone Tab &nearr;</a>
        </div>
      </div>

      <div class="iframe-wrapper">
        <iframe id="preview-iframe" src="concept-a/"></iframe>
      </div>
    </div>

    <!-- Architectural Comparison Matrix -->
    <h2 class="section-title">Comparative Design Architecture Matrix</h2>
    <table class="matrix-table">
      <thead>
        <tr>
          <th>Evaluation Dimension</th>
          <th>Concept A: Editorial Luxury (Recommended)</th>
          <th>Concept B: Minimal Fine Dining</th>
          <th>Concept C: Modern High-Contrast</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Brand Feeling</strong></td>
          <td>Michelin-guide editorial journal, artisanal heritage, timeless dignity</td>
          <td>Modernist Swiss laboratory, architectural restraint, clinical precision</td>
          <td>Nocturnal Beirut luxury, embers and basalt, high-energy sizzle</td>
        </tr>
        <tr>
          <td><strong>Dominant Canvas</strong></td>
          <td>Pure White (`#FFFFFF`) with 1px Hairlines</td>
          <td>Pure White (`#FFFFFF`) with Grid Matrix</td>
          <td>Pitch Black (`#000000`) with Stark White Bursts</td>
        </tr>
        <tr>
          <td><strong>Typography System</strong></td>
          <td>Playfair Display (Serif Display) + Plus Jakarta Sans</td>
          <td>Inter + Space Grotesk (Tabular Numerals)</td>
          <td>Syne (Monumental Sans) + Space Grotesk</td>
        </tr>
        <tr>
          <td><strong>Menu Presentation</strong></td>
          <td>Alternating 16:10 feature spreads + hairline rows + dotted bistro table</td>
          <td>Disciplined architectural data rows partitioned by hairlines</td>
          <td>Chiaroscuro spotlight photography + white inversion cards</td>
        </tr>
        <tr>
          <td><strong>Desktop Experience</strong></td>
          <td>Wide-margin editorial storytelling + slide-out order drawer</td>
          <td>Sticky left navigation index rail + structured catalog table</td>
          <td>Cinematic full-bleed spreads + high-contrast split checkout</td>
        </tr>
        <tr>
          <td><strong>Mobile Experience</strong></td>
          <td>Continuous fluid stream, no cards, floating pill drawer trigger</td>
          <td>Structured tabular rows with inline micro-steppers</td>
          <td>Stark black feed, luminous bottom cart capsule</td>
        </tr>
        <tr>
          <td><strong>Why Owner Will Love It</strong></td>
          <td>Instantly looks like a luxury restaurant monograph, not a software app</td>
          <td>Fastest scanning speed and uncompromising modernist clarity</td>
          <td>Dramatically distinct from every food app in the Middle East</td>
        </tr>
      </tbody>
    </table>

    <!-- Executive UI Audit & Elimination List -->
    <h2 class="section-title">Current UI Audit: What Was Eradicated</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:24px; margin-bottom:48px;">
      <div style="border:1px solid var(--border); padding:24px; background:var(--card-bg);">
        <h3 style="font-size:15px; font-weight:700; margin-bottom:12px;"><span class="pill-audit">Removed</span> "Card Farm" Grid Syndrome</h3>
        <p style="font-size:13px; color:var(--muted); line-height:1.6;">
          Every dish previously sat in an identical rounded white rectangle with heavy drop shadows and 20px corners. Replaced with open editorial compositions and 1px hairline rules.
        </p>
      </div>

      <div style="border:1px solid var(--border); padding:24px; background:var(--card-bg);">
        <h3 style="font-size:15px; font-weight:700; margin-bottom:12px;"><span class="pill-audit">Removed</span> Rainbow Emoji Category Chips</h3>
        <p style="font-size:13px; color:var(--muted); line-height:1.6;">
          11 pastels and raw OS emojis (`🍗`, `🍟`, `🥗`, `🍤`, `🍢`) that looked like a toy store. Replaced with an understated typographic rail and subtle active indicator.
        </p>
      </div>

      <div style="border:1px solid var(--border); padding:24px; background:var(--card-bg);">
        <h3 style="font-size:15px; font-weight:700; margin-bottom:12px;"><span class="pill-audit">Removed</span> Fast-Food Red Badges &amp; Slogans</h3>
        <p style="font-size:13px; color:var(--muted); line-height:1.6;">
          Aggressive red pills, circular floating FABs, and cliche slogans ("Hungry? Let's fix that.", "🔥 Fast & Fresh") eradicated in favor of dignified provenance and craftsmanship.
        </p>
      </div>

      <div style="border:1px solid var(--border); padding:24px; background:var(--card-bg);">
        <h3 style="font-size:15px; font-weight:700; margin-bottom:12px;"><span class="pill-audit">Removed</span> Dashboard Chrome &amp; Internal Artifacts</h3>
        <p style="font-size:13px; color:var(--muted); line-height:1.6;">
          Internal staff login buttons, pulsing server status dots, and kitchen routing boxes (`#branch-auto`) purged from customer-facing navigation.
        </p>
      </div>
    </div>

    <!-- Recommendation Statement -->
    <div style="background:#000; color:#fff; padding:40px; margin-bottom:60px;">
      <span style="font-size:11px; font-weight:700; letter-spacing:0.16em; text-transform:uppercase; color:#888;">Executive Recommendation</span>
      <h3 style="font-family:'Playfair Display', serif; font-size:28px; font-weight:700; margin:12px 0 16px;">Why Concept A (Editorial Luxury) Is Recommended</h3>
      <p style="font-size:15px; line-height:1.7; color:#DDD; max-width:900px; margin-bottom:20px;">
        Concept A achieves the perfect harmony between prestigious Levantine heritage and contemporary digital hospitality. The high-contrast serif typography (*Playfair Display*) immediately conveys warmth, history, and gastronomic authority, while the card-free layout treats photography like fine art. It completely dismantles the "fast-food kiosk" feeling while remaining effortless to navigate and order on both mobile phones and desktop monitors.
      </p>
      <div style="font-size:12px; color:#888; font-family:'Space Grotesk', monospace;">
        Status: Awaiting client review and selection before production code implementation.
      </div>
    </div>
  </main>

  <script>
    let currentUrl = 'concept-a/';

    function setPreview(url) {
      currentUrl = url;
      document.getElementById('preview-iframe').src = url;
      document.getElementById('btn-ext-link').href = url;
      document.querySelector('.previewer-section').scrollIntoView({ behavior: 'smooth' });

      document.querySelectorAll('[id^=\"btn-con-\"]').forEach(b => b.classList.remove('active'));
      if (url.includes('concept-a')) document.getElementById('btn-con-a').classList.add('active');
      if (url.includes('concept-b')) document.getElementById('btn-con-b').classList.add('active');
      if (url.includes('concept-c')) document.getElementById('btn-con-c').classList.add('active');
    }

    function switchConcept(url, btn) {
      currentUrl = url;
      document.getElementById('preview-iframe').src = url;
      document.getElementById('btn-ext-link').href = url;
      document.querySelectorAll('[id^=\"btn-con-\"]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }

    function setViewport(width, btn) {
      document.getElementById('preview-iframe').style.width = width;
      document.querySelectorAll('[id^=\"btn-vp-\"]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }
  </script>
</body>
</html>"""

with open('/root/dar-el-bek/design-preview/index.html', 'w') as f:
    f.write(hub_content)
print("Master showcase hub written successfully!")
