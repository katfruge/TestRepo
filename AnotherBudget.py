income = float(input('What is your monthly income?\n '))
print('Your total income next month will be: ' +str(income))
#Since I'm using the 50-20-30 budget rule, the income is automtically reduced by 50% to account for the 'needs' portion of the budget
spending = income * 0.5

#I want to allow the user a choice in the program
choice = int(input('\nWhat do you want to do?\n1) View overall budget\n2) View spending budget\n'))
#implementing a conditional statement
if choice == 1:
            print('\nYour overall budget this month is: $', str(income))
elif choice == 2:
            print('\nYour spending budget this month is: $', str(spending))
else:
            quit
#any other integer but 1 or 2 will cause the program to continue

option = int(input('\nHow much do you want to save?\n1) 20%\n2) 30%\n'))
if option ==1:
            self_savings = 0.20
elif option ==2:
            self_savings = 0.30
else:
            quit
    
#raising a NameError in the case that savings or self_savings is not defined due to user input error above 
try:
    savings = spending * self_savings
except NameError:
    print("Error: Incorrect integer entered has caused 'savings' value to be undefined. Rerun program and enter a valid integer.")

print('\nYour total savings this month are: $', str(savings))

#defining my gather expenses function
def gather_expenses():
    rent = float(input('\nEnter your monthly rent: '))
    utilities = float(input('Enter your monthly utilities costs: '))
    food = float(input('Enter your monthly food costs: '))
    other = float(input('Enter any other monthly costs you incur: '))
    expenses = rent + utilities + food + other
    #returning the result to the caller, gather_expenses()
    return expenses

#equating the two values
expenses = gather_expenses()
print('Your total expenses next month will be '+str(expenses))

#the margin will make up the 20% or 30% that can be spent based upon user input
margin = income - expenses - savings
if margin >= 0:
    print('Your spending budget will be $' + str(margin))
elif margin ==0:
    print('You have no spending budget!')
else:
    print('You are in the negative $' + str(margin))

#creating a class to put the information in
class Budget(object):
    def __init__(self, income, expenses, savings, margin):
        self.income = income
        self.expenses = expenses
        self.savings = savings
        self.margin = margin
        
#budget summary
print('\nYour budget summary is:\n')
print('Income: $' +str(income))
print('Expenses: $' +str(expenses))
print('Savings: $' +str(savings))
print('Spending Budget: $' +str(margin))