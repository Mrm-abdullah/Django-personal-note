# anisul islam 31
# matrix
""" matrix = [
    [1,2,3],
    [3,4,5]
]

matrix[0][2] = 10 #value change korar jonno
print(matrix[0][2])
for row in matrix:
    for col in row:
        print(col) """

# dictionary
""" studentId = {
    "101" : "Abdullah",
    102 : "Abdullah2",
    "103" : "Abdullah3",
}
print(studentId['101'])
print(studentId[101])
# print(studentId['105'])
print(studentId.get('103'))
print(studentId.get('106'), 'not a valid key') """

# truples
""" students = (
    "abdullah",
    ('a', 'as', 'ds',),
    "robel",
    "sakib",
)
print(students[1])
print(students[1:]) """

# set
""" num = {1,2,3,4,5,5}
print(num)
num1 = {1,2,3,4,5}
num2 = set([4,5,6])
num2.add(7)
num2.remove(7)
print(num2)
print(4 in num2)
print(4 not in num2)

print( num1 | num2)
print( num1 & num2)
print( num1 - num2) """

# stack ---- LIFO
""" books = []
books.append("learn c")
books.append("learn c++")
books.append("learn python")
print(books)
books.pop()
print('Now the top book: ', books[-1])
books.pop()
print('Now the top book: ', books[-1])
books.pop()
print(books)
if not books:
    print('no books') """

# queue ----FIFO ==== practice anisul 35
""" from collections import  deque

bank = deque(['anis', 'rasel', 'sakib'])
bank.popleft()
bank.popleft()
bank.popleft()
print(bank)
if not bank:
    print('no persion') """

# function
""" def add(a,b):
    sum = a+b
    print(sum)
add(2,3)
def addition(a,b,c):
    sum = a+b+c
    print(sum)
addition(2,3,4)

def message():
    print('hello everyone')
message() """

# return value from function
""" def add(a, b):
    sum = a + b
    return sum
print(add(3,4))

def large(a,b,c):
    if a>b and a>c:
        return a
    elif a<b>c:
        return b
    else:
        return c
print(large(34,39,10)) """