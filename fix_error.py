def spam():
    eggs = 'spam local'
    eggs = 'global'
    print(eggs)

spam()
print(spam) # ERROR!
#print(spam) # ERROR!

