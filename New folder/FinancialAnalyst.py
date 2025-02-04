Expense = {}
budget = 0
while True:
    print("\n    ---welcome to the Financial Analyst---\n")
    print("1- Add Income")
    print("2- Add Expenses")
    print("3- View Summry")
    print("4- Quit")
    choise = int(input("\nEnter your choise: "))
    while choise < 1 or choise > 4:
        print("Please enter a valid option (1, 2, 3, 4)")
        choise = int(input("\n Enter your choice: "))
    
    
    if choise == 1:
        budget = int(input("\nplease enter your income: "))
        print("\nincome added successfully")
    while choise == 2:
        Ex = input("enter the Expenses when done type 'done': ").lower()
        if Ex == 'done':
            print("\nExpense added successfully")
            break
        Val = int(input("enter the Value: "))
        Expense[Ex] = Val
    if choise == 3 :
        for i ,(keys,value) in enumerate(Expense.items(), start=1):
            print(i,'-',keys,value)
        for i in Expense:
            i = sum(Expense.values())
        print(f"\n\nThe total The total Expenses are {i}")
        print(f"\nThe Result is {budget-i}")
    if choise == 4:
        break
    

        







