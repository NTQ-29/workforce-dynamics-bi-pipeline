#state management system | pulls it in from internal memory
import streamlit as st
import pandas as pd
import numpy as np

# 1. Set up the browser page configuration
st.set_page_config(page_title="Atlas Tech Workforce Insights", layout="wide")

st.title("📊 Atlas Tech Workforce Dynamics & Attrition Dashboard")
st.markdown("---")

# 2. Emulate Data Ingestion (Using our Phase 4 Mock Generation Framework)
@st.cache_data
def load_gold_data():
    np.random.seed(42)
    num_employees = 250
    employee_ids = [f"EMP{str(i).zfill(3)}" for i in range(1, num_employees + 1)]
    departments = ['Engineering', 'Data Science', 'Human Resources', 'Sales']
    
    df = pd.DataFrame({
        'Employee_ID': employee_ids,
        'Department': np.random.choice(departments, size=num_employees, p=[0.4, 0.2, 0.1, 0.3]),
        'Job_Satisfaction': np.random.choice([1, 2, 3, 4, 5], size=num_employees, p=[0.1, 0.15, 0.25, 0.35, 0.15])
    })
    
    base_salaries = {'Engineering': 9500, 'Data Science': 10000, 'Sales': 6000, 'Human Resources': 5500}
    df['Monthly_Salary'] = [int(base_salaries[dept] + np.random.normal(0, 800)) for dept in df['Department']]
    
    market_midpoints = {'Engineering': 9500, 'Data Science': 10000, 'Sales': 6500, 'Human Resources': 5500}
    df['Market_Midpoint'] = df['Department'].map(market_midpoints)
    df['Compa_Ratio'] = round(df['Monthly_Salary'] / df['Market_Midpoint'], 2)
    
    def calculate_risk(row):
        if row['Compa_Ratio'] < 0.85 and row['Job_Satisfaction'] <= 2: return 'High'
        elif row['Compa_Ratio'] < 0.95 or row['Job_Satisfaction'] <= 3: return 'Medium'
        else: return 'Low'
        
    df['Retention_Risk'] = df.apply(calculate_risk, axis=1)
    return df

df_gold = load_gold_data()

# 3. Interactive Sidebar Filters (State Management triggers)
st.sidebar.header("Dashboard Filters")
selected_dept = st.sidebar.multiselect(
    "Filter by Department:",
    options=df_gold['Department'].unique(),
    default=df_gold['Department'].unique()
)

# Apply filter to the dataset
df_filtered = df_gold[df_gold['Department'].isin(selected_dept)]

# 4. High-Level Executive KPI Scorecards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Active Headcount", value=len(df_filtered))
with col2:
    avg_salary = f"${int(df_filtered['Monthly_Salary'].mean()):,}"
    st.metric(label="Average Monthly Salary", value=avg_salary)
with col3:
    high_risk_count = len(df_filtered[df_filtered['Retention_Risk'] == 'High'])
    st.metric(label="High Retention Risk Personnel", value=high_risk_count, delta="-2 this month", delta_color="inverse")

st.markdown("### Workforce Drill-Down Explorer")

# 5. Display the final processed data asset grid
st.dataframe(df_filtered[['Employee_ID', 'Department', 'Monthly_Salary', 'Compa_Ratio', 'Retention_Risk']], use_container_width=True)