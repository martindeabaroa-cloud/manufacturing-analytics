"""Generates the fictional dataset used in this project.

All data is synthetic. It mimics the structure of a real small furniture
manufacturer (melamine and sheet-metal furniture) without exposing any real
company information.
"""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)

# ------------------------------------------------------------------ materials
materials = pd.DataFrame([
    # id, name, unit, unit_cost (USD), stock, min_stock, lead_time_days
    ("M01", "Melamine board 18mm (white)", "m2", 9.50, 220, 150, 7),
    ("M02", "Melamine board 18mm (oak)", "m2", 11.20, 140, 120, 7),
    ("M03", "Fiberboard back panel 3mm", "m2", 3.10, 160, 80, 7),
    ("M04", "PVC edge banding", "m", 0.35, 1500, 1200, 5),
    ("M05", "Steel square tube 20x20", "m", 2.40, 260, 200, 10),
    ("M06", "Steel sheet 0.9mm", "m2", 14.80, 25, 30, 10),
    ("M07", "Epoxy powder paint (black)", "kg", 8.90, 18, 15, 10),
    ("M08", "Drawer slide (pair)", "unit", 4.60, 90, 80, 15),
    ("M09", "Hinge 35mm", "unit", 0.85, 420, 300, 15),
    ("M10", "Handle 128mm", "unit", 1.40, 230, 150, 15),
    ("M11", "Screws and fittings kit", "kit", 1.90, 210, 150, 5),
    ("M12", "Packaging (cardboard box)", "unit", 4.20, 140, 100, 5),
    ("M13", "Adjustable leveling foot", "unit", 0.55, 400, 300, 15),
], columns=["material_id", "material", "unit", "unit_cost", "stock", "min_stock", "lead_time_days"])

# ------------------------------------------------------------------ subassemblies (made in-house)
subassemblies = pd.DataFrame([
    ("S01", "Metal frame - desk", 25),          # labor minutes
    ("S02", "Metal frame - side table", 15),
    ("S03", "Drawer box", 12),
    ("S04", "Metal shelf frame", 30),
], columns=["item_id", "item", "labor_minutes"])

# ------------------------------------------------------------------ products
products = pd.DataFrame([
    ("P01", "Office desk 120cm", "Desks", 149, 45),
    ("P02", "Industrial desk 140cm", "Desks", 199, 55),
    ("P03", "Bookshelf 5 levels", "Storage", 139, 40),
    ("P04", "Industrial metal shelf", "Storage", 159, 35),
    ("P05", "Bedside table 1 drawer", "Bedroom", 69, 30),
    ("P06", "Chest of drawers 4", "Bedroom", 179, 65),
    ("P07", "Wardrobe 2 doors", "Bedroom", 259, 80),
    ("P08", "TV stand 160cm", "Living room", 149, 45),
    ("P09", "Industrial side table", "Living room", 79, 20),
    ("P10", "Shoe cabinet 3 doors", "Storage", 119, 40),
], columns=["product_id", "product", "category", "list_price", "labor_minutes"])

