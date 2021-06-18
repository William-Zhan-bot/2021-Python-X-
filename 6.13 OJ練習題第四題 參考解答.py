# 格里曆閏年規則如下： 西元年份除以4不可整除，為平年。 西元年份除以4可整除，
# 且除以100不可整除，為閏年。 西元年份除以100可整除，且除以400不可整除，為平年
month = input()
if month.isdigit():
    month = int(month)
    if month in [1,3,5,7,8,10,12]:
        print(31)
    elif month in [4,6,9,11]:
        print(30)
    elif month == 2:
        year = input()
        if year.isdigit():
            year = int(year)
            if (year%4 == 0 and year%100) != 0 or year%400 == 0:
                print(29)
            else:
                print(28)
        else:
            print("error")
    else:
        print("error")
else:
    print("error")