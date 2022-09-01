import sqlite3

conn = sqlite3.connect("woogin.db")
cur = conn.cursor()
conn.execute("""
CREATE TABLE ITEM (
    item_code varchar(20) PRIMARY KEY,
    item_name varchar(100),
    category varchar(100),
    active varchar(10));
""")

conn.commit()
conn.execute("""
CREATE TABLE ITEM_HISTORY (
    id INTEGER AUTOINCREMEN,
    item_code varchar(20),
    barcode varchar(20),
    statement varchar(10),
    history DATE,
    CONSTRAINT brand_history_fk FOREIGN KEY(item_code)
    REFERENCES ITEM(item_code))
;""" )
conn.commit()
conn.close()