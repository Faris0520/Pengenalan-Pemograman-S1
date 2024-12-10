def celcius_to_fahrenheit(celcius_float):
    return celcius_float * 1.8 + 32

print("convert celcius to fahrenheit")
celcius_float = float(input("enter a celcius temp: "))
fahrenheit_float = celcius_to_fahrenheit(celcius_float)
print(celcius_float," converts to ", fahrenheit_float, " Fahrenheit")