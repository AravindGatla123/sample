pos = -1


def search(list,n):
    i = 0
    while 1<len(list):
        if list[i] == n:
          globals()  ['pos'] = i
          return True
        i = i+1
    return False


list = [5,8,7,6,3,4,2]
n = int(input("please enter value:"))

if search(list,n):
    print("found at ", pos+1)
else:
    print("not found")