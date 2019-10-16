from dbms.mongodb import Mongo as dbms

print(dbms.get_stock_data(["MSFT"], ("20190102", "20190107")))