# ------------------------------------------------------------------ multi-level BOM (parent -> component, qty)
bom = pd.DataFrame([
    # subassemblies
    ("S01", "M05", 7.5), ("S01", "M07", 0.35), ("S01", "M13", 4),
    ("S02", "M05", 4.0), ("S02", "M07", 0.20), ("S02", "M13", 4),
    ("S03", "M01", 0.35), ("S03", "M03", 0.18), ("S03", "M08", 1), ("S03", "M11", 0.2),
    ("S04", "M05", 9.0), ("S04", "M06", 1.6), ("S04", "M07", 0.55), ("S04", "M13", 4),
    # P01 office desk
    ("P01", "M01", 1.6), ("P01", "M04", 7), ("P01", "S03", 1), ("P01", "M10", 1),
    ("P01", "M11", 1), ("P01", "M12", 1), ("P01", "M13", 4),
    # P02 industrial desk
    ("P02", "M02", 1.2), ("P02", "M04", 5), ("P02", "S01", 1), ("P02", "M11", 1), ("P02", "M12", 1),
    # P03 bookshelf
    ("P03", "M01", 3.2), ("P03", "M03", 1.5), ("P03", "M04", 16), ("P03", "M11", 1), ("P03", "M12", 1),
    # P04 metal shelf
    ("P04", "S04", 1), ("P04", "M02", 1.0), ("P04", "M04", 6), ("P04", "M11", 1), ("P04", "M12", 1),
    # P05 bedside table
    ("P05", "M01", 1.0), ("P05", "M03", 0.25), ("P05", "M04", 6), ("P05", "S03", 1),
    ("P05", "M10", 1), ("P05", "M11", 1), ("P05", "M12", 1),
    # P06 chest of drawers
    ("P06", "M01", 2.6), ("P06", "M03", 0.7), ("P06", "M04", 14), ("P06", "S03", 4),
    ("P06", "M10", 4), ("P06", "M11", 1), ("P06", "M12", 1), ("P06", "M13", 4),
    # P07 wardrobe
    ("P07", "M01", 6.8), ("P07", "M03", 1.9), ("P07", "M04", 26), ("P07", "M09", 6),
    ("P07", "M10", 2), ("P07", "M11", 2), ("P07", "M12", 2), ("P07", "M13", 4),
    # P08 TV stand
    ("P08", "M02", 2.4), ("P08", "M03", 0.6), ("P08", "M04", 12), ("P08", "M09", 4),
    ("P08", "M10", 2), ("P08", "M11", 1), ("P08", "M12", 1),
    # P09 side table
    ("P09", "M02", 0.4), ("P09", "M04", 2.5), ("P09", "S02", 1), ("P09", "M11", 0.5), ("P09", "M12", 1),
    # P10 shoe cabinet
    ("P10", "M01", 2.3), ("P10", "M03", 0.6), ("P10", "M04", 13), ("P10", "M09", 6),
    ("P10", "M10", 3), ("P10", "M11", 1), ("P10", "M12", 1), ("P10", "M13", 4),
], columns=["parent_id", "component_id", "qty"])

# ------------------------------------------------------------------ monthly sales (units), Jan-Oct 2025
months = pd.period_range("2025-01", "2025-10", freq="M")
base = {"P01": 38, "P02": 22, "P03": 45, "P04": 18, "P05": 60,
        "P06": 20, "P07": 12, "P08": 30, "P09": 26, "P10": 24}
season = np.array([0.85, 0.80, 1.10, 1.00, 0.95, 0.90, 1.05, 1.00, 1.10, 1.20])
rows = []
for pid, b in base.items():
    for m, s in zip(months, season):
        units = max(0, int(round(rng.normal(b * s, b * 0.12))))
        rows.append((str(m), pid, units))
sales = pd.DataFrame(rows, columns=["month", "product_id", "units_sold"])

# ------------------------------------------------------------------ finished goods stock
fg_stock = pd.DataFrame({
    "product_id": list(base),
    "units_in_stock": [12, 4, 20, 2, 25, 3, 1, 10, 8, 6],
})

# overhead (rent, energy, supervision, etc.), USD per month
overhead = pd.DataFrame([("Rent", 2200), ("Energy", 900), ("Supervision & admin", 3100),
                         ("Machine maintenance", 600), ("Other", 450)],
                        columns=["concept", "usd_per_month"])

materials.to_csv(DATA / "materials.csv", index=False)
subassemblies.to_csv(DATA / "subassemblies.csv", index=False)
products.to_csv(DATA / "products.csv", index=False)
bom.to_csv(DATA / "bom.csv", index=False)
sales.to_csv(DATA / "sales.csv", index=False)
fg_stock.to_csv(DATA / "finished_goods_stock.csv", index=False)
overhead.to_csv(DATA / "overhead.csv", index=False)
print("Data generated in", DATA)
