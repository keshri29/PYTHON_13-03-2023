#wap to print the distance between the two given point by user

# x1= int(input("enter x1: " ))
# x2= int(input("enter x2: " ))
# y1= int(input("enter y1: " ))
# y2= int(input("enter x2: " ))
# r=(((x2-x1)**2 + (y2-y1)**2 )**0.5)
# print("the distance between two point are:",(r))

x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)