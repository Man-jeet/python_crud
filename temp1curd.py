# @@@@@@@@@@@@@@@@@@@@@@@  LOGIN PART START HERE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("hello welcome to the curd:")

print(" 1. create an account: \n 2. login \n 3. exit")
option = int(input(" pls enter the option :"))
dic1 = {}
count = 0
dic2 = {"user1": {}}
if option == 1:
    print("Are you create a new account \n 1. yes\n 2. no")
    choose = int(input())
    if choose == 1:
        print("OK")
        username = input("enter the user name  ")
        Name = input("enter the full name ")
        passwd = input("Choose the password ")
        mobile_no = int(input("enter the mobile number"))
        a = 0
        for i in range(3):
            email = (input("enter the e-mail"))

            if "@" and ".com" in email:
                # dic1.update({"email" : email})
                # print(dic1)

                state = input("Enter the state ")
                # print("Are you human ?\n 1. yes \n 2. no")
                # human = int(input())
                # if human == 1:
                print("your account has sucessfully created ")
                dic1.update({username: {"name": Name, "email": email, "mobile number": mobile_no, "password": passwd, "state": state}})

                print("Can you see your data \n 1. yes \n 2. no")
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
                                if user_name == user_name  and passwd == dic1[username]["password"]:
                                    print("you are login your database sucessfully ")
                                    choice = int(input("what do you want to your data : \n 1. read \n 2. update\n 3. delete\n 4. exit"))
                                    if choice == 1:
                                        print("your current data : ", dic1)
                                    elif choice == 2:
                                        print("what do you want to update in your database : \n 1. name\n 2. mobile number\n 3. E-mail\n 4. user id ")
                                        option1 = int(
                                            input("pls enter your choice :"))
                                        if option1 == 1:
                                            option2 = input("pls enter the new name :")

                                            dic1[user_name]["name"] = option2
                                            print("your database is update sucessfully ")

                                            print("Do you want to read your database : \n 1. yes\n 2. no")
                                            option3 = int(input("enter your choice:"))
                                            print("updated database ")
                                            if option3 == 1:
                                                print(dic1)
                                        elif option1 == 2:
                                            print("please Enter the new mobile number :")
                                            option2 = int(input())
                                            dic1[user_name]["mobile number"] = option2
                                            print("Do you want to read your database : \n 1. yes\n 2. no")
                                            option3 = int(
                                                input("enter your choice:"))
                                            print("updated database ")
                                            if option3 == 1:
                                                print(dic1)
                                        elif option1 == 3:
                                            print("please Enter the new E-mail :")
                                            option2 = input()
                                            dic1[user_name]["E-mail"] = option2
                                            print("E-mail is updated sucessfully \n Do you want to read your database : \n 1. yes\n 2. no")
                                            option3 = int(
                                                input("enter your choice:"))
                                            print("updated database ")
                                            if option3 == 1:
                                                print(dic1)
                                        elif option1 == 4:
                                            print("please Enter the user id :")
                                            option2 = input()
                                            dic1[option2] = dic1[user_name]
                                            del dic1[user_name]
                                            print("user id is update sucessfully \n Do you want to read your database : \n 1. yes\n 2.   no")
                                            option3 = int(
                                                input("enter your choice:"))
                                            if option3 == 1:
                                                print("updated database : ", dic1)
                                    elif choice == 3:
                                        print("Are you delete some data in your database ?\n 1. yes\ 2. no")
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
                                                    print(" ok\n you are not visible your data \n GOOD LUCK")
                                        else:
                                            print(" ok \n Not delete the any data from your database ")
                                    elif choice == 4:
                                        print(" ok \n GOOD LUCK \n you are exit from your database")
                                        exit()
                                else:
                                    print("please enter the valid user name or password")
                            else:
                                print("this user name is not exits in the database\n please enter the  valid user name  ")
                        else:
                            print("OK\n you are exit from the database")
                            exit()
                else:
                    print("OK thanks for creating account in the database ")
            # else:
            #     print("invalid mail")
            else:
                print("please enter the valid email \n (for example example@example.com)")
                count = count +1
                if count == 3:
                    print("you reach the maximum limit \n you are exit the program ")
    else:
        print("OK")
