
#

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items=0
medium_price_item=0
high_price_item=0
customers_served=0
total_sales=0

billing = True


# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
while billing:
    name= input ("\nEnter your name:")
    items=int(input("How many items are you buying? :"))


    if items<=0:
        print ("\nInvalid answer ; enter a positive number!")
        continue

    customer_total = 0 
    item_number=1

    while item_number<=items:
        item_name= input ("\nEnter item name: ") 
        item_price=int (input("Enter the price:  "))
        item_quantity= int(input("Enter the quantity: "))


        if item_price<= 0 or item_quantity<=0:
            print ("Invalid answer")
            continue
            
        item_total= item_price * item_quantity
        customer_total= customer_total+item_total
        print ("\n",item_name, " = ",  item_quantity *item_price ,"\nTotal =", customer_total)
        

        if item_price<=50:
            low_price_items+=item_quantity
        elif item_price<=100:
            medium_price_item+=item_quantity
        else:
            high_price_item+=item_quantity

        item_number+=1                

 
    customers_served+= 1
    total_sales+=customer_total
    
    print ("\nCUSTOMER TOTAL: ", customer_total)
    print ("\n=====BILLING COMPLETED=====")
    next_customer= input("\nNext customer? (yes/no): ").lower()
    if next_customer!="yes":
        billing = False

for slot in range (1,4):
    if slot==1:
        label, total= "Low priced item: ", low_price_items
    elif slot==2:
        label, total = "Medium priced item: ", medium_price_item
    else:
        label,total= "High priced item: ", high_price_item

    if total>0:
        print (f"{label}: {total}", end= " ")
print ( )       
print ("customer served: ", customers_served)
print ("total sales: " , total_sales)

    

    
