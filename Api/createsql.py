from Api.connect import connect


def sql_create():
    db = connect()
    curseur = db.cursor()

    curseur.execute("DROP TABLE IF EXISTS EMPLOYEE")
    tab1 = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    curseur.execute(tab1)

    curseur.execute("DROP TABLE IF EXISTS ami")
    tab2 = """CREATE TABLE ami (
             prenom  CHAR(20) NOT NULL,
             nom  CHAR(20),
             age INT,  
             sex CHAR(1))"""
    curseur.execute(tab2)

    curseur.close()
    db.close()
