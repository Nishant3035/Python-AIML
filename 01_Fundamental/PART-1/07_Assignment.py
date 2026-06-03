""""Ask the user for a temperature in Celsius (string input). Convert it to ,
then calculate and print temperature in Fahrenheit

Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) +32"""

celsius =str(input("Enter the value "))

celsius=float(celsius)
fahrenheitTemp = (celsius*(9/5))+32

print(float(fahrenheitTemp))