actual_cost=float(input("Please entrer the actual product price:"))
sale_amount=float(input("Please enter the sales amount: "))
if(actual_cost < sale_amount):
    amount=sale_amount-actual_cost
    print("Total profit={0}".format(amount))
else:
    print("No profit!!!!")