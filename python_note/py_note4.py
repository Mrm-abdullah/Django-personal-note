# xargs ------ anisul 38
""" def student(*details):
    print(details)
    print(details[0])
student(101, 'rasel')
student(101, 'rasel', 3.69)

def add(*numbeers):
    sum = 0
    for num in numbeers:
        sum = sum + num
    return sum
print(add(1,2,3,4,5)) """

# xxargs
""" def student(**details):
    print(details)
    print(details['name'])
student(id=101, name= 'rasel') """

# lamda function
""" print((lambda a,b : a*a + 2*a*b + b*b) (2,3)) """

# map
""" def squere(x):
    return x*x
num = [1,2,3,4,5]
print(list(map(squere,num))) """

# filter
""" num = [1,2,3,4,5]
f = list(filter(lambda x : x%2==0, num))
print(f) """
