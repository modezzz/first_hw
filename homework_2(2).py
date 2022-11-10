# def leap_year_calc_first():
#     """Function for compute leap year"""
#     coefficients = [4, 400, 100]
#     a, b, c = coefficients
#     year = int(input('Enter a year in digits format: '))
#     print('Yes' if year % a == 0 and year % c != 0 or year % b == 0 else 'No')
#
#
# leap_year_calc_first()
#
#
# def leap_year_calc_second():
#     """Function for compute leap year"""
#     year = int(input('Enter a year in digits format: '))
#     print('Yes' if year % 4 == 0 and year % 400 == 0 else 'No')
#
#
# leap_year_calc_second()


def leap_year_calc_third():
    """Function for compute leap year"""
    year = int(input('Enter a year in digits format: '))
    if bool(year % 4) ^ bool(year % 400) ^ bool(year % 100):
        print('Yes')
    else:
        print('No')


leap_year_calc_third()










