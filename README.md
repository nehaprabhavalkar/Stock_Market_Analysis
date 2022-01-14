# Stock Market Analysis
A tool to analyse NSE Stock Data for Nifty 50 stocks

## Overview

- Automated data collection from NSE website for each business day
- Automated data quality checks to ensure correctness of the data
- Visualizations showing trends for the stock for 5 Day, 1 Month, 6 Months and 1 Year 


## Project Directory Structure

```
Stock_Market_Analysis
├─ .github
│  └─ ISSUE_TEMPLATE
│     ├─ feature-template.md
│     ├─ story-template.md
│     └─ task-template.md
├─ .gitignore
├─ code
│  ├─ backfill.py
│  ├─ config.json
│  ├─ current.py
│  ├─ holiday_check.py
│  ├─ utils.py
│  ├─ __init__.py
│  
├─ dags
├─ images
├─ README.md
├─ sql
│  ├─ holidays_ddl.sql
│  ├─ holidays_dml.sql
│  ├─ sectors_ddl.sql
│  ├─ sectors_dml.sql
│  ├─ stocks_ddl.sql
│  └─ stocks_dml.sql
├─ web
│  ├─ app.py
│  ├─ graph_utils.py
│  ├─ static
│  │  └─ styles
│  │     └─ style.css
│  ├─ templates
│  │  ├─ index.html
│  │  └─ results.html
│  ├─ test.db
│  ├─ __init__.py
│  
├─ __init__.py

```

## Tech Stack
#### Python Libraries
- requests
- pandas
#### Database
- SQLite
#### Pipeline Orchestration 
- Apache Airflow
#### Web 
- Flask 
- HTML / CSS
- JavaScript

## Files Description

## Setup


## License
MIT