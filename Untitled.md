```python
print('hello')
```

    hello
    


```python
x=['apple', 'banana','cherry','grapes','strawberry','papaya','orange']
print(x)
```

    ['apple', 'banana', 'cherry', 'grapes', 'strawberry', 'papaya', 'orange']
    


```python
x=['apple', 'banana','cherry','grapes','strawberry','papaya','orange']
print(x[:3])
```

    ['apple', 'banana', 'cherry']
    


```python
x=['apple', 'banana','cherry','grapes','strawberry','papaya','orange']
print(x[-4:-1])
```

    ['grapes', 'strawberry', 'papaya']
    


```python
x=['apple', 'banana','cherry','grapes','strawberry','papaya','orange']
print(x[::-1])
```

    ['orange', 'papaya', 'strawberry', 'grapes', 'cherry', 'banana', 'apple']
    


```python
x=['apple', 'banana','cherry','grapes','strawberry','papaya','orange']
print(x[6:3:-1])
```

    ['orange', 'papaya', 'strawberry']
    


```python
x=['apple', 'banana','cherry','grapes','strawberry','papaya','orange']
print(x[2::-1])
```

    ['cherry', 'banana', 'apple']
    


```python
x=['apple', 'banana','cherry','grapes']
x.append('orange')
x.append('papaya')
x.append('strawberry')
print(x)
```

    ['apple', 'banana', 'cherry', 'grapes', 'orange', 'papaya', 'strawberry']
    


```python
x=['apple', 'banana','cherry','grapes','papaya','strawberry','orange']
temp=x[4]
x[4]=x[5]
x[5]=temp
print(x[:4]+x[:-4:-1])
```

    ['apple', 'banana', 'cherry', 'grapes', 'orange', 'papaya', 'strawberry']
    


```python

```
