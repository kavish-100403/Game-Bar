# Group Members: 12 Science A
# Project Name: Game Bar
# Member 1 : Hem Desai-19
# Member 2 : Kavish Rajpopat-21
# Member 3 : Prarthan Agarwal-29
import mysql.connector as sc
import pandas as pd
print("\t \t \t \tWelcome to GameBar")


while True:
    print()
    mycon = sc.connect(host="localhost", user="root",
                       passwd="1234", database="userinfo")
    c = mycon.cursor()
    c.execute("select * from userid;")
    e = c.fetchall()
    d = dict(e)
    print("LOGIN OR REGISTER")
    print("1.for Login: \n2.for Register:")
    inp = int(input("1 0r 2:"))
    if inp == 1:
        a = input("Enter user_id:")
        b = input("Enter user_pwd:")
        if a in d.keys():
            if d[a] == b:
                print("SUCCESFULLY LOGGED IN")
                import gamedata
                game = gamedata.gamesui()
                print(game)
                break

            else:
                print("INVALID PASSWORD \n")

        else:
            print("INVALID USERNAME \n")

    if inp == 2:
        import registration
        registration.reg()
    else:
        print("choose from above options \n")
