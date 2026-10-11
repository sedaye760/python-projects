Weight=float(input("Enter your weight in kq:"))
Height=float(input("Enter your height in meters:"))
BMI= Weight / (Height**2)
print("Your BMI is:",round(BMI,2))

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal weight")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")