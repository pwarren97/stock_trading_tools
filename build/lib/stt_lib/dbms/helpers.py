import stt_lib.conf
import stt_lib.dbms

def import_dbms():
    if stt_lib.conf.DB == "mongodb":
        from stt_lib.dbms.mongodb import Mongo as dbms
        dbms.connect()
    elif stt_lib.conf.DB == "sql":
        from stt_lib.dbms.sql import SQL as dbms
        dbms.connect()
    return dbms
