PickaNumber = int(input('Pick a number:'))
# print(PickaNumber)
# print(type(PickaNumber))
x=range(1,PickaNumber)
answers=[]
for num in x:
    if PickaNumber % num == 0:
        answers.append(num)
print('The numbers divisable by',PickaNumber, 'is ', PickaNumber, 'and', tuple(answers))