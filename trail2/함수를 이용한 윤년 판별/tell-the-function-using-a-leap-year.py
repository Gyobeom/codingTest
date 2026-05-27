y = int(input())

# Please write your code here.
def checkYear(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
if checkYear(y):
    print('true')
else:
    print('false')