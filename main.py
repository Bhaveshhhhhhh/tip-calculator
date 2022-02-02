print("Welcome to the tip calculator!~")
totalbill = float(input("Enter the total bill amount:\n"))
per = int(input("enter the tip percenatage 10 12 13:\n"))
person = int(input("how many people to didvid the bill:\n"))
total_bill = per / 100 * totalbill + totalbill
print(f"the total bill is: \n{total_bill}")
m  = total_bill / person
j =(round(m,2))
print(f"each perrson will pay\n{j}")