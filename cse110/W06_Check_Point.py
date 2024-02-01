

loan_size = float(input("How large is the loan? "))

credit_history = float(input("How good is your credit history? "))

income = float(input("How high is your income? "))

down_payment = float(input("How large is your down payment? "))

if loan_size >= 5:
    if credit_history  >= 7 and income >= 7:
        print("Yes")
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            print("Yes")
        else:
            print("No")
    else:
        if credit_history < 7 or income < 7:
             print("No")
else:
    if loan_size < 5:
        if credit_history < 4:
            print("No")
        else:
            if down_payment >= 7 or income >= 7:
                print("Yes")
            elif down_payment >= 4 and income >= 4:
                print("Yes")
            else:
                print("No")
'''
•»First, check if the loan size is at least 5. If it is, use the following rules:


◦»If the credit history and income are both at least 7, then the decision is "yes"


◦»If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"


◦»Otherwise (if neither the credit history nor income is at least 7), the decision is "no"


•»Otherwise (if the loan is not 5 or greater), use these rules:


◦»If the credit is less than 4, then the decision is "no"


◦»Otherwise, check the following:


◾»If either the income or the down payment is at least 7, the decision is "yes"


◾»If both the income and the down payment are at least 4, then the answer is "yes"


◾»Otherwise, the decision is "no"


Finally, display the decision to the user.
'''









