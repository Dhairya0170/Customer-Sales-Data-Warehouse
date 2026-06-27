# 📊 Customer Sales Data Warehouse

A complete **Data Warehouse** solution for customer sales analysis. This project demonstrates end-to-end data modeling, ETL processes, and dimensional modeling using Star Schema.

## 🏗️ Architecture

- **Data Generation**: Python + Faker
- **Ingestion**: Python + psycopg2 (load to PostgreSQL)
- **Data Warehouse**: Star Schema (Fact + Dimensions)
- **Transformation**: SQL + dbt Core
- **Analytics**: Ready-to-use fact table for BI/reporting

## ✨ Key Features

- Synthetic sales dataset generation (5,000+ customers, 300+ products)
- **Star Schema** design with surrogate keys
- Clean separation of **staging** and **marts** layers using dbt
- Automated ETL pipeline (generate → load → transform)
- Ready for Power BI / Tableau analysis

## 🛠️ Tech Stack

- **Python** (Pandas, Faker, psycopg2)
- **dbt Core**
- **PostgreSQL**
- **SQL** (Dimensional Modeling)

## 🚀 How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/Dhairya0170/Customer-Sales-Data-Warehouse.git
   cd Customer-Sales-Data-Warehouse
