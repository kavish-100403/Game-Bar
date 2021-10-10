def reg():
    import mysql.connector as sc
    a=input("Enter user_id:")
    b=input("Enter user_pwd:")
    mydb=sc.connect(host="localhost",user="root",passwd="1234",database="userinfo")
    mycursor=mydb.cursor()

    sql = "INSERT INTO userid (userid,pwd) VALUES (%s,%s)"
    val = (a,b)
    mycursor.execute(sql,val)
    mydb.commit()
    print("try logging in now \n")
    
