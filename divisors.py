PickaNumber = int(input('Please pick a number:'))
print(PickaNumber)
print(type(PickaNumber))
x=range(1,PickaNumber)
for num in x:
    if PickaNumber % num == 0:
        print (num)