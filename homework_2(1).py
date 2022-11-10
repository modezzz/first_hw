def leap_year_cacl():
    """Function for compute leap year"""
    year = int(input('Enter a year in digits format: '))
    if len(str(year)) == 4:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('Incorrect format of year.')


leap_year_cacl()


