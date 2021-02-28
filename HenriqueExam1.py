# Henrique Medeiros dos Reis
# Henrique Exam 1
# 9/17/2018

# Variables
pay = 0.0
total = 0.0
sales = 0.0
average = 0.0
days = 0
counter = 0

days = int(input('Enter the number of days: '))
while days <= 0:
    int(input('Days must be greater than zero. Please try again: '))
for i in range(counter, days, 1):
    sales = float(input('Enter the daily sales: '))
    while sales <= 0:
        float(input('Daily sales must be greater than zero. Please try again: '))
    total += sales
# Math
average = total / days
pay = total / 100 * 10

print('Avarege sales:  $',format(average, ',.2f'))
print('Total Sales:    $',format(total, ',.2f'))
print("Salesperson's payment:  $",format(pay, ',.2f'))
