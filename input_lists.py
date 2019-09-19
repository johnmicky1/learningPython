#In this type of lists you are abble to input limitless data:
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
###The benefit of using a list is that your data is now in a structure, so your
#program is much more flexible in processing the data than it would be with
#several repetitive variables.