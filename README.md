# SmartField Inc. – NYC311 Mini Data Platform

This repository implements a mini data platform using the NYC 311 Service Requests dataset. It follows a complete data pipeline from raw ingestion to ML feature serving using Databricks and open-source tools.

---

## 🏗️ Architecture

- **Delta Lake** medallion architecture (Bronze → Silver → Gold)
- **PySpark** for data ingestion and transformation
- **FastAPI** for serving Gold-layer features via REST API
- **Databricks** as the compute engine and storage layer

---

## 📁 Project Structure

```
nyc311-smartfield-implementation/
│
├── pipeline/                  # PySpark notebooks for Bronze → Gold
│   ├── bronze_ingestion.py
│   ├── silver_transformation.py
│   └── gold_feature_engineering.py
│
├── api/                       # FastAPI microservice
│   ├── main.py
│   ├── routes/
│   │   └── features.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   └── services/
│       └── databricks_query.py
│
├── .env.example               # Environment variable template
├── requirements.txt           # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file from the provided template:
```bash
cp .env.example .env
```

Fill it with:
```env
DATABRICKS_HOST=https://<workspace>.databricks.com
DATABRICKS_TOKEN=your_token
DATABRICKS_WAREHOUSE_ID=your_sql_warehouse_id
```

---

## 🚀 Components

### 🔹 PySpark Notebooks
1. `bronze_ingestion.py`: Reads raw data in JSON format via API and writes to Bronze Delta table
2. `silver_transformation.py`: Cleans, types, validates → Silver
3. `gold_feature_engineering.py`: Extracts ML-ready features → Gold

### 🔹 FastAPI Server
- `/features`: Serves Gold data via Databricks SQL
- `/ping`: Health check endpoint
- Modular codebase with clear separation:
  - `core/`: config + auth
  - `services/`: query logic
  - `routes/`: API endpoints

Run locally:
```bash
uvicorn api.main:app --reload
```

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔐 API Security

- Uses `x-api-key` for authentication
- Credentials and tokens are stored in `.env`
- API keys are parsed from ENV for flexibility

---

## 📄 Dataset

[NYC Open Data – 311 Service Requests](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

---

## 📦 Requirements

- Python 3.8+
- Databricks SQL Warehouse
- Uvicorn, FastAPI, Pandas, Delta Lake libraries