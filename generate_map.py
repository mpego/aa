import sys
import math
import os
from PIL import Image, ImageDraw, ImageFont

def generate_tactical_map():
    # 2K Resolution Dimensions
    width, height = 2560, 1440
    print(f"Initializing image generation: {width}x{height} pixels...")

    # Create base image (RGB) with extremely deep military forest-black color
    # Deep night green: #030804
    base_color = (3, 8, 4)
    image = Image.new("RGB", (width, height), base_color)
    # Draw on a transparent layer, then composite
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    # Color Palette Definitions (RGBA)
    c_grid = (16, 185, 129, 12)       # Very faint emerald for grid
    c_grid_active = (16, 185, 129, 30) # Faint emerald for region sub-grids
    c_border = (16, 185, 129, 90)     # Emerald green for borders
    c_glow = (52, 211, 153, 140)      # Mint green for glow highlights
    c_fill_land = (12, 36, 18, 55)    # Semi-transparent dark forest land fill
    c_fill_sea = (4, 15, 8, 30)       # Deep dark sea zone fill
    c_frontline = (239, 68, 68, 160)   # High-viz red for frontlines
    c_hud = (16, 185, 129, 200)       # Solid tactical green for HUD text/borders
    c_hud_dim = (16, 185, 129, 100)   # Faint HUD elements
    c_text_bright = (240, 253, 244, 255) # Mint white for high-contrast labels
    c_amber = (245, 158, 11, 180)     # Warm amber for hazard/classified tags

    # Try loading high-quality TrueType fonts on macOS, fallback as needed
    font_paths = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Courier New.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "Arial.ttf"
    ]
    
    # Load fonts at various sizes
    f_title = None
    f_subtitle = None
    f_label = None
    f_small = None

    for path in font_paths:
        if os.path.exists(path):
            try:
                f_title = ImageFont.truetype(path, 42)
                f_subtitle = ImageFont.truetype(path, 24)
                f_label = ImageFont.truetype(path, 16)
                f_small = ImageFont.truetype(path, 12)
                print(f"Loaded font: {path}")
                break
            except Exception as e:
                continue
                
    if f_title is None:
        print("System fonts not found. Falling back to default font.")
        f_title = ImageFont.load_default()
        f_subtitle = ImageFont.load_default()
        f_label = ImageFont.load_default()
        f_small = ImageFont.load_default()

    # 1. DRAW TACTICAL GRID (Square / Hex hybrid aesthetic)
    grid_size = 80
    print("Drawing tactical coordinate grid...")
    for x in range(0, width, grid_size):
        # Vertical grid lines
        overlay_draw.line([(x, 0), (x, height)], fill=c_grid, width=1)
        # Vertical coordinates (A1, B5...)
        if x > 0 and x < width - 100 and x % 160 == 0:
            col_letter = chr(65 + (x // 160) % 26)
            overlay_draw.text((x + 8, 15), f"LON.{col_letter}0{x//10}", fill=c_hud_dim, font=f_small)

    for y in range(0, height, grid_size):
        # Horizontal grid lines
        overlay_draw.line([(0, y), (width, y)], fill=c_grid, width=1)
        # Horizontal coordinates
        if y > 0 and y < height - 100 and y % 160 == 0:
            overlay_draw.text((15, y + 8), f"LAT.0{y//10}N", fill=c_hud_dim, font=f_small)

    # 2. DRAW SHAPES FOR LAND MASSES (Territories / Sectors)
    print("Generating landmass polygons...")
    # Define coordinate sectors (polygons representing major land territories)
    sectors = {
        "WESTERN ALLIED SECTOR (AMERICA / ATLANTIC)": [
            (100, 300), (320, 250), (450, 420), (550, 500), (420, 780), 
            (250, 850), (120, 750), (80, 520)
        ],
        "EASTERN EURASIAN THEATER (URSS / COLD ZONE)": [
            (1150, 200), (1550, 150), (1850, 220), (2050, 350), (1950, 580), 
            (1700, 680), (1420, 650), (1250, 450), (1100, 320)
        ],
        "EUROPEAN COMBAT SECTOR": [
            (780, 280), (1050, 280), (1150, 420), (1120, 600), (950, 680), 
            (820, 620), (740, 450)
        ],
        "PACIFIC BASIN & ISLAND CHAIN": [
            (2100, 700), (2350, 680), (2450, 850), (2300, 1050), (2120, 1100), 
            (1950, 950), (1900, 820)
        ],
        "SOUTHERN REFINERY SECTOR (MIDDLE EAST / AFRICA)": [
            (850, 780), (1180, 720), (1350, 850), (1250, 1150), (1020, 1220), 
            (880, 1100), (820, 920)
        ]
    }

    # Draw sea backgrounds for specific coordinates
    sea_zones = [
        [(550, 200), (780, 200), (740, 600), (420, 780)], # North Atlantic
        [(1150, 650), (1420, 650), (1700, 680), (1350, 850)], # Indian Ocean
        [(100, 900), (600, 950), (800, 1300), (100, 1300)] # South Atlantic
    ]
    for zone in sea_zones:
        overlay_draw.polygon(zone, fill=c_fill_sea, outline=c_grid_active)

    # Draw land masses with glowing borders
    for name, poly in sectors.items():
        # Draw semi-transparent background fill
        overlay_draw.polygon(poly, fill=c_fill_land)
        
        # Draw multi-layered glowing border
        overlay_draw.polygon(poly, outline=c_glow, width=4)
        overlay_draw.polygon(poly, outline=c_border, width=1)
        
        # Draw a small subgrid inside the landmass to make it look high-tech
        # We can extract the bounding box
        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        
        # Draw faint internal hash lines
        for x in range(int(min_x), int(max_x), 40):
            overlay_draw.line([(x, min_y), (x, max_y)], fill=(16, 185, 129, 6), width=1)

        # Label the territory
        center_x = sum(xs) // len(poly)
        center_y = sum(ys) // len(poly)
        
        overlay_draw.text((center_x - 100, center_y - 20), name, fill=c_text_bright, font=f_subtitle)
        overlay_draw.text((center_x - 100, center_y + 10), "STATUS: SECURED // ALLIED FORCES", fill=c_hud_dim, font=f_small)

    # 3. DRAW COMBAT FRONTLINES ( glowing red dashed lines / danger zones )
    print("Drawing frontlines & supply corridors...")
    frontlines = [
        # European Front (between Europe and Eurasian Sector)
        [(740, 450), (780, 280)],
        [(1120, 600), (1250, 450)],
        # African Front
        [(820, 920), (850, 780)]
    ]
    for line in frontlines:
        # Draw glowing red thick boundary
        overlay_draw.line(line, fill=(239, 68, 68, 50), width=8)
        overlay_draw.line(line, fill=c_frontline, width=2)
        
        # Draw caution stripes or markers along the frontline
        mid_x = (line[0][0] + line[1][0]) // 2
        mid_y = (line[0][1] + line[1][1]) // 2
        overlay_draw.text((mid_x + 10, mid_y - 10), "WARNING // CONTESTED FRONTLINE", fill=(239, 68, 68, 220), font=f_small)

    # 4. DRAW NAVAL AND AIR SUPPLY ROUTES (cyan/green dotted lines)
    routes = [
        # America to Europe
        [(450, 420), (740, 450), "SEA SUPPLY LINE CORRIDOR ZETA"],
        # Africa to Europe
        [(1180, 720), (1120, 600), "OIL TRANSIT CHANNEL ALPHA"],
        # Eurasia to Pacific
        [(1950, 580), (2100, 700), "AIR CORRIDOR OMEGA"]
    ]
    for route in routes:
        line_coords = route[:2]
        name = route[2]
        
        # Draw a beautiful dotted/dashed line
        # We can interpolate points
        p1, p2 = line_coords[0], line_coords[1]
        distance = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        num_dots = int(distance / 25)
        
        for i in range(num_dots + 1):
            t = i / num_dots
            dot_x = int(p1[0] + (p2[0]-p1[0]) * t)
            dot_y = int(p1[1] + (p2[1]-p1[1]) * t)
            
            # Glow dot
            overlay_draw.ellipse([(dot_x - 6, dot_y - 6), (dot_x + 6, dot_y + 6)], fill=(16, 185, 129, 30))
            overlay_draw.ellipse([(dot_x - 2, dot_y - 2), (dot_x + 2, dot_y + 2)], fill=(52, 211, 153, 255))
            
        mid_x = (p1[0] + p2[0]) // 2
        mid_y = (p1[1] + p2[1]) // 2
        overlay_draw.text((mid_x - 80, mid_y + 12), name, fill=c_hud_dim, font=f_small)

    # 5. DRAW INFRASTRUCTURE NODES (Refineries, Silos, Industrial Complexes)
    print("Placing operational infrastructure targets...")
    nodes = [
        {"coord": (320, 250), "type": "INDUSTRY", "name": "ALLIED MANUFACTORING BASE", "oil": "+0", "ipc": "8 IPC"},
        {"coord": (420, 780), "type": "NAVAL", "name": "ATLANTIC NAVAL SHIPYARD", "oil": "+1", "ipc": "2 IPC"},
        {"coord": (1550, 150), "type": "SILO", "name": "INTERCONTINENTAL SILO SIGMA", "oil": "+0", "ipc": "3 IPC"},
        {"coord": (1700, 680), "type": "REFINERY", "name": "SIBERIAN REFINERY #4", "oil": "+3", "ipc": "4 IPC"},
        {"coord": (950, 680), "type": "REFINERY", "name": "MEDITERRANEAN DRILLING ZONE", "oil": "+2", "ipc": "2 IPC"},
        {"coord": (1020, 1220), "type": "REFINERY", "name": "SUB-SAHARAN CRUDE RIG #12", "oil": "+4", "ipc": "1 IPC"},
        {"coord": (2120, 1100), "type": "AIR", "name": "PACIFIC FORCE AIRBASE", "oil": "+0", "ipc": "3 IPC"}
    ]

    for node in nodes:
        nx, ny = node["coord"]
        ntype = node["type"]
        
        # Color based on type
        if ntype == "REFINERY":
            n_color = c_amber
            icon_char = "⌖"
        elif ntype == "SILO":
            n_color = (239, 68, 68, 250) # red
            icon_char = "▲"
        elif ntype == "INDUSTRY":
            n_color = c_hud
            icon_char = "⚙"
        else:
            n_color = (6, 182, 212, 250) # cyan
            icon_char = "⚓" if ntype == "NAVAL" else "✈"

        # Draw glowing ring
        overlay_draw.ellipse([(nx - 16, ny - 16), (nx + 16, ny + 16)], outline=n_color, width=2)
        overlay_draw.ellipse([(nx - 22, ny - 22), (nx + 22, ny + 22)], outline=(n_color[0], n_color[1], n_color[2], 60), width=1)
        overlay_draw.ellipse([(nx - 6, ny - 6), (nx + 6, ny + 6)], fill=n_color)

        # Draw tech crosshairs inside the ring
        overlay_draw.line([(nx - 30, ny), (nx - 10, ny)], fill=n_color, width=1)
        overlay_draw.line([(nx + 10, ny), (nx + 30, ny)], fill=n_color, width=1)
        overlay_draw.line([(nx, ny - 30), (nx, ny - 10)], fill=n_color, width=1)
        overlay_draw.line([(nx, ny + 10), (nx, ny + 30)], fill=n_color, width=1)

        # Label details
        overlay_draw.text((nx + 35, ny - 15), node["name"], fill=c_text_bright, font=f_label)
        overlay_draw.text((nx + 35, ny + 3), f"YIELD: {node['ipc']} | OIL: {node['oil']}", fill=n_color, font=f_small)

    # 6. DRAW MAIN HUD BORDERS AND DECALS
    print("Adding Tactical HUD HUD/Border interface...")
    # Outer frame
    pad = 40
    overlay_draw.rectangle([(pad, pad), (width - pad, height - pad)], outline=c_hud, width=2)
    # Faint outer border
    overlay_draw.rectangle([(pad - 10, pad - 10), (width - pad + 10, height - pad + 10)], outline=c_hud_dim, width=1)
    
    # Corner brackets / Crosshairs
    bracket_len = 50
    corners = [
        # Top-Left
        [(pad, pad + bracket_len), (pad, pad), (pad + bracket_len, pad)],
        # Top-Right
        [(width - pad - bracket_len, pad), (width - pad, pad), (width - pad, pad + bracket_len)],
        # Bottom-Left
        [(pad, height - pad - bracket_len), (pad, height - pad), (pad + bracket_len, height - pad)],
        # Bottom-Right
        [(width - pad - bracket_len, height - pad), (width - pad, height - pad), (width - pad, height - pad - bracket_len)]
    ]
    for b in corners:
        overlay_draw.line(b[0:2], fill=c_glow, width=5)
        overlay_draw.line(b[1:3], fill=c_glow, width=5)

    # Top HUD Strip
    overlay_draw.rectangle([(pad, pad), (width - pad, pad + 60)], fill=(12, 24, 16, 240), outline=c_hud, width=1)
    overlay_draw.text((pad + 20, pad + 10), "THEATER OF WAR // COGNITIVE COMBAT TERMINAL", fill=c_text_bright, font=f_title)
    overlay_draw.text((width - pad - 420, pad + 18), "SECURE SATELLITE CONNECTION: ACTIVE // v2.0", fill=c_hud, font=f_subtitle)

    # Bottom HUD Strip
    overlay_draw.rectangle([(pad, height - pad - 50), (width - pad, height - pad)], fill=(12, 24, 16, 240), outline=c_hud, width=1)
    overlay_draw.text((pad + 20, height - pad - 35), "CLASSIFIED INTEL - LEVEL 4 COGNITIVE DEPLOYMENT // SYSTEM STATUS: OK", fill=c_amber, font=f_label)
    overlay_draw.text((width - pad - 350, height - pad - 35), "SECTOR: GLOBAL BRIEFING MAP 2K", fill=c_hud, font=f_label)

    # 7. UNIT PROFILE / STATS CARD (Transparent legend in lower left)
    print("Generating unit profiles and rules legend card...")
    legend_x, legend_y = 100, 920
    legend_w, legend_h = 550, 420
    
    # Semi-transparent background
    overlay_draw.rectangle([(legend_x, legend_y), (legend_x + legend_w, legend_y + legend_h)], 
                           fill=(5, 12, 8, 220), outline=c_hud, width=2)
    # Card header
    overlay_draw.rectangle([(legend_x, legend_y), (legend_x + legend_w, legend_y + 40)], 
                           fill=(12, 36, 18, 240), outline=c_hud, width=1)
    overlay_draw.text((legend_x + 15, legend_y + 10), "MILITARY HARDWARE REGISTRY (V2 RULES)", fill=c_text_bright, font=f_label)
    
    # Unit stats text
    units_intel = [
        ("INFANTRY", "ATK: 1 (2 w/ Art.)", "DEF: 2", "COST: 3 IPC", "Role: Frontline Hold"),
        ("TANK", "ATK: 3", "DEF: 3", "COST: 6 IPC", "Role: Heavy Breakthrough"),
        ("FIGHTER", "ATK: 3", "DEF: 4", "COST: 10 IPC", "Role: High Mobility Air"),
        ("DESTROYER", "ATK: 2", "DEF: 2", "COST: 8 IPC", "Role: Anti-Sub / Screen"),
        ("CARRIER", "ATK: 1", "DEF: 2", "COST: 14 IPC", "Role: Air Wing Transport"),
        ("SUBMARINE", "ATK: 2", "DEF: 1", "COST: 6 IPC", "Role: Stealth Raiding")
    ]
    
    item_y = legend_y + 55
    for unit, atk, dfn, cost, role in units_intel:
        # Draw hardware symbol character
        sym = "⚔" if "Heavy" in role or "Frontline" in role else "✈" if "Air" in role else "⚓"
        overlay_draw.text((legend_x + 15, item_y), f"{sym} {unit}", fill=c_hud, font=f_label)
        
        stats_str = f"{atk}  |  {dfn}  |  {cost}"
        overlay_draw.text((legend_x + 180, item_y), stats_str, fill=c_text_bright, font=f_small)
        overlay_draw.text((legend_x + 360, item_y), role, fill=c_text_bright, font=f_small)
        
        # Bottom divider for each row
        overlay_draw.line([(legend_x + 15, item_y + 24), (legend_x + legend_w - 15, item_y + 24)], fill=(16, 185, 129, 20), width=1)
        item_y += 35

    # 8. THREE PILLARS SUMMARY CARD (Lower right)
    pillars_x, pillars_y = width - 650, 920
    pillars_w, pillars_h = 550, 420
    overlay_draw.rectangle([(pillars_x, pillars_y), (pillars_x + pillars_w, pillars_y + pillars_h)], 
                           fill=(5, 12, 8, 220), outline=c_hud, width=2)
    # Header
    overlay_draw.rectangle([(pillars_x, pillars_y), (pillars_x + pillars_w, pillars_y + 40)], 
                           fill=(12, 36, 18, 240), outline=c_hud, width=1)
    overlay_draw.text((pillars_x + 15, pillars_y + 10), "COGNITIVE SYSTEM PILLARS", fill=c_text_bright, font=f_label)

    pillars_intel = [
        ("1. THE OIL ECONOMY", "Refineries yield raw crude blocks used to fuel tanks", "and aircraft movement. No fuel means structural paralysis."),
        ("2. THE FRONTLINE SYSTEM", "No Doom Stacks allowed. Units can only move or retreat", "safely where contiguous pipelines and connectivity hold."),
        ("3. HIGH-RISK PRECISION STR STRIKES", "Deploy silos and bombers to strike deep oil refineries", "and shatter your enemy's engine of production.")
    ]

    item_y = pillars_y + 55
    for title, desc1, desc2 in pillars_intel:
        overlay_draw.text((pillars_x + 15, item_y), title, fill=c_amber, font=f_label)
        overlay_draw.text((pillars_x + 15, item_y + 22), desc1, fill=c_text_bright, font=f_small)
        overlay_draw.text((pillars_x + 15, item_y + 38), desc2, fill=c_text_bright, font=f_small)
        
        overlay_draw.line([(pillars_x + 15, item_y + 58), (pillars_x + pillars_w - 15, item_y + 58)], fill=(16, 185, 129, 20), width=1)
        item_y += 65

    # Composite layers
    final_image = Image.alpha_composite(image.convert("RGBA"), overlay)
    
    # Save image as 2K high-res PNG
    output_filename = "theater_of_war_2k_map.png"
    print(f"Saving finalized high-resolution 2K image to: {output_filename}...")
    final_image.convert("RGB").save(output_filename, "PNG", quality=100)
    print("Image generation complete. Operation successful.")

if __name__ == "__main__":
    generate_tactical_map()
