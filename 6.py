x=['apple','banana','cherry','grapes','papaya','strawberry','orange'];
#to find the first 0-2 index element
#print(x[:3]) 
#to find the elements from 4 index element
print(x[4:])
print(x[2::-1])
print(x[6:3:-1])
print(x[2:5])

temp=x[5]
x[5]=x[6]
x[6]=temp
temp1=x[4]
x[4]=x[5]
x[5]=temp1
print(x)

#  arrange the element in this order [0 1 3 4 2 7 6 5]
# list=['apple','banana','kiwi','cherry','grapes','strawberry','orange','papaya']


print(x[:2])