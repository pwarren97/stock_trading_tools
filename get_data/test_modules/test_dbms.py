from dbms.mongodb import Mongo as dbms

"""
Coverage:

"""
def run():
    print(dbms.get_stock_data(["MSFT"], ("20190102", "20190107")))