elif option == 3:
    print(" OK\n you are exit")
    exit()
else:
    print(" you are not login in this database\n pls sign up ")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ creating account part a-start here @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# if option == 2:
#     user_name = input("enter the user name :")
#     # passwd = int(input("enter the password :"))
#     if user_name in dic2:
#         user1 = list(dic2.keys())
#         print(user1)
#         user_name = "".join(user1)
#         print(user_name)
#         if user_name == user_name:
#             print("you are login your database sucessfully ")
#             print("what do you want to your data : \n 1. read \n 2. update\n 3. delete\n 4. exit")
#             choice = int(input())
#             if choice == 1:
#                 print("your current data : ", dic1)
#             elif choice == 2:
#                 print(
#                     "what do you want to update in your database : \n 1. name\n 2. mobile number\n 3. E-mail\n 4. user id ")
#                 option1 = int(input("pls enter your choice :"))
#                 if option1 == 1:
#                     option2 = input("pls enter the new name :")
#                 # dic1["boy123"]["name"] = option2
#                 # print(dic1)
#                     dic1[user_name]["name"] = option2
#                     print("your database is update sucessfully ")
#                 # print(dic1)
#                     print("Do you want to read your database : \n 1. yes\n 2. no")
#                     option3 = int(input("enter your choice:"))
#                     print("updated database ")
#                     if option3 == 1:
#                         print(dic1)
#                 elif option1 == 2:
#                     print("please Enter the new mobile number :")
#                     option2 = int(input())
#                     dic1[user_name]["mobile number"] = option2
#                     print("Do you want to read your database : \n 1. yes\n 2. no")
#                     option3 = int(input("enter your choice:"))
#                     print("updated database ")
#                     if option3 == 1:
#                         print(dic1)
#                 elif option1 == 3:
#                     print("please Enter the new E-mail :")
#                     option2 = input()
#                     dic1[user_name]["E-mail"] = option2
#                     print("Do you want to read your database : \n 1. yes\n 2. no")
#                     option3 = int(input("enter your choice:"))
#                     print("updated database ")
#                     if option3 == 1:
#                         print(dic1)
#                 elif option1 == 4:
#                     print("please Enter the user id :")
#                     option2 = input()
#                     dic1[option2] = dic1[user_name]
#                     del dic1[user_name]
#                     print(
#                         "user id is update sucessfully \n Do you want to read your database : \n 1. yes\n 2. no")
#                     option3 = int(input("enter your choice:"))
#                     if option3 == 1:
#                         print("updated database : ", dic1)
#             elif choice == 3:
#                 print("Are you delete some data in your database ?\n 1. yes\ 2. no")
#                 option3 = int(input())
#                 if option3 == 1:
#                     print("please insert the data you want to delete :")
#                     option2 = input()
#                     # del dic1[user_name][option2]
#                     data1 = dic1[user_name].pop(option2)
#                     print("your database after delete some data :", dic1)
#                     print("Do you want to check delete data :\n 1. yes \n 2. no")
#                     option3 = int(input())
#                     if option3 == 1:
#                         print(data1)
#                         print(option2, ":", data1)
#                     else:

#                         print(" ok\n you are not visible your data \n GOOD LUCK")
#                 else:
#                     print(" ok \n Not delete the any data from your database ")
#             elif choice == 4:
#                 print(" ok \n GOOD LUCK \n you are exit from your database")

#     else:
#         print(
#             "This user name is not exits in the database\n please sign up in the database ")
# # else:
# #     print("you are not login in the database \n pplease sign up in the database ")1
