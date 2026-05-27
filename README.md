### workforce-dynamics-bi-pipeline

# Workforce Dynamics & BI Analytics Lifecycle Pipeline

An end-to-end business intelligence lifecycle demonstration engineering a programmatic workforce dataset into a production-ready, interactive analytics dashboard. This project implements a modular **Star Schema (Medallion-inspired)** database architecture, custom business logic logic-engines, and data-observability quality gates.

---

## System Architecture & Data Flow

1. **Bronze Layer (Raw Storage):** Programmatic ingestion of 250 human resource profiles saved as an immutable flat storage CSV asset (`bronze_workforce_raw.csv`).
2. **Silver Layer (Relational Schema):** Utilizing **DuckDB** inside an in-memory execution kernel to normalize the data into an optimized **Star Schema**:
   * `dim_employee`: Unique structural dimension profiles (Primary Key: `Employee_ID`).
   * `fact_payroll_satisfaction`: Quantitative transactional records (Foreign Key: `Employee_ID`).
3. **Gold Layer (Business Aggregates):** Execution of a business transformation engine calculating key metrics (**Compa-Ratio**, **Retention Risk Flags**) passing through a structural **Data Quality Gate**.
4. **Presentation Layer (BI App):** A responsive, state-managed **Streamlit Application** enabling executive stakeholders to perform live department filter roll-ups.

---

## Core Business Metric Definitions

* **Compa-Ratio:** Calculated as $\frac{\text{Actual Monthly Salary}}{\text{Market Midpoint Salary}}$ to isolate compensation equity gaps.
* **Retention Risk Score:** A conditional logic matrix flagging personnel as **High Risk** if they are simultaneously underpaid ($\text{Compa-Ratio} < 0.85$) and experiencing low job alignment ($\text{Job Satisfaction} \le 2$).

---

##  Tech Stack & Tooling

* **Language:** Python 3.10+
* **Data Manipulation:** Pandas, NumPy Arrays (Vectorized computing blocks)
* **SQL Engine:** DuckDB (Embedded OLAP engine for speed and memory efficiency)
* **Dashboarding UI:** Streamlit Web Framework

---

## How to Run the Application Local Deployment

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME