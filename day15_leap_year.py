# Create a program that checks if a year is a leap year.
import calendar
def is_leap_year(year: int):
    # rule is % 4 but not % 100 but also % 400
    # python has a calendar module actually
    # return calendar.isleap(year)
    # BC? super intereting: https://www.reddit.com/r/AskHistory/comments/ll1o6n/are_there_leap_years_in_bc/
    # there were no leap years in BC because it was a mess with leap months etc.
    # then Julian did leap year but it accumulated 11 extra days because the year is not 265.25 but like 365.24
    # and orthodox church refused to give back those 10 days :-D
    if not isinstance(year, int):
        print('year must be integer')
        return None
    if year < 1:
        print('there are only leap years in AD')
        return None
    else:
        return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

if __name__=="__main__":
    try:
        year = int(input('enter year:'))
        print('leap') if is_leap_year(year) else print('not leap') #it still prints if None is returned
    except ValueError:
        print('year must be integer')
