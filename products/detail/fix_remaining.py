#!/usr/bin/env python3
"""Fix corrupted files by creating minimal valid HTML for remaining files."""
import os, re

BASE = r"E:\项目\mining-machinery\products\detail"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    cn = len(re.findall(r'[\u4e00-\u9fff]', content))
    kb = len(content) // 1024
    print(f"OK {path.split('/')[-1]}: {kb}KB, {cn} CN chars")

# 1. screw-conveyor.html
sc = '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
sc += '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
sc += '<meta name="description" content="XingQing Machinery Screw Conveyor, GX series 6 models, screw diameter 160-500mm, capacity 3-17t/h, tubular enclosed conveying.">\n'
sc += '<title>Screw Conveyor | XingQing Machinery</title>\n'
sc += '<link rel="icon" href="../../images/favicon.svg">\n<link rel="stylesheet" href="../../css/style.css">\n'
sc += '<style>*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}:root{--bg-primary:#0d0d0d;--bg-secondary:#141414;--bg-tertiary:#1a1a1a;--text-primary:#f5f5f5;--text-secondary:#a0a0a0;--accent:#F5A623;--border:#2a2a2a;--radius:8px;--transition:.2s ease}'
sc += 'body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg-primary);color:var(--text-primary);line-height:1.6}'
sc += '.container{max-width:1200px;margin:0 auto;padding:0 24px}'
sc += '.btn{display:inline-block;padding:12px 28px;border-radius:6px;font-size:15px;font-weight:600;text-decoration:none;transition:all var(--transition);border:none;cursor:pointer}'
sc += '.btn-primary{background:var(--accent);color:#1a1a1a}.btn-primary:hover{filter:brightness(1.1)}'
sc += '.btn-outline{background:transparent;color:var(--text-primary);border:1px solid var(--border)}.btn-outline:hover{border-color:var(--accent);color:var(--accent)}'
sc += '.nav{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(13,13,13,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}'
sc += '.nav-inner{display:flex;align-items:center;justify-content:space-between;height:64px}'
sc += '.nav-logo{font-size:20px;font-weight:800;text-decoration:none;color:var(--text-primary);display:flex;align-items:center;gap:10px}'
sc += '.nav-logo img{height:36px;flex-shrink:0}'
sc += '.nav-links{display:flex;gap:28px}.nav-links a{color:var(--text-secondary);text-decoration:none;font-size:14px;font-weight:500}'
sc += '.nav-links a:hover,.nav-links a.active{color:var(--accent)}'
sc += '.nav-actions{display:flex;align-items:center;gap:14px}.nav-cta{background:var(--accent);color:#1a1a1a!important;padding:8px 18px;border-radius:6px;font-size:14px;font-weight:600;text-decoration:none}'
sc += '.nav-hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer}.nav-hamburger span{width:22px;height:2px;background:var(--text-primary);border-radius:1px}'
sc += '.breadcrumb{padding:100px 0 20px;background:var(--bg-primary)}'
sc += '.breadcrumb-nav{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-secondary)}'
sc += '.breadcrumb-nav a{color:var(--text-secondary);transition:color var(--transition)}.breadcrumb-nav a:hover{color:var(--accent)}'
sc += '.breadcrumb-nav .sep{color:var(--border);user-select:none}.breadcrumb-nav .current{color:var(--accent);font-weight:500}'
sc += '.product-header{padding:20px 0 48px;background:var(--bg-primary)}'
sc += '.product-header h1{font-size:48px;font-weight:800;letter-spacing:-0.02em;line-height:1.15}.product-header h1 .en{color:var(--accent)}'
sc += '.hero-row{display:grid;grid-template-columns:1fr 1.1fr;gap:60px;align-items:center;padding:0 0 64px;background:var(--bg-primary)}'
sc += '.hero-row-left{max-width:520px}'
sc += '.hero-row-left .series-tag{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);border:1px solid rgba(245,166,35,.35);padding:6px 14px;border-radius:4px;margin-bottom:20px}'
sc += '.hero-row-left .product-desc{font-size:17px;color:var(--text-secondary);line-height:1.7;margin-bottom:32px}'
sc += '.hero-row-left .hero-actions{display:flex;gap:14px;flex-wrap:wrap}'
sc += '.hero-row-right{display:flex;align-items:center;justify-content:center}.hero-row-right img{max-width:100%;height:auto;border-radius:12px}'
sc += '.section-title{font-size:30px;font-weight:800;color:var(--text-primary);letter-spacing:-0.01em;margin:0 0 32px;padding-left:18px;border-left:4px solid var(--accent);line-height:1.2}'
sc += '.section-title .en{display:block;font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--text-secondary);margin-top:6px}'
sc += '.detail-section{padding:56px 0;border-top:1px solid var(--border)}.overview-text{font-size:16px;line-height:1.85;color:var(--text-secondary);max-width:880px}'
sc += '.principle-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:36px}'
sc += '.principle-step{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:28px 24px;position:relative;transition:border-color var(--transition)}.principle-step:hover{border-color:var(--accent)}'
sc += '.principle-step .step-num{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;background:var(--accent);color:#1a1a1a;font-size:17px;font-weight:800;margin-bottom:16px}'
sc += '.principle-step h3{font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:10px}.principle-step p{font-size:13px;line-height:1.7;color:var(--text-secondary)}'
sc += '.principle-flow{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:24px 28px}.principle-flow .flow-label{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:12px}'
sc += '.principle-flow .flow-path{font-size:15px;color:var(--text-primary);line-height:1.8;font-weight:600}.principle-flow .flow-path .arrow{color:var(--accent);margin:0 8px}'
sc += '.table-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--border);border-radius:8px}'
sc += '.params-table{width:100%;min-width:600px;border-collapse:collapse;font-size:13px}'
sc += '.params-table thead{background:var(--bg-secondary)}.params-table th{padding:12px 10px;text-align:center;font-weight:700;font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--accent);border-bottom:1px solid var(--border);white-space:nowrap}'
sc += '.params-table td{padding:10px 10px;text-align:center;color:var(--text-secondary);border-bottom:1px solid var(--border);white-space:nowrap}'
sc += '.params-table tbody tr:nth-child(even){background:rgba(255,255,255,.015)}.params-table tbody tr:hover{background:rgba(245,166,35,.06)}'
sc += '.params-table .model-col{color:var(--text-primary);font-weight:600}.params-note{margin-top:14px;font-size:12px;color:var(--text-secondary)}'
sc += '.structure-table{width:100%;border-collapse:collapse;font-size:14px;border:1px solid var(--border);border-radius:8px;overflow:hidden}'
sc += '.structure-table thead{background:var(--bg-secondary)}.structure-table th{padding:14px 18px;text-align:left;font-weight:700;font-size:13px;letter-spacing:.05em;color:var(--accent);border-bottom:1px solid var(--border)}'
sc += '.structure-table td{padding:14px 18px;color:var(--text-secondary);border-bottom:1px solid var(--border);line-height:1.6;vertical-align:top}'
sc += '.structure-table tbody tr:nth-child(even){background:rgba(255,255,255,.015)}.structure-table .part-col{color:var(--text-primary);font-weight:700;white-space:nowrap}.structure-table .mat-col{color:var(--accent);white-space:nowrap}'
sc += '.features-grid-2col{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}'
sc += '.feature-item{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:28px 28px 28px 52px;position:relative;transition:border-color var(--transition)}.feature-item:hover{border-color:var(--accent)}'
sc += '.feature-item::before{content:"";position:absolute;left:22px;top:32px;width:14px;height:14px;background:var(--accent);transform:rotate(45deg);border-radius:2px}'
sc += '.feature-item h3{font-size:16px;font-weight:700;margin-bottom:8px;color:var(--text-primary)}.feature-item p{font-size:13px;color:var(--text-secondary);line-height:1.65}'
sc += '.app-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-bottom:36px}'
sc += '.app-card{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:28px;transition:border-color var(--transition)}.app-card:hover{border-color:var(--accent)}'
sc += '.app-card h3{font-size:17px;font-weight:700;color:var(--text-primary);margin-bottom:12px;display:flex;align-items:center;gap:10px}'
sc += '.app-card h3::before{content:"";width:8px;height:8px;background:var(--accent);transform:rotate(45deg);border-radius:1px;flex-shrink:0}'
sc += '.app-card p{font-size:14px;line-height:1.75;color:var(--text-secondary)}'
sc += '.app-tags{display:flex;flex-wrap:wrap;gap:12px}.app-tag{display:inline-block;padding:10px 22px;font-size:14px;font-weight:500;color:var(--text-secondary);background:var(--bg-secondary);border:1px solid var(--border);border-radius:6px;transition:all var(--transition)}'
sc += '.app-tag:hover{color:var(--accent);border-color:var(--accent);background:rgba(245,166,35,.06)}'
sc += '.advice-list{list-style:none;counter-reset:advice;padding:0;margin:0;display:grid;gap:16px}'
sc += '.advice-list li{counter-increment:advice;background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:22px 24px 22px 64px;position:relative;font-size:14px;line-height:1.75;color:var(--text-secondary)}'
sc += '.advice-list li::before{content:counter(advice);position:absolute;left:20px;top:22px;width:30px;height:30px;border-radius:50%;background:var(--accent);color:#1a1a1a;font-size:15px;font-weight:800;display:flex;align-items:center;justify-content:center}'
sc += '.advice-list li strong{color:var(--text-primary)}'
sc += '.detail-cta{padding:64px 0;background:var(--bg-secondary);border-top:1px solid var(--border)}'
sc += '.detail-cta-inner{display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap}.detail-cta-text{font-size:20px;font-weight:700;color:var(--text-primary)}.detail-cta-text span{color:var(--accent)}.detail-cta-btns{display:flex;gap:14px;flex-wrap:wrap}'
sc += '.footer{padding:64px 0 32px;background:var(--bg-primary);border-top:1px solid var(--border)}.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:40px}'
sc += '.footer-brand p{font-size:14px;color:var(--text-secondary);margin-top:12px;line-height:1.7}.footer-col h4{font-size:14px;font-weight:700;margin-bottom:16px;color:var(--text-primary)}'
sc += '.footer-col a{display:block;font-size:13px;color:var(--text-secondary);text-decoration:none;margin-bottom:10px;transition:color var(--transition)}.footer-col a:hover{color:var(--accent)}'
sc += '.footer-bottom{display:flex;justify-content:space-between;align-items:center;padding-top:24px;border-top:1px solid var(--border);font-size:13px;color:var(--text-secondary)}'
sc += '@media(max-width:1024px){.hero-row{grid-template-columns:1fr;gap:40px}.features-grid-2col{grid-template-columns:1fr}.principle-steps{grid-template-columns:repeat(2,1fr)}.app-cards{grid-template-columns:1fr}.product-header h1{font-size:36px}.footer-grid{grid-template-columns:1fr 1fr}}'
sc += '@media(max-width:768px){.nav-links{display:none}.nav-hamburger{display:flex}.product-header h1{font-size:28px}.section-title{font-size:24px}.principle-steps{grid-template-columns:1fr}.detail-cta-inner{flex-direction:column;text-align:center}}'
sc += '</style></head><body>'
sc += '<nav class="nav"><div class="container nav-inner"><a href="../../index.html" class="nav-logo"><img src="../../images/logo-color.png" alt="XingQing Machinery" height="36"> XingQing Machinery</a><div class="nav-links"><a href="../../index.html">Home</a><a href="../" class="active">Products</a><a href="../../about/">About</a><a href="../../projects/">Projects</a><a href="../../news/">News</a><a href="../../contact/">Contact Us</a></div><div class="nav-actions"><a href="../../contact/" class="nav-cta">Get a Quote</a></div></div></nav>'
sc += '<section class="breadcrumb"><div class="container"><nav class="breadcrumb-nav"><a href="../../index.html">Home</a><span class="sep">/</span><a href="../">Products</a><span class="sep">/</span><a href="../feeding.html">Feeding &amp; Conveying</a><span class="sep">/</span><span class="current">Screw Conveyor</span></nav></div></section>'
sc += '<section class="product-header"><div class="container"><h1><span class="en">Screw Conveyor</span></h1></div></section>'
sc += '<section class="hero-row container"><div class="hero-row-left"><div class="series-tag">GX Series &middot; 6 Models &middot; Screw Dia. 160-500mm &middot; Horizontal/Inclined Enclosed Conveying</div>'
sc += '<p class="product-desc">The Screw Conveyor is a continuous conveying equipment that uses a rotating screw blade to push materials along an enclosed trough. The motor drives the screw shaft through a gearbox. As the screw blade rotates at a fixed pitch, the material does not rotate with the blade due to its own weight and trough friction, but is pushed forward axially. The GX series is a tubular screw conveyor with seamless steel tube housing and continuous screw blade. 6 models (GX160-GX500), screw diameter 160-500mm, capacity 3-17 t/h, for horizontal, inclined or vertical installation. Widely used for enclosed conveying of powder, granular and small lump materials in mining, metallurgy, building materials, chemical and grain industries.</p>'
sc += '<div class="hero-actions"><a href="../../contact/" class="btn btn-primary">Get a Quote</a><a href="#" class="btn btn-outline">Download Brochure</a></div></div>'
sc += '<div class="hero-row-right"><img src="../images/螺旋输送机.jpg" alt="Screw Conveyor"></div></section>'
sc += '</body></html>'
write_file(f"{BASE}/screw-conveyor.html", sc)

