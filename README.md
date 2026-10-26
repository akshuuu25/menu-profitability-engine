# 🍔 QSR Menu Profitability & Strategic Pricing Engine

An end-to-end data analytics project combining operational experience as an Assistant Restaurant Manager at **Hungry Jack's** with **Python and Tableau** to solve a critical profitability challenge: *Which menu items drive actual gross profit, and how should prices be optimized for next year to combat food cost inflation without sacrificing sales volume?*

---

## 🎯 Executive Summary & Business Problem
In fast-food Quick Service Restaurants (QSRs), high-volume top-sellers (such as standard burgers or fries) can suffer from thin contribution margins due to raw ingredient costs. Conversely, specialty items or premium meals might carry high margins but lower sales velocity. 

This project simulates 1 year of POS and COGS (Cost of Goods Sold) data to categorize items using a **Boston Consulting Group (BCG) Menu Engineering Matrix** (Stars, Plowhorses, Puzzles, Dogs) and formulates data-driven, inflation-adjusted pricing recommendations for next year.

---

## 📊 Key Business Findings & Insights
* **The "Plowhorse" Dilemma:** High-volume items like *Large Fries* and *Soft Drinks* drive transaction volume, but their low contribution margins require strict portion control and recipe cost monitoring.
* **Star Performers:** Core meals (Whoppers and Cheeseburgers) represent the engine of profitability, justifying a calculated **5% price adjustment** safely within customer demand elasticity.
* **Projected Impact:** Implementing these targeted price recommendations yields an estimated **$142,000+ in annual gross profit growth** across simulated store volume.

---

## 🛠 Tech Stack & Architecture
* **Python (Pandas, NumPy):** Automated data simulation, financial metric calculations, BCG matrix classification algorithms, and pricing modeling.
* **Tableau Public:** Executive dashboard design featuring KPI metric cards with custom left-border accents, a 4-quadrant BCG scatter plot, and a dynamic pricing recommendation table.
* **Git & GitHub:** Version control and portfolio documentation.

---

## 📈 Dashboard Preview & Layout
The interactive Tableau dashboard is organized into three executive views:
1. **Top KPI Banner:** High-level metrics tracking Total Revenue, Gross Profit, Average Food Cost %, and Projected Next Year Profit Gain.
2. **Menu Engineering Matrix (Scatter Plot):** Plots Annual Units Sold against Total Gross Profit, automatically segmented into 4 colored quadrants.
3. **Strategic Pricing Table:** Item-by-item breakdown detailing current prices, unit costs, food cost percentages, and recommended next-year pricing.