#Complete Menu Driven Program will be written here
import sys
from admin_panel import *
from user_panel import *
admin = Admin()
user = User()

while True:
    print("Press 1 For Admin Login \n\n")
    print("Press 2 For User Login \n\n")
    print("Press 3 for Exit\n\n\n")
    choice = int(input("Enter Your Choice: "))
    if choice==1:
        print("************************Admin Login****************************************")
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        valid_login = admin.admin_login(username,password)
        if valid_login:
            print("Logged in Successfully\n\n")
            print("Press 1 For Add New Food Items\n\n")
            print("Press 2 For Edit Food Items\n\n")
            print("Press 3 For View Food Items\n\n")
            print("Press 4 For Remove Food Item from the Menu\n\n")
            
            option = int(input("Enter Your Choice :"))
            if option==1:
                admin.add_food_item()
                print("\n\n")
                print("Food Item Added Successfully")
                print("\n\n")
                print("Thank You for using our application")
                exit_check=int(input("Press 1 button if you want to exit now: "))
                if(exit_check==1):
                    sys.exit()
            elif option==2:
                admin.edit_food_item()
                print("\n\n")
                print("Food Item Edited Successfully")
                print("\n\n")
                print("Thank You for using our application")
                exit_check=int(input("Press 1 button if you want to exit now: "))
                if(exit_check==1):
                    sys.exit()
            elif option==3:
                admin.Show_Food_Items()
                print("\n\n")
                print("You are able to see all Food Items Successfully")
                print("\n\n")
                exit_check=int(input("Press 1 button if you want to exit now: "))
                if(exit_check==1):
                    sys.exit()
            elif option==4:
                print(admin.remove_food_item())
                print("\n\n")
                print("You are able to remove Food Item Successfully")
                print("\n\n")
                exit_check=int(input("Press 1 button if you want to exit now: "))
                if(exit_check==1):
                    sys.exit()
            else:
                print("Please give Valid Input")
        
        else:
            print("Please Enter Valid UserName and Password")

    elif choice==2:
        print("************************User Login****************************************\n\n")
        print("Press 1 If you are New user and want to Register : \n\n")
        print("Press 2 For User Login : \n\n")
        print("Press 3 for Exit\n\n\n")
        option_main = int(input("Enter Your Choice : "))
        if(option_main==1):
            print("************************New User Registration Page****************************************")
            valid_login = user.register()        
            print("************** Please provide login details now to login as existing user **************\n\n")
            option_main=2
        if(option_main==2):    
            valid_login = user.user_login()
            if valid_login:
                print("Logged in Successfully\n\n")
                print("Press 1 for Place New Order\n\n")
                print("Press 2 for Order History\n\n")
                print("Press 3 for Update Profile\n\n")
                option_sub = int(input("Enter Your Choice :"))
                if option_sub==1:
                    user.place_new_order(valid_login)
                    print("\n\n")
                    print("Thank You for using our application")
                    exit_check=int(input("Press 1 button if you want to exit now: "))
                    if(exit_check==1):
                        sys.exit()
                elif option_sub==2:
                    user.order_history(valid_login)
                    print("\n\n")
                    print("Thank You for using our application")
                    exit_check=int(input("Press 1 button if you want to exit now: "))
                    if(exit_check==1):
                        sys.exit()
                elif option_sub==3:
                    user.update_profile(valid_login)
                    print("\n\n")
                    print("Thank You for using our application")
                    exit_check=int(input("Press 1 button if you want to exit now: "))
                    if(exit_check==1):
                        sys.exit()
                else:
                    print("Please give Valid Input")
        
        else:
            print("Please Enter Valid UserName and Password")
    elif choice==3:
        print("Thank You for using our application")
        sys.exit()
