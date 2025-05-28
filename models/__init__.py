import sqlite3

CONN = sqlite3.connect('coursera.db')
CURSOR = CONN.cursor()