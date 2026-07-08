## Healthcare Data Pipeline using Azure Databricks & Medallion Architecture

###  Project Overview

This project demonstrates an end-to-end Healthcare Data Engineering Pipeline built using Azure Data Lake Storage Gen2, External Databricks, PySpark, Delta Lake, and Lakeflow Declarative Pipelines.

The pipeline follows the Medallion Architecture (Bronze → Silver → Gold) to transform raw healthcare data into clean, analytics-ready datasets. The project automates data ingestion, transformation, and business-level aggregations while following modern Data Engineering best practices.

---

#  Project Workflow

1. Upload healthcare dataset into Azure Data Lake Storage Gen2.
2. Ingest raw CSV into Bronze Layer.
3. Clean and transform data in Silver Layer.
4. Generate business-level Gold tables.
5. Execute the complete workflow using Lakeflow Pipelines.

---

#  Project Screenshots

## 1️⃣ Source Data Stored in Azure Data Lake Storage Gen2

The healthcare dataset is stored inside an Azure Storage Container before ingestion.

<img width="1643" height="791" alt="Screenshot 2026-07-08 145910" src="https://github.com/user-attachments/assets/c7872597-9dae-4ca5-a754-ea6e03274a08" />

---

## 2️⃣ Bronze Layer

The raw healthcare dataset is successfully loaded into the Bronze Layer without any transformations.

<img width="1091" height="562" alt="image" src="https://github.com/user-attachments/assets/73a80b05-e68f-4e9a-9a29-35a4e09cd91f" />

---

## 3️⃣ Pipeline Source Code Structure

The project is organized into separate Silver and Gold transformation modules inside the Databricks Pipeline.

<img width="441" height="657" alt="Screenshot 2026-07-08 143421" src="https://github.com/user-attachments/assets/a58b76fa-cd6e-4823-858c-f7ef73fcf427" />

---

## 4️⃣ Pipeline Graph

This graph shows the dependency between the Silver Layer and multiple Gold Layer materialized views.

<img width="1503" height="903" alt="Screenshot 2026-07-08 142704" src="https://github.com/user-attachments/assets/1898422c-87a7-447b-ace3-78bf07e4baca" />

---

## 5️⃣ Successful Pipeline Job Execution

The Healthcare Data Pipeline successfully executes from Bronze ingestion to Silver and Gold transformations.
<img width="1662" height="832" alt="Screenshot 2026-07-08 143403" src="https://github.com/user-attachments/assets/c16c2942-cd33-4ed8-b6e1-64d623bd189a" />


---

# 📂 Project Structure

```
Healthcare_Data_Pipeline
│
├── bronze
│
├── silver_transformations
│   └── silver_transformation.py
│
├── gold_transformations
│   ├── gold_patient_count_by_hospital.py
│   ├── gold_average_billing_by_hospital.py
│   ├── gold_condition_analysis.py
│   ├── gold_admission_type_analysis.py
│   └── gold_hospital_ranking.py
│
└── README.md
```

---

# 📊 Gold Layer Outputs

The Gold Layer produces business-ready analytical tables including:

- Patient Count by Hospital
- Average Billing by Hospital
- Hospital Ranking
- Admission Type Analysis
- Medical Condition Analysis

These tables can be directly connected to Power BI, Tableau, or Databricks SQL Dashboards.

---

# ✅ Key Features

- End-to-End Healthcare Data Pipeline
- Medallion Architecture Implementation
- Bronze, Silver & Gold Layers
- Data Cleaning & Standardization
- Business-Level Aggregations
- Delta Lake Tables
- Unity Catalog Integration
- Lakeflow Declarative Pipelines
- Automated Pipeline Execution
- Analytics-Ready Gold Tables

---

# 🚀 Technology Stack

- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- Unity Catalog
- Lakeflow Declarative Pipelines
- Git & GitHub

---

# 📈 Future Enhancements

- Power BI Dashboard
- Incremental Data Loading
- Change Data Capture (CDC)
- Real-Time Streaming using Kafka
- Predictive Analytics using Machine Learning

---

# 👨‍💻 Author

**Harshit Sharma**

Data Engineer | Azure | PySpark | Databricks | SQL | Python

GitHub: https://github.com/ha1shu


---
