# 🏟️ Football Data Pipeline & Analytics Project

## 🧰 Tech Stack

- **Python** – for API interaction, data processing, and transformation
- **SQL** – for querying and analysis of structured data
- **AWS RDS (PostgreSQL)** – for storing raw, staging, and warehouse data
- **GitHub Actions** – for scheduling automated extract and load jobs
- **Looker Studio** – for building interactive visual dashboards
- **dbt (Data Build Tool)** – for transforming and modeling warehouse data

## 🎯 Project Objective

**Who are you helping?**  
This project supports performance analysts at elite football clubs, like Manchester City, by enabling smarter decisions regarding player workload and injury prevention.

**What problem are you solving?**  
Analysts often lack a clean, centralized system for viewing historical match workloads, player appearances, and injury trends. Manual tracking limits insights.

**How will you solve their problem?**  
By building an end-to-end pipeline that extracts match and player data via API and web scraping, loads it into a warehouse, transforms it using dbt, and visualizes it in Looker Studio, we provide clear performance metrics at their fingertips.

## 👔 Job Description

This project aligns with the job description for a **Performance Data Analyst** at **Manchester City FC**. The role involves building scalable data infrastructure, collaborating with coaching staff, and leveraging analytics to enhance player availability and performance.

This project mimics the end-to-end responsibilities of that role—from ETL and transformation to visualization and insight delivery.

🔗 [View Job_Description.pdf](./proposal/Job_Description.pdf)

## 📊 Data

### Sources
- [Football-Data.org API](https://www.football-data.org/documentation/quickstart) – for match and player statistics
- [FBref via web scraping](https://fbref.com/en/) – for detailed squad, position, and injury information

### Characteristics
- Multi-season player and match data (scores, team stats, minutes played)
- Semi-structured JSON from API
- Structured HTML tables for scraping

## 📓 Notebooks / Python Scripts

- [`api_extract_load_raw.py`](./api/API_Extract_Load_Raw.py): Extracts and loads match/player data into raw schema  
- [`web_scrape_extract_load_raw.py`](./scrape/Web_Scrape_Extract_Load_Raw.py): Scrapes squad data and stores into raw schema  
- [`dbt_models/`](./dbt_models/): dbt transformations for staging and analytics tables  
- [`Native_API_SQL_Analysis.ipynb`](./analysis/Native_API_SQL_Analysis.ipynb): SQL-based descriptive and diagnostic analysis  
- [`Web_Scrape_SQL_Analysis.ipynb`](./analysis/Web_Scrape_SQL_Analysis.ipynb): SQL analysis of scraped squad data

## 🚀 Future Improvements

- Integrate injury history API for more robust risk modeling  
- Add a machine learning component for predicting future injuries based on player workload patterns 
