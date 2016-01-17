# input
name = input("Enter name: ")
hours_worked_weekly = int(input("Enter number of hours worked weekly: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
CPF_contribution_rate = int(input("Enter CPF contribution rate(%): "))

# calculate
gross_pay = hours_worked_weekly * hourly_pay_rate
CPF_contribution = gross_pay * CPF_contribution_rate / 100
net_pay = gross_pay - CPF_contribution

# print
print("Payroll statement for {}".format(name))
print("Number of hours worked in week: {}".format(hours_worked_weekly))
print("Hourly pay rate: ${0:.2f}".format(hourly_pay_rate))
print("Gross pay = ${0:.2f}".format(gross_pay))
print("CPF contribution at {0}% = ${1:.2f}".format(CPF_contribution_rate,CPF_contribution))
print("Net pay = ${0:.2f}".format(net_pay))
