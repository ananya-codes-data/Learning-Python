# simple interest
# final value = principle + interest earned
# interst earned = principal x roi x time
# final value = principal + (principal x roi x time)
# final value = principal(1 + rt)

# compund interest
# final value = principal + (principal x roi)** time
# final value = principal(1 + r)**time

# componding frequency 

# final value = principal*(1 + (r/compounding frequency))**(time*compounding frequency)



principal = float(input("enter your principal amount: "))

if principal < 0:
    print("negative value not allowed")
else:
    roi = float(input("what's the annual interest rate: "))
    if roi < 0:
        print("negative roi not acceptable")
    else:
        time = int(input("how many years is the principal invested: "))
        if time <= 0:
            print("zero or negative value not allowed")
        else:
            compounding_frequency = int(input("what's the compounding freqency? 1- Annually, 2- Half-yearly, 3- Quarterly, 4- Monthly:"))
            if compounding_frequency == 4:
                final_amount = round(principal*(1 + ((roi/100)/ 12))**(time * 12), 2)
            elif compounding_frequency == 3:
                final_amount = round(principal*(1 + ((roi/100)/ 4))**(time * 4), 2)
            elif compounding_frequency == 2:
                final_amount = round(principal*(1 + ((roi/100)/ 2))**(time * 2), 2)
            else:
                final_amount = round(principal*(1 + ((roi/100)))**time, 2)
            interest_earned = round(final_amount - principal, 2)
            print(f"the final amount is: {final_amount}")
            print(f"the total interest earned is: {interest_earned}")