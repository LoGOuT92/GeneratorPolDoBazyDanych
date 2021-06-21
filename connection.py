import cx_Oracle
def pol():
    cx_Oracle.init_oracle_client(lib_dir=  r"C:\oracle\instantclient_19_10")
    dsn = cx_Oracle.makedsn("217.173.198.135", 1522, sid="orcltp")
    connection = cx_Oracle.connect("login", "haslo", dsn, encoding="UTF-8")
    return connection