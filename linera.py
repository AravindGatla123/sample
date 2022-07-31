def search(list,n):
     for i in len(list):
         if list[i] == n:
             globals()['pos'] =1
             return True

     return False


list = [3,5,4,7,8,1]
n = 1
if search(list,n):
    print("found")
else:
    print("not found")