# Admin functionality
import json
class Admin:
    
    def __init__(self):
        try:
            with open("food_item_details.json","r") as f:
                food_data=json.load(f)
            self.count=len(food_data)
            self.food_item_details=food_data
            #print("self count is",self.count,len(food_data))
        except:
            self.count=0
            self.food_item_details={}

    def admin_login(self,username,password):
        if username=="admin" and password=="admin":
            return True
        return False
    
    def add_food_item(self):
        self.count=self.count+1
        food_name=input("Enter the Food Name: ")
        food_quantity=input("Enter the Food Quantity: ")
        # food_quantity=[]
        # food_qunantity_size=int(input("enter the quantity size which we want to add: ")
        food_price=input("Enter the Food Price: ")
        food_discount=input("Enter the Discount on the Food Price")
        food_stock=input("Enter the amount left in stock: ")
        food_item={"Food Name":food_name,"Food Quantity":food_quantity,"Food Price":food_price,"Discount":food_discount,"Food Stock Left":food_stock}
        self.food_item_details[self.count]=food_item
        with open("food_item_details.json","w") as f:
            json.dump(self.food_item_details,f,indent=3)
        return self.food_item_details
    def edit_food_item(self):
        with open("food_item_details.json","r") as f:
            food_data=json.load(f)
        for food_id,single_item in food_data.items():
            print("Food ID:",food_id," ----- Food Items:",single_item)
        id=input("Enter the Food ID which you want to edit: ")
        item=input("Enter the Category which you want to Edit: ")
        new_value=input("Enter the updated value: " )
        food_data[id][item]=new_value
        with open("food_item_details.json","w") as f:
            json.dump(food_data,f,indent=3)
        print("Food details updated successfully...")
        return food_data
    def Show_Food_Items(self):
        with open("food_item_details.json","r") as f:
            food_data=json.load(f)
        for food_id,single_item in food_data.items():
            print("Food ID:",food_id," ----- Food Items:",single_item)
    def remove_food_item(self):
        with open("food_item_details.json","r") as f:
            food_data=json.load(f)
        for food_id,single_item in food_data.items():
            print("Food ID:",food_id," ----- Food Items:",single_item)
        id=input("Enter the Food ID which you want to remove: ")
        del food_data[id]
        with open("food_item_details.json","w") as f:
            json.dump(food_data,f,indent=3)
        return food_data















