# #Tip calculator
print('Welcome to the tip calculator!')
total_bill = input('How much was the total bill? (£)\n')
tip = input('How much tip would you like to give? 10, 12 or 15?\n')
split=input('How many people to split the bill?\n')
calculation = round((float(total_bill) * (1+float(tip)/100) / int(split)), 2)
response = f'Each person should pay : £{calculation}'
print(response)