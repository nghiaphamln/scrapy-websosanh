import _sqlite3


class DatabasePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = _sqlite3.connect("./data.db")
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""DROP TABLE IF EXISTS DATA""")
        self.cur.execute("""CREATE TABLE DATA (name text, price text, image text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cur.execute("""INSERT INTO DATA VALUES (?, ?, ?)""", (item['name'], item['price'], item['image']))
        self.conn.commit()
