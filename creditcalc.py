import math
import argparse

# write your code here
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

loan = [args.type, args.payment, args.principal, args.periods, args.interest]

args_number = 0

for c in loan:
    if c is not None:
        args_number += 1

if args_number == 4:
    if loan[0] == "diff":
        if loan[1] is not None:
            print("Incorrect parameters")
        elif min(loan[2], int(loan[3]), loan[4]) < 0:
            print("Incorrect parameters")
        else:
            principal = loan[2]
            periods = int(loan[3])
            interest = loan[4] / (12 * 100)
            overpayment = 0
            for month in range(1, periods + 1):
                monthly_payment = principal / periods + interest * (principal - (principal * (month - 1)) / periods)
                monthly_payment = math.ceil(monthly_payment)
                overpayment += monthly_payment
                print(f"Month {month}: payment is {monthly_payment}")
            overpayment -= principal
            print("Overpayment = ", int(overpayment))
    elif loan[0] == "annuity":
        if loan[1] is None:
            if min(loan[2], loan[3], loan[4]) > 0:
                principal = loan[2]
                periods = loan[3]
                interest = loan[4]
                interest = interest / (12 * 100)
                payment = principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)
                payment = math.ceil(payment)
                print(f"Your annuity payment = {payment}!")
                overpayment = payment * periods - principal
                print("Overpayment = ", round(overpayment))
            else:
                print("Incorrect parameters")
        elif loan[2] is None:
            if min(loan[1], loan[3], loan[4]) > 0:
                payment = loan[1]
                periods = loan[3]
                interest = loan[4]
                interest = interest / (12 * 100)
                principal = round(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
                print(f"Your loan principal = {principal}!")
                overpayment = payment * periods - principal
                print("Overpayment = ", round(overpayment))
            else:
                print("Incorrect parameters")
        elif loan[3] is None:
            if min(loan[1], loan[2], loan[4]) > 0:
                principal = loan[2]
                payment = loan[1]
                interest = loan[4]
                interest = interest / (12 * 100)
                periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
                if periods % 12 == 0:
                    if periods // 12 != 1:
                        print(f"It will take {periods // 12} years and to repay this loan!")
                    else:
                        print("It will take 1 year and to repay this loan!")
                elif periods // 12 == 0:
                    if periods % 12 != 1:
                        print(f"It will take and {periods % 12} months to repay this loan!")
                    else:
                        print("It will take and 1 month to repay this loan!")
                else:
                    if periods // 12 != 1 and periods % 12 != 1:
                        print(f"It will take {periods // 12} years and {periods % 12} months to repay this loan!")
                    elif periods // 12 != 1:
                        print(f"It will take {periods // 12} years and 1 month to repay this loan!")
                    elif periods % 12 != 1:
                        print(f"It will take 1 year and {periods % 12} months to repay this loan!")
                    else:
                        print(f"It will take 1 year and 1 month to repay this loan!")
                overpayment = payment * periods - principal
                print("Overpayment = ", round(overpayment))
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
