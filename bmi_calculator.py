
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height**2)

if BMI < 18.5:
    print("Your BMI is {}, you are underweight.".format(BMI))
elif 18.5 < BMI < 25:
    print("Your BMI is {}, you have a normal weight.".format(BMI))
elif 25 < BMI < 30:
    print("Your BMI is {}, you are slightly overweight.".format(BMI))
elif 30 < BMI < 35:
    print("Your BMI is {}, you are obese.".format(BMI))
elif  BMI > 35:
    print("Your BMI is {}, you are clinically obese.".format(BMI))
