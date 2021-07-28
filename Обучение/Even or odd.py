def even_odd(a):
    if a % 2 == 0:
        print(str(a) + " is even number")
    else:
        print(str(a) + " is an odd number")

print("Enter your number:")
even_odd(int(input()))