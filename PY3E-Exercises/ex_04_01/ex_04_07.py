def computergrade (fs):
    if fs == 10.0:
        print("Bad Score")
        exit()
    elif fs >= 0.9:
        print("A")
        exit()
    elif fs >= 0.8:
        print("B")
        exit()
    elif fs >= 0.7:
        print("c")
        exit()
    elif fs >= 0.6:
        print("d")
        exit()
    elif fs < 0.6:
        print("f")
        exit()

score = input("Enter Score: ")
try:
    fs = float(score)
except:
    print("Bad Score, Enter a number")
    exit()

grade = computergrade(fs)
