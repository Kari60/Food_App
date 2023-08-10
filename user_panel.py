import json
class User:
    def __init__(self):
        try:
            with open("user_details.json","r") as f:
                user_data=json.load(f)
            self.count=len(user_data)
            self.user_details=user_data
            #print("self count is",self.count,len(user_data))
        except:
            self.count=0
            self.user_details={}
    def register(self):
        self.count=self.count+1
        name=input("Please Enter Your Full Name: ")
        phone_no=int(input("Please Enter Your Phone Number: "))
        email=input("Please Enter Your Email ID: ")
        address=input("Please Enter Your Address: ")
        password=input("Please Enter Your Password: ")
        user_data={"Full Name":name,"Phone Number":phone_no,"Email":email,"Address":address,"Password":password,"Order History":[]}
        self.user_details[self.count]=user_data
        #self.user_details[user_id]["Order History"]
        with open("user_details.json","w") as f:
            json.dump(self.user_details,f,indent=3)
        print("Congratulations: ",name, ", You are Registered Successfully to our Food App...")
        return self.user_details
    def user_login(self):
        print("\n\n************** Login Page **************\n\n")
        with open("user_details.json","r") as f:
            user_data=json.load(f)
        all_mails=[]
        for user_id,user_details in user_data.items():
            all_mails.append(user_details["Email"])
        counter=0
        while True:
            counter+=1
            email=input("Please Enter your Email ID: ")
            password=input("Please Enter your Password: ")
            user_password=""
            if email in all_mails:
                for user_id,user_details in user_data.items():
                    if user_data[user_id]["Email"]==email:
                       user_password=user_data[user_id]["Password"]
                       break                
                if password==user_password:
                    print("You are successfully Logged in...")
                    return user_id
                else:
                    print("Incorrect Password, Please provide valid password...")
                    if(counter==3):
                        return False
            else:
                print("Incorrect Email ID, Please provide valid Email ID if you are registered user...")
                if(counter==3):
                    return False

    def display_menu_options(self):
        print("\n\n************** Please choose one of the below 3 options Available for you **************\n\n")
        print("\n\n\t\t\t 1. Place New Order")
        print("\n\n\t\t\t 2. Order History")
        print("\n\n\t\t\t 3. Update Profile")
        sel_option=int(input("Please choose one of the above 3 options(enter either 1 or 2 or 3): "))
        return sel_option
    def place_new_order(self,user_id):
        food_menu=[{"food_name":"Tandoori Chicken","Quantity":"4 pieces","Price":240},
                   {"food_name":"Vegan Burger","Quantity":"1 piece","Price":320},
                   {"food_name":"Truffle Cake","Quantity":"500 gm","Price":900},
                   ]
        for index,i in enumerate(food_menu):
            print("item no: ",index+1," and item data:",i)
        sel_option=input("Please enter the list of food items you want to have(Ex: 1,2 for Tandoori and Vegan): ")
        options=sel_option.split(",")
        print("You have selected the below food item(s):")
        for option in options:
            if int(option) in list(range(1,len(food_menu)+1)):
                print("\n\n")
            else:
                print("Please choose the item numbers from the Menu provided...")
        ordered_food_items=[]
        for option in options:
            item_no=int(option)
            print("item no:",item_no," and item data: ",food_menu[item_no-1])
            ordered_food_items.append(food_menu[item_no])
        print("\n\nPress 1 for Order Confirmation:\n\n")
        print("\n\nPress 2 for Order Deletion:\n\n")
        choice=int(input("Please enter your choice: "))
        if choice==1:
            print("\n\nOrder Placed Successfully...\n\n")
        else:
            print("\n\nOrder Cancelled...\n\n")        
        self.user_details[user_id]["Order History"].append(ordered_food_items)
        with open("user_details.json","w") as f:
            json.dump(self.user_details,f,indent=3)
        return ordered_food_items
    def order_history(self,user_id):
        with open("user_details.json","r") as f:
            user_data=json.load(f)
        for id,user_details in user_data.items():
            if id==user_id:
                print("\n\n************** You have previously ordered below food items **************\n\n")
                for history in user_data[id]["Order History"]:
                    print(history)
                break
            else:
                print("You don't have any orders till now...")
                break
    def update_profile(self,user_id):
        with open("user_details.json","r") as f:
            user_data=json.load(f)
        for id,user_details in user_data.items():
            print("\n\n************** Please see your details **************\n\n")
            if(id==user_id):
                print(user_data[id])
                field=input("\n\nEnter the Field which you want to edit(provide name of the field as mentioned above Ex: Full Name): ")
                new_value=input("Enter the updated value: " )
                user_data[id][field]=new_value
                print("user data is",user_data[id][field],field,new_value)
                with open("user_details.json","w") as f:
                    json.dump(user_data,f,indent=3)
                print("\n\nUser details updated Successfully\n\n")
                break
        return user_data

