# if else program in python exercises: BMI score
weight= float(input( "Enter your weight (in kilograms): "))
height = float(input( "Enter your height (in meters): "))
bmi = weight / (height ** 2)
if bmi <18.5:
    print ( "Underweight")
elif 18.5 <= bmi <24.9:
    print ( "Normal weight")
elif 25 <= bmi <29.9:
    print ( "Overweight")
else:
    print("Obese")