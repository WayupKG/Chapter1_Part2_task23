def intercalary():
    year = int(input())
    if year % 4 != 0:
        print("обычный год")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("високосный год")
        else:
            print("обычный год")
    else:
        print("високосный год")
intercalary()