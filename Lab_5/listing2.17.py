percent_float = float(input("What is your percentage? "))

if 90 <= percent_float < 100:
    print("Kamu mendapat A")
if 80 <= percent_float < 90:
    print("Kamu mendapat B")
if 70 <= percent_float < 80:
    print("Kamu mendapat C")
if 60 <= percent_float < 70:
    print("Kamu mendapat D")
else:
    print("Not good")