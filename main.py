import pandas as pd
from fastapi import FastAPI
import random

app = FastAPI()


df = pd.read_csv('AnimeQuotes.csv')


@app.get("/")
def root():
    return {"message": "Hi, this is Random Anime Qoute API"}


@app.get("/random-anime-quote")
def root():
    num = random.randint(0, 120)
    quote = df['Quote'][num]
    character = df['Character'][num]
    anime = df['Anime'][num]
    return {
        "quote": quote,
        "character": character,
        "anime": anime
    }
