x = ["Aravind", 22, 33,3.5]

for i in x:
    print(i)
for i in range(23,33):
    print(i)
for i in range(1,21):
    if i%5!=0:
     print(i)

## Candy Game-break
av = 10
x = int(input("How many Candys you want?:"))
i  = 1
while i<=x:
    if i>av:
        print("No more candys")
        break
    print("Candy")
    i+=1

print("out of loop")

#continue
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)
print("bye")

#pass
for i in range(1,101):
    if i%2==0:
        pass
    else:
        print(i)
#pattern
for i in range(4):
    for j in range(4):
        print("#",end="")
    print()
for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print()

for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()