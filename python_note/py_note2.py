# anisul islam dio 23 start

# list

""" subjects = ['c','c','c', 'c++', 'java', 'os', '12', '56']
print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1])
print('c' in subjects) # ck korar jonno
print('cc' not in subjects) # ck korar jonno
print(subjects + [77, 89])
print(subjects * 3)

print(len(subjects))
subjects.append(100) # sese value add korara jonno
print(subjects)
print(len(subjects))
subjects.insert(2,'hhh') # mon moto jaygay value add korara jonno
print(subjects)
print(len(subjects))
subjects.remove(100) # mon moto value remove korar jonno
print(subjects)
subjects.sort() # list k abc akare sajanor jonno.
subjects.reverse() # list ta ses theke dekhanor jonno
subjects.pop() # seser value remove korar jonno
subjects.clear() # list clear korar jonno.
sub = subjects.copy()
print(sub)
print(subjects.index('c')) #kono value ar index dekhar jonno
print(subjects.count('c'))
print(subjects) """

# range (akta range a number genarate korar jonno)
""" num = list(range(5,11,2)) # suru , ses +1 , bebodan
print(num)
print(num[2]) """

# for loop
num = [10, 20, 30, 40, 50]
""" index = 0
n = len(num)
while index<n:
    print(num[index])
    index = index + 1 """
""" sum = 0
for x in num:
    sum = sum + x
    print(x)
    print(sum) """

# serics
""" #1+2+3+....+n
n = 5
sum = 0
for x in range(1,n+1,1):
    sum = sum + x
print(sum) """

""" #1+3+5+....+n
n = 5
sum = 0
for x in range(1,n+1,2):
    sum = sum + x
print(sum) """

""" #1*1+2*2+3*3+....+n
n = 5
sum = 0
for x in range(1,n+1,1):
    sum = sum + x*x
print(sum) """

""" #1*2*3*....*n
n = 5
sum = 1
for x in range(1,n+1,1):
    sum = sum *x
print(sum) """

#molik songkha, gosagu, losagu, factorial koro

# *
# **
# ***
# ****
""" n = 3
for x in range(n+1):
    print(x * '* ') """

# guessing 
""" from random import randint
for x in range(1,6):
    guessNumber = int(input("Enter your Guess between 1 to 5 : "))
    randomNumber = randint(1,5)
    if guessNumber == randomNumber:
        print('You have won')
    else:
        print('You have lost')
        print('random number was : ', randomNumber) """

# list as input user
""" n = input("Enter a text of number : ")
list = n.split() #  sob gulo value k alada korart jonno
sum = 0
for num in list:
    sum = sum + int(num)
print(sum) """

# letter gonona kora --- anisul islam 30

