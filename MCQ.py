### Q1
# ==> a) error     because syntax error class is nor defined properly 

# Q2
# ==> class keyword

# Q3)
# ==>c) Reference to current object

# Q4)
# ==> d)__init__ constructor 

# Q5
# ==> c)

#Q6
# def calculate_price(price,category):
    
    
#     if category.lower()=="electronic":
#         gst=0.18
#     elif category.lower()=="clothing":
#         gst=0.05
#     elif category.lower()=="books":
#         gst=0
#     else :
#         gst=0
    
#     final_price=price+(price*gst)
#     return final_price

# store=calculate_price(20000,"electronic")
# print(store)
    
        
# Q7)
# ch=int(input("enter the value"))

# match ch:
#     case 1:
#         print("View Products")      
#     case 2:
#         print("Add to Cart") 
#     case 3:
#         print("Checkout") 
#     case 4:
#         print("Exit")
#     case _:
#         print("invalid choice")


# Q8)
def count_items(cart):
    store=len(cart)
    print('total is :',store)
cart= ["Laptop","Mouse","Keyboard"]
count_items(cart)


