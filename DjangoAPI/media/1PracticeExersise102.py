#Prompt the user to inter the price of itme
p = float(input("Enter the price of the item: "))
while(p<=0):
    print("Wrong input! Please inter a valid price: ")
    p = float(input("Enter the price of the item: "))
qOFi = float(input("Enter the quantity of purchased: "))
print("The price of the item:", p)
print("The quantity of the item:", qOFi)
t = 0
if(qOFi>=10):
    t=0.95*p*qOFi
    print("Total after discount:", 0.95*p*qOFi)
else:
    tNd=p*qOFi
    print("Total: %.2f",(tNd))
             
             
