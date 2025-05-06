Native_API_Extract_Load_Raw.ipynb/py
# %%
import requests
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# API access
API_KEY = os.getenv("API_KEY")
headers = {'X-Auth-Token': API_KEY}


# ------------------------
# 📊 MATCH DATA
# ------------------------
url_matches = 'https://api.football-data.org/v4/teams/65/matches?season=2023'
response_matches = requests.get(url_matches, headers=headers)
data_matches = response_matches.json()


matches_df = pd.json_normalize(data_matches['matches'])


# Handle nested 'referees' column
if 'referees' in matches_df.columns:
   matches_df['referees'] = matches_df['referees'].apply(lambda x: str(x) if isinstance(x, list) else x)


# Save match data locally
matches_df.to_csv('raw_api_matches.csv', index=False)


# PostgreSQL connection setup
pg_user = os.getenv("PG_USER")
pg_password = os.getenv("PG_PASSWORD")
pg_host = os.getenv("PG_HOST")
pg_db = os.getenv("PG_DB")


engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_db}')




# Write match data to raw schema
matches_df.to_sql('raw_api_matches', engine, if_exists='replace', index=False, schema='raw')


print("✅ Match data loaded into PostgreSQL → schema: raw")
print(matches_df.info())
print(matches_df.head())


# ------------------------
# 👥 PLAYER DATA
# ------------------------
url_players = "https://api.football-data.org/v4/teams/65"
response_players = requests.get(url_players, headers=headers)
team_data = response_players.json()


players_df = pd.json_normalize(team_data['squad'])


# Optional: keep clean subset
available_columns = ['name', 'position', 'dateOfBirth', 'nationality', 'shirtNumber']
players_df = players_df[[col for col in available_columns if col in players_df.columns]]


# Save player data locally
players_df.to_csv("raw_api_players.csv", index=False)


# Write player data to raw schema
players_df.to_sql('raw_api_players', engine, if_exists='replace', index=False, schema='raw')


print("✅ Player data loaded into PostgreSQL → schema: raw")
print(players_df.info())
print(players_df.head())
