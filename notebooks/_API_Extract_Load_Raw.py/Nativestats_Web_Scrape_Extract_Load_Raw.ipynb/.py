# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ------------------------
# 🔐 Load environment variables
# ------------------------
load_dotenv()
pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_host = os.getenv("PG_HOST")
pg_db = os.getenv("PG_DB")

# ------------------------
# 🌐 SCRAPE PLAYER DATA
# ------------------------

url = "https://native-stats.org/team/65"
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the squad table
table = soup.find('table')
rows = table.find_all('tr')[1:]  # Skip header row

# Extract player data
data = []
for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 6:
        number = cols[0].text.strip()
        name = cols[1].text.strip()
        position = cols[2].text.strip()
        contract_start = cols[3].text.strip()
        contract_end = cols[4].text.strip()
        minutes = cols[5].text.strip()
        data.append([number, name, position, contract_start, contract_end, minutes])

# Create DataFrame
players_df = pd.DataFrame(data, columns=[
    'jersey_number', 'name', 'position', 'contract_start', 'contract_end', 'minutes_played'
])

# Save to CSV
players_df.to_csv('raw_web_players.csv', index=False)

# ------------------------
# 🛢️ LOAD INTO PostgreSQL
# ------------------------

engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_db}')

if not players_df.empty:
    players_df.to_sql('raw_web_players', engine, if_exists='replace', index=False, schema='raw')
    print("✅ Web-scraped player data loaded into PostgreSQL → schema: raw")
else:
    print("⚠️ No player data found. Table not created.")

# Show results
print(players_df.info())
print(players_df.head())
