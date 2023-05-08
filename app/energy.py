import sqlite3
import csv

DB_FILE = "energy.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS")
