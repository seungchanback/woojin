import sqlite3

with open('./sample_data_item.sql','r') as item_sample_script_file:
    item_sample_script = item_sample_script_file.read()

conn = sqlite3.connect("woogin.db")
cur = conn.cursor()
cur.executescript(item_sample_script)
conn.commit()
conn.close()