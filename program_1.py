# Eliya Statema
# 2/20/25
# Kilometer Converter

def convert_to_miles():
    kilometers = float(input("Enter a distance in kilometers: "))
    miles = kilometers * 0.6214
    return miles

print("The distance in miles is", convert_to_miles())