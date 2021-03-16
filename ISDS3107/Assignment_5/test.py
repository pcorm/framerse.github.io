import sqlalchemy as db

engine = db.create_engine('sqlite:///customer.sqlite')
connection = engine.connect()
results = connection.execute('select * from customer')
for row in results:
     print(row)

connection.close()
