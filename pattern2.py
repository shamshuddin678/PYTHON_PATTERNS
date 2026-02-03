def pattern2(n):
    for i in range(n):
        for j in range(i):
            print("*",end=" ")
        print()    
pattern2(5)

'''
DRY RUN:
n=5
i=0: j=0 to 0 -> *
i=1: j=0 to 1 -> * *
i=2: j=0 to 2 -> * * *
i=3: j=0 to 3 -> * * * *
i=4: j=0 to 4 -> * * * * * 
'''          