# 2. shredder.html
sd = sc.replace('Screw Conveyor', 'Shredder').replace('GX Series', '600-2500 Series')
sd = sd.replace('6 Models', '8 Models')
sd = sd.replace('Screw Dia.', 'Blade Dia.')
sd = sd.replace('160-500mm', '200-600mm')
sd = sd.replace('3-17 t/h', 'Various capacities')
sd = sd.replace('Horizontal/Inclined Enclosed Conveying', 'Dual-shaft Shearing &middot; Solid Waste Volume Reduction')
sd = sd.replace('<title>Screw Conveyor | XingQing Machinery</title>', '<title>Shredder | XingQing Machinery</title>')
sd = sd.replace('<meta name="description" content="XingQing Machinery Screw Conveyor, GX series 6 models, screw diameter 160-500mm, capacity 3-17t/h, tubular enclosed conveying.">',
               '<meta name="description" content="XingQing Machinery Shredder - 600-2500 series 8 models, dual-shaft shearing design, blade diameter 200-600mm for waste plastic, rubber, scrap metal, wood, straw recycling.">')
sd = sd.replace('<a href="../feeding.html">Feeding &amp; Conveying</a>', '<a href="../crushing.html">Crushing Equipment</a>')
sd = sd.replace('The Screw Conveyor is a continuous conveying equipment that uses a rotating screw blade to push materials along an enclosed trough. The motor drives the screw shaft through a gearbox. As the screw blade rotates at a fixed pitch, the material does not rotate with the blade due to its own weight and trough friction, but is pushed forward axially. The GX series is a tubular screw conveyor with seamless steel tube housing and continuous screw blade. 6 models (GX160-GX500), screw diameter 160-500mm, capacity 3-17 t/h, for horizontal, inclined or vertical installation. Widely used for enclosed conveying of powder, granular and small lump materials in mining, metallurgy, building materials, chemical and grain industries.',
               'The Shredder is a shear-type shredder using dual-shaft counter-rotating design. Blades cut, tear and squeeze to reduce material size. Made of high-strength alloy steel with heat treatment for toughness. 8 models (600-2500), blade diameter 200-600mm, suitable for volume reduction of waste plastic, rubber, scrap metal, wood, straw and other bulky solid waste.')
sd = sd.replace('../images/螺旋输送机.jpg', '../images/撕碎机_compressed.jpg')
sd = sd.replace('alt="Screw Conveyor"', 'alt="Shredder"')
write_file(f"{BASE}/shredder.html", sd)

# Note: vertical-shaft, wet-pan-mill, jig-machine, filter-press need more complete restoration
# But they are either partially written or empty. Let me note the state.
for f in ["vertical-shaft-cnc-sand-maker/index.html", "wet-pan-mill/index.html", "jig-machine.html", "filter-press.html"]:
    path = f"{BASE}/{f}"
    sz = os.path.getsize(path) if os.path.exists(path) else 0
    print(f"PARTIAL: {f}: {sz} bytes")
