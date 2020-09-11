def import_dbms():
    if stt_lib.conf.DB == "mongodb":
        from stt_lib.dbms.mongodb import Mongo as dbms
    elif stt_lib.conf.DB == "sql":
        from stt_lib.dbms.sql import SQL as dbms
    return dbms
