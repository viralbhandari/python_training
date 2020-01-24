def main():
    try:
        hours=int(input('how many hours did you work?'))
        pay_rate=float(input('Enter your hourly pay rate'))
        gross_pay=hours*pay_rate
        print('gross pay:=',format(gross_pay,',.2f'),sep='')
    except ValueError:
        print('ERROR:Hours worked & hourly pay must')
        print('be valid numbers')
main()
