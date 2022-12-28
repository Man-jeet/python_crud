# @@@@@@@@@@@@@@@@@@@@@@@  LOGIN PART START HERE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("hello welcome to the crud:")

print(" 1. create an account: \n 2. login \n 3. exit")
option = int(input(" pls enter the option :"))
dic1 = {}
count = 0
dic2 = {"user1": {}}
if option == 1:
    print("Do you want to create a new account \n 1. yes\n 2. no")
    choose = int(input())
    if choose == 1:
        print("OK")
        username = input("enter the user name   \t")
        Name = input("enter the full name  \t")
        for i in range(3):
            passwd = input("Choose the password  \t")
            if len(passwd) > 6 and len(passwd) < 16:
                for i in range(3):
                    mobile_no = input("enter the mobile number \t")
                    if len(mobile_no) == 10 :
                        for i in range(3):
                            email = (input("enter the e-mail \t"))
                            if "@" and ".com" in email:
                                state = input("Enter the state \t ")
                                print("your account has sucessfully created ")
                                dic1.update({username: {"name": Name, "email": email, "mobile number": mobile_no, "password": passwd, "state": state}})
                                print("Do you want to see your data \n 1. yes \n 2. no")
                                human = int(input())
                                if human == 1:
                                    print("your current data is : ", dic1)
                                    while True:
                                        print( "Do you want to login to your database\n  1. yes\n  2. no")
                                        human = int(input())
                                        if human == 1:
                                            user_name = input("enter the user name :")
                                            if user_name in dic1:
                                                passwd = input("enter the password")
                                                user_name = list(dic1.keys())
                                                user_name = "".join(user_name)
                                                if user_name == user_name and passwd == dic1[username]["password"]:
                                                    print("you are login your database sucessfully ")
                                                    choice = int(input("what do you want to your data : \n 1. read \n 2. update\n 3. delete\n 4. exit"))
                                                    if choice == 1:
                                                        print("your current data : ", dic1)
                                                    elif choice == 2:
                                                        print("what do you want to update in your database : \n 1. name\n 2. mobile number\n 3. E-mail\n 4. user id ")
                                                        option1 = int(input("pls enter your choice : \t"))
                                                        if option1 == 1:
                                                            option2 = input("pls enter the new name : \t")

                                                            dic1[user_name]["name"] = option2
                                                            print("your database is update sucessfully ")

                                                            print("Do you want to read your database : \n 1. yes\n 2. no")
                                                            option3 = int(input("enter your choice: \t"))
                                                            print("updated database ")
                                                            if option3 == 1:
                                                                print(dic1)
                                                        elif option1 == 2:
                                                            for i in range(3):
                                                                print("please Enter the new mobile number : \t")
                                                                option2 = input()
                                                                if len(option2) == 10:
                                                                    dic1[user_name]["mobile number"] = option2
                                                                    print("Do you want to read your database : \n 1. yes\n 2. no")
                                                                    option3 = int(input("enter your choice: \t"))
                                                                    print("updated database ")
                                                                    if option3 == 1:
                                                                        print(dic1)
                                                                        break
                                                                else:
                                                                    print("please enter the correct mobile numbers")
                                                                    if i == 2:
                                                                        exit()
                                                        elif option1 == 3:
                                                            print("please Enter the new E-mail : \t")
                                                            option2 = input()
                                                            dic1[user_name]["E-mail"] = option2
                                                            print("E-mail is updated sucessfully \n Do you want to read your database : \n 1. yes\n 2. no")
                                                            option3 = int(
                                                                input("enter your choice: \t"))
                                                            print("updated database ")
                                                            if option3 == 1:
                                                                print(dic1)
                                                        elif option1 == 4:
                                                            print("please Enter the user id : \t")
                                                            option2 = input()
                                                            dic1[option2] = dic1[user_name]
                                                            del dic1[user_name]
                                                            print("user id is update sucessfully \n Do you want to read your database : \n 1. yes\n 2.   no")
                                                            option3 = int(
                                                                input("enter your choice: \t"))
                                                            if option3 == 1:
                                                                print("updated database : ", dic1)
                                                    elif choice == 3:
                                                        print("Do you want to delete some data from your database ?\n 1. yes\ 2. no")
                                                        option3 = int(input())
                                                        if option3 == 1:
                                                            print( "please insert the data you want to delete :")
                                                            option2 = input()
                                                            if option2 == "password":
                                                                print("you do not delete your password\n This is the your login caredential")
                                                            else:
                                                                data1 = dic1[user_name].pop(option2)
                                                                print("your database after delete some data :", dic1)
                                                                print("Do you want to check delete data :\n 1. yes \n 2. no")
                                                                option3 = int(input())
                                                                if option3 == 1:
                                                                # print(data1)
                                                                    print(option2, ":", data1)
                                                                else:
                                                                    print(" ok\n your data is not visiable as per your request")
                                                        else:
                                                            print(" ok \n No data is deleted from your database ")
                                                    elif choice == 4:
                                                        print(" ok \nyou are exit from your database")
                                                        exit()
                                                else:
                                                    print("please enter the valid user name or password")
                                            else:
                                                print("user name not exits in the database\n please enter the  valid user name  ")
                                        else:
                                            print("OK\n you are exit from the database")
                                            exit()
                                else:
                                    print("OK thanks for creating account in the database ")
                                    break
                            else:
                                print("please enter the valid email \n (for example example@example.com)")
                                count = count +1
                                if count == 3:
                                        print("you have reached maximum limit \n you are out of the program")
                    else:
                        print("please enter the correct mobile numbers ")
            else:
                print("your password length should be between 6 to 15 characters")
    else:
        print("OK , you don't want to create an account")
elif option == 3:
    print(" OK\n you are exit from the program")
    exit()
else:
    print(" you are not login in database\n pls sign up ")
