n=int(input("enter a number:"))
i=2
if n<0:
    ptint("negative number")
else:
    if n<2:
        print("the no. is not a prime no.")
    elif n>2:
        while n>i:
            if n%i==0:
                print("the no. is not a prime no.")
                break
            i=i+1
        else:
            print("the no. is a prime no.")
    else:
        print("the no. is a prime no.")