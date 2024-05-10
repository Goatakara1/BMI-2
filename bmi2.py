height = float(input("Enter your height in meter.\n "))
weight = int(input("Enter your weight in kilogram.\n "))

bmi = weight / (height * height)

bmi_rounded = round(bmi,2)

if bmi < 18.5:
    print(f"Your bmi is {bmi_rounded}, you are underweight.")
elif bmi <  25:
    print(f"Your bmi is {bmi_rounded}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi_rounded}, you are slightly overveight.")
elif bmi < 35:
    print(f"Your bmi is {bmi_rounded}, you are obese.")
else:
    print(f"Your bmi is {bmi_rounded}, you are clinically obese.")
  