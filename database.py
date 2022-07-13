import os
import sqlite3
from msilib import schema


class DB:
    schema = """CREATE TABLE IF NOT EXISTS pancake (
     id INTEGER,
     contract TEXT NOT NULL ,
     symbol TEXT
     version TEXT
      FOREIGN KEY(id) REFERENCES gateio(id)
     
    ##
    CREATE TABLE IF NOT EXISTS gateio(
    id INTEGER,
     symbol TEXT
)

)"""

    def __init__(self, dbFileName="data.db"):
        is_new = not os.path.isfile(dbFileName)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, dbFileName)
        self.conn = sqlite3.Connection(
            db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        if is_new:
            for s in self.schema.split("##"):
                self.conn.cursor().execute(s)
                self.conn.commit()

    def commit(self):
        self.conn.commit()



    def insert_pancake(self, id, contact, symbol, version):
        cur = self.conn.cursor()
        cur.execute("""INSERT OR REPLACE INTO pancake (id, contract, symbol, version)   VALUES(?, ?, ?, ?)""",
                    (id, contact,symbol, version)
                    )

    def insert_gate(self, id, symbol):
        cur = self.conn.cursor()
        cur.execute("""INSERT OR REPLACE INTO gateio (id, symbol)   VALUES(?, ?)""",
                    (id, symbol)
                    )