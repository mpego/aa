import math
import os
from PIL import Image, ImageDraw, ImageFont

def generate_box_cover():
    # 2K Vertical Board Game Box Resolution (2.5K vertical poster ratio: 1920x2560)
    width, height = 1920, 2560
    print(f"Initializing box cover generation: {width}x{height} pixels (Vertical 3:4 High-Res)...")

    # Base Canvas (RGB) with extremely rich tactical night-vision deep forest-black
    base_color = (2, 6, 3)
    image = Image.new("RGB", (width, height), base_color)
    
    # Overlay Layer (RGBA) for compositing glowing vectors and transparent HUDs
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Color Palette Definitions (RGBA)
    c_bg_grid = (16, 185, 129, 6)      # Extremely faint emerald for background matrix
    c_radar_grid = (16, 185, 129, 20)  # Faint emerald for radar circles
    c_radar_sweep = (52, 211, 153, 10) # Sweep beam gradient segment
    c_accent_green = (16, 185, 129, 140) # Sharp primary green
    c_glow_mint = (52, 211, 153, 180)    # High-intensity glowing mint
    c_fill_land = (12, 40, 20, 40)       # Semi-transparent dark green landmasses
    c_red_frontline = (239, 68, 68, 180) # Intense crimson for combat frontlines
    c_amber = (245, 158, 11, 200)        # Deep warning amber for classified stamps
    c_text_bright = (240, 253, 244, 255) # Minty white for crisp headers and titles
    c_text_dim = (164, 230, 192, 140)    # Soft green-gray for labels

    # Load high-quality TrueType fonts on macOS, fallback as needed
    font_paths = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Courier New.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "Arial.ttf"
    ]
    
    # Load fonts at various sizes to make a stunning typographical layout
    f_huge_title = None
    f_sub_title = None
    f_header = None
    f_body = None
    f_tiny_hud = None

    for path in font_paths:
        if os.path.exists(path):
            try:
                f_huge_title = ImageFont.truetype(path, 110) # Main Title
                f_sub_title = ImageFont.truetype(path, 42)   # Subtitle
                f_header = ImageFont.truetype(path, 28)      # Card Headers
                f_body = ImageFont.truetype(path, 20)        # Explanatory text
                f_tiny_hud = ImageFont.truetype(path, 14)    # Technical details
                print(f"Loaded font library: {path}")
                break
            except Exception as e:
                continue
                
    if f_huge_title is None:
        print("System fonts not found. Falling back to default.")
        f_huge_title = ImageFont.load_default()
        f_sub_title = ImageFont.load_default()
        f_header = ImageFont.load_default()
        f_body = ImageFont.load_default()
        f_tiny_hud = ImageFont.load_default()

    # 1. DRAW BACKGROUND HUD GRID (Faint 80px technical coordinate lines)
    print("Drawing background tactical grid...")
    grid_size = 80
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=c_bg_grid, width=1)
        if x % 240 == 0:
            draw.text((x + 6, 20), f"GRID.SYS_X0{x//10}", fill=(16, 185, 129, 30), font=f_tiny_hud)

    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=c_bg_grid, width=1)
        if y % 240 == 0:
            draw.text((20, y + 6), f"LAT_0{y//10}N", fill=(16, 185, 129, 30), font=f_tiny_hud)

    # 2. DRAW MAIN HUD OVERLAYS & CANVAS FRAME (High-tech borders)
    print("Overlaying technical frames & corner bracket designs...")
    pad = 60
    # Outer thin bounding box
    draw.rectangle([(pad, pad), (width - pad, height - pad)], outline=c_accent_green, width=2)
    # Inner margin lines
    draw.rectangle([(pad + 15, pad + 15), (width - pad - 15, height - pad - 15)], outline=(16, 185, 129, 40), width=1)
    
    # Large glowing corners
    c_len = 120
    corners = [
        # Top-Left
        [(pad, pad + c_len), (pad, pad), (pad + c_len, pad)],
        # Top-Right
        [(width - pad - c_len, pad), (width - pad, pad), (width - pad, pad + c_len)],
        # Bottom-Left
        [(pad, height - pad - c_len), (pad, height - pad), (pad + c_len, height - pad)],
        # Bottom-Right
        [(width - pad - c_len, height - pad), (width - pad, height - pad), (width - pad, height - pad - c_len)]
    ]
    for corner in corners:
        draw.line(corner[0:2], fill=c_glow_mint, width=6)
        draw.line(corner[1:3], fill=c_glow_mint, width=6)

    # 3. DRAW CENTRAL TACTICAL COGNITIVE RADAR (Concentric circular scopes)
    print("Drawing glowing central radar sweeps...")
    # Radar Center: (960, 1380) — Center of the vertical box
    cx, cy = 960, 1350
    concentric_radii = [180, 360, 540, 720, 900]
    
    # Concentric circles with technical ticks
    for r in concentric_radii:
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=c_radar_grid, width=2)
        # Add technical degree marks on outer ring
        if r == 720:
            for deg in range(0, 360, 15):
                rad = math.radians(deg)
                tx1 = cx + int(r * math.cos(rad))
                ty1 = cy + int(r * math.sin(rad))
                tx2 = cx + int((r + 15) * math.cos(rad))
                ty2 = cy + int((r + 15) * math.sin(rad))
                draw.line([(tx1, ty1), (tx2, ty2)], fill=c_accent_green, width=2)

    # Draw radar crosshairs lines stretching wide
    draw.line([(cx - 960, cy), (cx + 960, cy)], fill=(16, 185, 129, 30), width=1)
    draw.line([(cx, cy - 960), (cx, cy + 960)], fill=(16, 185, 129, 30), width=1)
    
    # Draw radar active sweeping beam
    print("Compositing sweeping radar beam vectors...")
    for angle in range(35, 75):
        rad = math.radians(angle)
        tx = cx + int(900 * math.cos(rad))
        ty = cy - int(900 * math.sin(rad))
        # Fade beam line towards the edge of sweep
        beam_alpha = int(2 + (angle - 35) * (18 / 40))
        draw.line([(cx, cy), (tx, ty)], fill=(16, 185, 129, beam_alpha), width=3)

    # 4. DRAW VECTOR CONTINENTS (Theatre map simulation)
    print("Tracing continent wireframes inside radar scope...")
    vector_continents = [
        # America Sector
        [(150, 750), (450, 680), (620, 850), (750, 1050), (580, 1350), (410, 1420), (250, 1250), (180, 950)],
        # Europe Sector
        [(750, 780), (950, 780), (1080, 950), (1020, 1150), (820, 1250), (700, 1100), (650, 900)],
        # Asia / Eurasia Sector
        [(1120, 680), (1550, 620), (1800, 750), (1880, 980), (1650, 1200), (1420, 1250), (1220, 1100), (1150, 950)],
        # Refinery Continent
        [(880, 1320), (1220, 1280), (1410, 1450), (1310, 1750), (1050, 1820), (850, 1680), (780, 1480)]
    ]
    for poly in vector_continents:
        # Draw base forest green translucent land fill
        draw.polygon(poly, fill=c_fill_land)
        # Draw high-intensity glowing boundary
        draw.polygon(poly, outline=c_glow_mint, width=5)
        draw.polygon(poly, outline=c_accent_green, width=1)
        
        # Add high-tech coordinate labels on territories
        tx = sum(p[0] for p in poly) // len(poly)
        ty = sum(p[1] for p in poly) // len(poly)
        draw.text((tx - 60, ty - 10), "ZONE SECURED", fill=c_text_dim, font=f_tiny_hud)

    # 5. DRAW WAR FRONT CRIMSON PATHS (Frontlines based on rules.md)
    print("Drawing high-risk red frontlines across theatre map...")
    crimson_frontlines = [
        # Allied/Eurasian Boundary Front
        [(620, 850), (750, 780), (700, 1100)],
        # Eurasian/Refinery Boundary Front
        [(1020, 1150), (1220, 1100), (1420, 1250)],
        # Middle East Contested Corridor
        [(1080, 950), (1150, 950)]
    ]
    for line in crimson_frontlines:
        # Thick outer warning glow
        draw.line(line, fill=(239, 68, 68, 60), width=12)
        # Sharp high-viz crimson core
        draw.line(line, fill=c_red_frontline, width=4)
        
        # Draw combat marker crosshairs at frontline centers
        mx = (line[0][0] + line[-1][0]) // 2
        my = (line[0][1] + line[-1][-1]) // 2
        draw.ellipse([(mx - 15, my - 15), (mx + 15, my + 15)], outline=(239, 68, 68, 220), width=2)
        draw.line([(mx - 25, my), (mx + 25, my)], fill=c_red_frontline, width=1)
        draw.line([(mx, my - 25), (mx, my + 25)], fill=c_red_frontline, width=1)
        draw.text((mx + 20, my - 30), "WARNING // CONTESTED", fill=(239, 68, 68, 255), font=f_tiny_hud)

    # 6. DRAW COGNITIVE INFRASTRUCTURE TARGET PINS (Silos & Refineries)
    print("Placing tactical target silos, refineries, and pipelines...")
    strategic_targets = [
        {"coord": (380, 920), "label": "ALLIED SILO SECTOR"},
        {"coord": (1480, 880), "label": "EURASIAN INDUSTRIAL CELL"},
        {"coord": (1150, 1550), "label": "SOUTHERN REFINERY #9"},
        {"coord": (820, 1020), "label": "EUROPEAN COMBAT DEPLOYMENT"}
    ]
    for target in strategic_targets:
        tx, ty = target["coord"]
        # Outer neon lock ring
        draw.ellipse([(tx - 25, ty - 25), (tx + 25, ty + 25)], outline=c_amber, width=2)
        draw.ellipse([(tx - 12, ty - 12), (tx + 12, ty + 12)], fill=c_amber)
        # Crosshair lines
        draw.line([(tx - 40, ty), (tx - 15, ty)], fill=c_amber, width=2)
        draw.line([(tx + 15, ty), (tx + 40, ty)], fill=c_amber, width=2)
        draw.line([(tx, ty - 40), (tx, ty - 15)], fill=c_amber, width=2)
        draw.line([(tx, ty + 15), (tx, ty + 40)], fill=c_amber, width=2)
        
        draw.text((tx + 45, ty - 15), target["label"], fill=c_text_bright, font=f_body)
        draw.text((tx + 45, ty + 8), "TARGET LOCKED // SAT_SECURE", fill=c_amber, font=f_tiny_hud)

    # 7. MAIN TITLES & TYPOGRAPHY BRANDING (Stunning Glowing Poster Title)
    print("Compositing main glowing titles...")
    # Background shadow/glow for title to give a neon stencil look
    title_text = "THEATER OF WAR"
    title_x = width // 2
    title_y = 380
    
    # Simulated Title Neon Glow
    glow_offsets = [(-4, -4), (4, -4), (-4, 4), (4, 4), (-2, 0), (2, 0), (0, -2), (0, 2)]
    for ox, oy in glow_offsets:
        draw.text((title_x + ox, title_y + oy), title_text, fill=(52, 211, 153, 100), font=f_huge_title, anchor="mm")
    
    # Sharp, bright white core of the title
    draw.text((title_x, title_y), title_text, fill=c_text_bright, font=f_huge_title, anchor="mm")

    # Double lined bracket border around Title
    draw.line([(width//2 - 550, title_y - 100), (width//2 + 550, title_y - 100)], fill=c_accent_green, width=3)
    draw.line([(width//2 - 550, title_y + 100), (width//2 + 550, title_y + 100)], fill=c_accent_green, width=3)
    draw.line([(width//2 - 550, title_y - 100), (width//2 - 550, title_y + 100)], fill=c_accent_green, width=6)
    draw.line([(width//2 + 550, title_y - 100), (width//2 + 550, title_y + 100)], fill=c_accent_green, width=6)

    # Subtitles and Edition Labels
    draw.text((title_x, title_y + 160), "", fill=c_amber, font=f_sub_title, anchor="mm")
    draw.text((title_x, title_y + 220), "COMMANDER'S TACTICAL EDITION // OPERATIONAL MANUAL V2.0", fill=c_text_dim, font=f_header, anchor="mm")

    # 8. THREE GAME PILLARS BOXES (At the bottom of the cover)
    print("Drawing board game cover features & pillars cards...")
    pillars_y = height - 520
    card_width = 540
    card_height = 360
    spacing = 60
    start_x = pad + 60
    
    pillars_info = [
        {"num": "I", "title": "THE OIL ECONOMY", "desc": "Refineries yield crude fuel.\nTank and aircraft engines\nrequire movement logistics.\nFuel chains dictate victory."},
        {"num": "II", "title": "FRONTLINE COMBAT", "desc": "No Doom Stacks allowed.\n5 vs 5 frontline capacity limits.\nConnected pipelines form\ncontiguous secure movement."},
        {"num": "III", "title": "PRECISION STRIKES", "desc": "Silos launch deep missiles.\nBombers devastate infrastructure.\nShatter industrial refineries.\nParalyze enemy production."}
    ]

    for i, pillar in enumerate(pillars_info):
        cx_card = start_x + i * (card_width + spacing)
        
        # Transparent card backgrounds
        draw.rectangle([(cx_card, pillars_y), (cx_card + card_width, pillars_y + card_height)], 
                       fill=(6, 18, 10, 230), outline=c_accent_green, width=2)
        # Glowing top caps
        draw.rectangle([(cx_card, pillars_y), (cx_card + card_width, pillars_y + 40)], 
                       fill=(12, 36, 18, 240), outline=c_accent_green, width=1)
        
        # Numbers & titles
        draw.text((cx_card + 20, pillars_y + 10), f"PILLAR {pillar['num']}", fill=c_amber, font=f_header)
        draw.text((cx_card + 20, pillars_y + 60), pillar["title"], fill=c_text_bright, font=f_header)
        
        # Divider line
        draw.line([(cx_card + 20, pillars_y + 100), (cx_card + card_width - 20, pillars_y + 100)], fill=c_radar_grid, width=1)
        
        # Descriptions
        draw.text((cx_card + 20, pillars_y + 120), pillar["desc"], fill=c_text_dim, font=f_body, spacing=8)

    # 9. BOTTOM HUD, INTRO COMMANDER QUOTE, BARCODE
    print("Adding board game cover HUD decals and taglines...")
    bottom_y = height - pad - 60
    
    # Bottom HUD line
    draw.line([(pad, bottom_y), (width - pad, bottom_y)], fill=c_accent_green, width=2)
    
    # Tactically themed quote
    tagline_text = '"GOOD LUCK, COMMANDER. MAY YOUR PIPELINES FLOW AND YOUR FRONTLINES HOLD."'
    draw.text((width // 2, bottom_y + 35), tagline_text, fill=c_text_bright, font=f_header, anchor="mm")
    
    # Bottom HUD Technical Indicators
    draw.text((pad + 20, bottom_y - 25), "LEVEL 4 DEPLOYMENT COGNITIVE SYSTEMS", fill=c_amber, font=f_tiny_hud)
    draw.text((width - pad - 260, bottom_y - 25), "GAME PIECES / BOARDS NOT INCLUDED", fill=c_accent_green, font=f_tiny_hud)

    # Technical Barcode in Lower Right
    barcode_x = width - pad - 120
    barcode_y = height - pad - 150
    draw.rectangle([(barcode_x, barcode_y), (barcode_x + 100, barcode_y + 65)], fill=(5, 12, 8, 220), outline=c_accent_green, width=1)
    
    # Draw simulated barcode lines
    bar_x = barcode_x + 10
    while bar_x < barcode_x + 90:
        bar_w = 2 if bar_x % 6 == 0 else 4 if bar_x % 8 == 0 else 1
        draw.line([(bar_x, barcode_y + 5), (bar_x, barcode_y + 50)], fill=c_text_bright, width=bar_w)
        bar_x += bar_w + (2 if bar_x % 3 == 0 else 1)
    draw.text((barcode_x + 10, barcode_y + 52), "3498-2512-AA", fill=c_accent_green, font=f_tiny_hud)

    # Final Composite alpha layers onto the base canvas
    final_image = Image.alpha_composite(image.convert("RGBA"), overlay)
    
    # Save the finalized premium vertical box cover PNG
    output_filename = "theater_of_war_box_cover.png"
    print(f"Saving finalized high-resolution board game box cover to: {output_filename}...")
    final_image.convert("RGB").save(output_filename, "PNG", quality=100)
    print("Cover art generation completed successfully.")

if __name__ == "__main__":
    generate_box_cover()
