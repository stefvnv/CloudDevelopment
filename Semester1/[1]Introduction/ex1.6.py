def main():
    gross = float(input('Enter your gross pay: '))
    paye = gross * 0.25
    prsi = gross * 0.12
    usc = gross * 0.10
    sub = 34.56
    net = gross - paye - prsi - usc - sub
    print('\nEmployee Payslip')
    print('------------------')
    print('Gross Pay =€{0:,.2f}'.format(gross))
    print('PAYE =€{0:,.2f}'.format(paye))
    print('PRSI =€{0:,.2f}'.format(prsi))
    print('USC =€{0:,.2f}'.format(usc))
    print('Union Sub =€{0:,.2f}'.format(sub))
    print('------------------')
    print('\tNet Pay=€{0:,.2f}'.format(net))

main()
