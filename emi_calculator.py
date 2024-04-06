p = float(input("Enter the Principal amount:"))
r = float(input("Enter the annual rate of interest:"))
n = int(input("Enter the number of month:"))

#converting the rate of intrest from months to year
r = r/(12*100)

emi = p * r * ((1 + r)**n)/((1+r)**n-1)

print(f"Your montly EMI is: {round(emi, 2)}")