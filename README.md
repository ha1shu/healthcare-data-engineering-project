## Healthcare Data Pipeline using Azure Databricks & Medallion Architecture

####  Project Overview

This project was developed as part of the **Celebal Technologies CEI (Celebal Excellence Internship) Program 2026**. It demonstrates an end-to-end Healthcare Data Engineering Pipeline built using ADLS gen2, External Databricks, PySpark, Delta Lake, and Lakeflow Declarative Pipelines.

The solution follows the Medallion Architecture (Bronze → Silver → Gold) to transform raw healthcare data into clean, analytics-ready datasets. It automates data ingestion, data transformation, and business-level aggregations, providing a scalable and reliable data processing workflow aligned with modern Data Engineering best practices.

---

####  Project Workflow

1. Upload healthcare dataset into Azure Data Lake Storage Gen2.
2. Ingest raw CSV into Bronze Layer.
3. Clean and transform data in Silver Layer.
4. Generate business-level Gold tables.
5. Execute the complete workflow using Lakeflow Pipelines.

---

###  Project Screenshots

## 1️ Source Data Stored in Azure Data Lake Storage Gen2

The healthcare dataset is stored inside an Azure Storage Container before ingestion.

<img width="1643" height="791" alt="Screenshot 2026-07-08 145910" src="https://github.com/user-attachments/assets/c7872597-9dae-4ca5-a754-ea6e03274a08" />

---

## 2️ Bronze Layer

<img width="1902" height="848" alt="Screenshot 2026-07-11 183059" src="https://github.com/user-attachments/assets/a81367b1-35a1-4f81-8747-e266d98b928e" />
The raw healthcare dataset is loaded into the Bronze Layer from the source CSV file. Basic column name standardization is performed to maintain consistency and the data is stored as a Delta table without modifying the original records or applying any business transformations.

#### Code of bronze this:-
<img width="1910" height="906" alt="image" src="https://github.com/user-attachments/assets/532c839c-085e-4a54-926e-3760510c3405" />

---

## 3️ Pipeline Source Code Structure

The project is organized into separate Silver and Gold transformation modules inside the Databricks Pipeline.

<img width="441" height="657" alt="Screenshot 2026-07-08 143421" src="https://github.com/user-attachments/assets/a58b76fa-cd6e-4823-858c-f7ef73fcf427" />

---

## 4️ Pipeline Graph

This graph shows the dependency between the Silver Layer and multiple Gold Layer materialized views.
<img width="1896" height="887" alt="image" src="https://github.com/user-attachments/assets/79e60ec6-c4ea-43ae-ab56-860bf81fa043" />

---

## 5 Successful Pipeline Job Execution

The pipeline job executes the complete Medallion workflow by running the Bronze ingestion notebook first, followed by the Silver and Gold transformation pipeline, ensuring end-to-end automated data processing.
<img width="1662" height="832" alt="Screenshot 2026-07-08 143403" src="https://github.com/user-attachments/assets/c16c2942-cd33-4ed8-b6e1-64d623bd189a" />

<img width="1912" height="923" alt="image" src="https://github.com/user-attachments/assets/b16b9a98-7fd7-4be0-a334-ab501471a642" />


---
```
healthcare-data-engineering-project
│
├── README.md
├── LICENSE
│
├── notebooks/
│   ├── bronze_to_adls.ipynb
│   └── test_business_data.ipynb
│
├── pipeline/
│   ├── silver/
│   │   └── silver_transformation.py
│   │
│   └── gold/
│       ├── gold_patient_count_by_hospital.py
│       ├── gold_average_billing_by_hospital.py
│       ├── gold_condition_analysis.py
│       ├── gold_admission_type_analysis.py
│       └── gold_hospital_ranking.py
│
├── screenshots/
│   ├── azure-storage.png
│   ├── bronze-layer.png
│   ├── pipeline-folder.png
│   ├── pipeline-graph.png
│   └── pipeline-job.png
│
└── docs/
    └── architecture.png
```

---

### Gold Layer Outputs

The Gold Layer produces business-ready analytical tables including:

- Patient Count by Hospital
 <img width="1917" height="892" alt="image" src="https://github.com/user-attachments/assets/de2211b1-3385-427a-bcbc-50fee30644fe" />

- Average Billing by Hospital
<img width="910" height="511" alt="image" src="https://github.com/user-attachments/assets/59fb5485-a708-4bca-aa71-815c3799a3bf" />
 
- Hospital Ranking
<img width="852" height="525" alt="image" src="https://github.com/user-attachments/assets/493face0-9e7a-42bd-a5a4-1ff67a47874b" />

- Admission Type Analysis
<img width="1916" height="811" alt="image" src="https://github.com/user-attachments/assets/934e41f2-85f6-4637-83aa-8c3590e11988" />

- Medical Condition Analysis
<img width="838" height="522" alt="image" src="https://github.com/user-attachments/assets/4cc7e346-4a29-47ae-991d-1235bcc326c8" />

These tables can be directly connected to Power BI, Tableau, or Databricks SQL Dashboards.

---

#### Key Features

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

####  Technology Stack

- Azure Data Lake Storage Gen2
- External Databricks
- PySpark
- Delta Lake
- Unity Catalog
- Lakeflow Declarative Pipelines
- Git & GitHub

---

####  Future Enhancements

- Power BI Dashboard
- Incremental Data Loading
- Change Data Capture (CDC)
- Real-Time Streaming using Kafka
- Predictive Analytics using Machine Learning

---

# Author

**Harshit Sharma**

Data Engineer | Azure | PySpark | Databricks | SQL | Python

GitHub: https://github.com/ha1shu


---
