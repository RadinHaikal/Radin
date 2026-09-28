""" PROGRAMMER NAME: RADIN MUHAMAD FARIS HAIKAL
 PROBLEM DESCRIPTION :  program that asks the user to enter the
monthly usage and then calculates and displays the amount of the bill to be paid
after receiving the discount."""   

monthly_usage = float(input("Enter monthly usage (RM): ")) #input monthly usage
if monthly_usage < 50:
  billPrice = monthly_usage-(monthly_usage*0) #usage less than RM50 per month
    
elif monthly_usage <= 100:
  billPrice = monthly_usage-(monthly_usage*0.05) #usage <= RM100 per month
  
else:
   billPrice = monthly_usage-(monthly_usage*0.20) #usage > RM100 per month
   

print(f"Bill to be paid, RM{billPrice:.2f}")
  

