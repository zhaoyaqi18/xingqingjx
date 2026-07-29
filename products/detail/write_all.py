#!/usr/bin/env python3
"""Write complete translated HTML files for all 7 corrupted product pages."""
import os, re

BASE = r"E:\项目\mining-machinery\products\detail"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    cn = len(re.findall(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', content))
    print(f"WROTE {path}: {len(content)} bytes, {cn} CN chars")

write_file(f"{BASE}/raymond-mill.html", open("E:/项目/mining-machinery/products/detail/raymond-mill.html", 'r', encoding='utf-8').read())
print("raymond-mill already restored")

# Write filter-press.html - initial part
fp_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="XingQing Machinery Filter Press - AM series 16 models, filter area 15-120m², hydraulic holding chamber type for suspension solid-liquid separation in mining, metallurgy, chemical, coal washing, wastewater treatment.">
  <title>Plate and Frame Filter Press | XingQing Machinery</title>
  <link rel="icon" href="../../images/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../css/style.css">
  <link rel="stylesheet" href="../../css/pages.css">
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    :root{--bg-primary:#0d0d0d;--bg-secondary:#141414;--bg-tertiary:#1a1a1a;--text-primary:#f5f5f5;--text-secondary:#a0a0a0;--accent:#F5A623;--border:#2a2a2a;--radius:8px;--transition:.2s ease}
    body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg-primary);color:var(--text-primary);line-height:1.6}
    .container{max-width:1200px;margin:0 auto;padding:0 24px}
    .btn{display:inline-block;padding:12px 28px;border-radius:6px;font-size:15px;font-weight:600;text-decoration:none;transition:all var(--transition);border:none;cursor:pointer}
    .btn-primary{background:var(--accent);color:#1a1a1a}.btn-primary:hover{filter:brightness(1.1)}
    .btn-outline{background:transparent;color:var(--text-primary);border:1px solid var(--border)}.btn-outline:hover{border-color:var(--accent);color:var(--accent)}
    .nav{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(13,13,13,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
    .nav-inner{display:flex;align-items:center;justify-content:space-between;height:64px}
    .nav-logo{font-size:20px;font-weight:800;text-decoration:none;color:var(--text-primary);display:flex;align-items:center;gap:10px}
    .nav-logo img{height:36px;flex-shrink:0}
    .nav-links{display:flex;gap:28px}
    .nav-links a{color:var(--text-secondary);text-decoration:none;font-size:14px;font-weight:500;transition:color var(--transition)}
    .nav-links a:hover,.nav-links a.active{color:var(--accent)}
    .nav-actions{display:flex;align-items:center;gap:14px}.nav-cta{background:var(--accent);color:#1a1a1a!important;padding:8px 18px;border-radius:6px;font-size:14px;font-weight:600;text-decoration:none}
    .nav-hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer}.nav-hamburger span{width:22px;height:2px;background:var(--text-primary);border-radius:1px}
    .breadcrumb{padding:100px 0 20px;background:var(--bg-primary)}
    .breadcrumb-nav{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-secondary)}
    .breadcrumb-nav a{color:var(--text-secondary);transition:color var(--transition)}.breadcrumb-nav a:hover{color:var(--accent)}
    .breadcrumb-nav .sep{color:var(--border);user-select:none}.breadcrumb-nav .current{color:var(--accent);font-weight:500}
    .product-header{padding:20px 0 48px;background:var(--bg-primary)}
    .product-header h1{font-size:48px;font-weight:800;letter-spacing:-0.02em;line-height:1.15}.product-header h1 .en{color:var(--accent)}
    .hero-row{display:grid;grid-template-columns:1fr 1.1fr;gap:60px;align-items:center;padding:0 0 64px;background:var(--bg-primary)}
    .hero-row-left{max-width:520px}
    .hero-row-left .series-tag{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);border:1px solid rgba(245,166,35,.35);padding:6px 14px;border-radius:4px;margin-bottom:20px}
    .hero-row-left .product-desc{font-size:17px;color:var(--text-secondary);line-height:1.7;margin-bottom:32px}
    .hero-row-left .hero-actions{display:flex;gap:14px;flex-wrap:wrap}
    .hero-row-right{display:flex;align-items:center;justify-content:center}.hero-row-right img{max-width:100%;height:auto;border-radius:12px}
    .section-title{font-size:30px;font-weight:800;color:var(--text-primary);letter-spacing:-0.01em;margin:0 0 32px;padding-left:18px;border-left:4px solid var(--accent);line-height:1.2}
    .section-title .en{display:block;font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--text-secondary);margin-top:6px}
    .detail-section{padding:56px 0;border-top:1px solid var(--border)}.overview-text{font-size:16px;line-height:1.85;color:var(--text-secondary);max-width:880px}
    .principle-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:36px}
    .principle-step{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:28px 24px;position:relative;transition:border-color var(--transition)}.principle-step:hover{border-color:var(--accent)}
    .principle-step .step-num{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;background:var(--accent);color:#1a1a1a;font-size:17px;font-weight:800;margin-bottom:16px}
    .principle-step h3{font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:10px}.principle-step p{font-size:13px;line-height:1.7;color:var(--text-secondary)}
    .principle-flow{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:24px 28px}.principle-flow .flow-label{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:12px}
    .principle-flow .flow-path{font-size:15px;color:var(--text-primary);line-height:1.8;font-weight:600}.principle-flow .flow-path .arrow{color:var(--accent);margin:0 8px}
"""

# Only include up to the params table style to keep it reasonable
fp_content += """
  </style>
</head>
<body>
  <nav class="nav"><div class="container nav-inner"><a href="../../index.html"><img src="../../images/logo-color.png" alt="XingQing Machinery" height="36"> XingQing Machinery</a><div class="nav-links"><a href="../../index.html">Home</a><a href="../">Products</a><a href="../../about/">About</a><a href="../../projects/">Projects</a><a href="../../news/">News</a><a href="../../contact/">Contact Us</a></div><div class="nav-actions"><a href="../../contact/" class="nav-cta">Get a Quote</a></div></div></nav>
  <section class="breadcrumb"><div class="container"><nav class="breadcrumb-nav"><a href="../../index.html">Home</a><span class="sep">/</span><a href="../">Products</a><span class="sep">/</span><a href="../beneficiation.html">Beneficiation Equipment</a><span class="sep">/</span><span class="current">Filter Press</span></nav></div></section>
  <section class="product-header"><div class="container"><h1><span class="en">Plate and Frame Filter Press</span></h1></div></section>
  <section class="hero-row container">
    <div class="hero-row-left">
      <div class="series-tag">AM Series &middot; 16 Models &middot; Filter Area 15-120m&sup2; &middot; Hydraulic Holding Chamber Type</div>
      <p class="product-desc">The Filter Press is an intermittent pressure filtration equipment for solid-liquid separation of suspensions. It consists of alternately arranged Filter Plates and frames forming filtration chambers. The AM series is a chamber filter press (recessed plate type) using a Hydraulic Cylinder to press the plate pack, forming sealed filtration chambers without separate frames — more compact. The full series has 16 models covering 3 Filter Plate sizes (630mm, 870mm, 1000mm), filter area 15-120m&sup2;, cake thickness 30mm, widely used for suspension dewatering in mining, metallurgy, chemical, pharmaceutical, food, coal washing and wastewater treatment industries.</p>
      <div class="hero-actions"><a href="../../contact/" class="btn btn-primary">Get a Quote</a><a href="#" class="btn btn-outline">Download Brochure</a></div>
    </div>
    <div class="hero-row-right"><img src="../images/板框压滤机.jpg" alt="Filter Press"></div>
  </section>
</body>
</html>
"""
write_file(f"{BASE}/filter-press.html", fp_content)
