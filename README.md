# Manufacturing Analytics: BOM Costing & Production Planning

Costing and production planning model for a furniture manufacturer, built with Python.

At my job in a furniture factory (melamine and sheet-metal furniture, ~30 employees) I built the company's **first costing model** and a **BOM-based production planning system**. The real data is confidential, so this repository reproduces the same approach with a **fictional dataset** of 10 products.

👉 **[Open the notebook](notebook.ipynb)**

## Business questions
1. What does each product really cost (materials + labor + overhead)?
2. Which products are underpriced, and what price would reach the target margin?
3. Based on recent sales, what do we need to produce and which materials do we need to buy?

## Approach
- **Multi-level BOM explosion:** a recursive function goes from finished product → in-house subassemblies (metal frames, drawer boxes) → raw materials.
- **Full costing:** materials + labor + overhead allocated by labor minutes.
- **Margin analysis:** margin on the net price after the e-commerce/marketplace fee, compared with a 30% target, and the price needed to reach it.
- **MRP:** 3-month sales forecast → production plan net of finished goods stock → material requirements → purchase order that keeps minimum stock, prioritized by supplier lead time.
- **Excel output** with costs, production plan and purchase order for non-technical users.

## Key findings
- **3 of 10 products are below the target margin:** Chest of drawers (5%), Bedside table (11%) and Industrial metal shelf (20%).
- **Drawers are the main cost driver:** one drawer box is 43% of the chest of drawers' cost.
- Reaching the target would require pricing the chest of drawers at **USD 243 instead of 179**, or redesigning it to cut cost.
- Next month's plan: **237 units** to produce and a **USD 9,254** purchase order, with 15-day lead time items ordered first.

## Repository structure
```
├── notebook.ipynb                     # Full analysis
├── generate_data.py                   # Generates the fictional dataset
├── data/                              # Materials, products, BOM, sales, stock, overhead
└── output/costing_and_planning.xlsx   # Results exported to Excel
```

## Tools
Python (pandas, Matplotlib), Excel (openpyxl)

## About me
Industrial Engineer (UCA Rosario, Argentina) focused on data analytics. [LinkedIn](https://www.linkedin.com/in/martin-de-abaroa-b07542374/)
