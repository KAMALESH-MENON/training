import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(
        database=os.getenv("DATABASE"),
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        port=os.getenv("PORT")
    )


cursor = connection.cursor()
