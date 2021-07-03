tt = 0
count = 0
while count < 10:
    num = int(input("Enter a non-neg num "))
    while(num<0):
        num =int(input("Please enter a positive number!!! "))
    tt==num
    count+=1
print("The avg is: ", tt/count)

