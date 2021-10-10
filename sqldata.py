#extracting data from mysql
def sql_data():
    import mysql.connector as sc
    import pandas as pd
    print()
    mycon=sc.connect(host="localhost",user="root",passwd="1234",database="userinfo")
    c=mycon.cursor()
    c.execute("select * from userid;")
    e=c.fetchall()


    





