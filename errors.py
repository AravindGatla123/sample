# compile error, logical , run time

a = 5
b = 2

try:
    print("resorce open")
    print(a/b)
    k = int(input("enter any value : "))
    print(k)
except ZeroDivisionError as e:
    print("Hey you can't divide a number by Zero:", e)

except ValueError as e:
    print("Invalid error:")

except Exception as e:
    print("Something when wrong")

finally:
    print("close resoure")

print("bye")