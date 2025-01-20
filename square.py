n = int(input("enter the number:"))
for i in range(n):
    num = float(input("enter number {}: ".format(i+1)))
    print("square of {} is:{}".format(num, num ** 2))
