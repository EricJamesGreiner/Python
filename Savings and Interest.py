'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.09

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  
while i <= years:
    print(f' Savings at beginning of year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)
    i = i + 1 

print('\n')