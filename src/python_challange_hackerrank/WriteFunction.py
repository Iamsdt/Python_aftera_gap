y = 2013

if y % 4 == 0:
    if y % 100 != 0 or y % 400 == 0 :
        print("leap2")
    else:
        print("@@@@nleap")

else:
    print("Not leap")
