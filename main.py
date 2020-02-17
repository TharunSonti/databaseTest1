import sqlite3

# http://docs.python.org/3/library/sqlite3.html

con = sqlite3.connect("test.db")
cur = con.cursor()

# Create table
try:
  cur.execute('''CREATE TABLE test
             (id integer primary key, year real, price real)''')
except sqlite3.Error as e:
  print("caught sql error 1:", e.args[0]) 


try:
  with con:
    cur.execute('''INSERT INTO test VALUES ('4', '2020', '2')''')
    cur.execute('''INSERT INTO test VALUES ('2', '2020', '29')''')
    cur.execute('''INSERT INTO test VALUES ('3', '2020', '26')''')
except sqlite3.Error as e:
  print("caught sql error 2:", e.args[0]) 


# con.row_factory = sqlite3.Row
# cur = con.execute('select * from test')
# # instead of cursor.description:
# row = cur.fetchall()
# names = row[0].keys()
# print(names)

for row in cur.execute('SELECT * FROM test'):
  print(row)

con.commit()
con.close()