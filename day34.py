def isNum():
    while True:
        try:
            n = int(input("Enter number: "))
            print(n)
        except:
            print("Not a number, retry")
isNum()