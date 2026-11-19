def convert(value, from_unit, to_unit):
    celsies = 0
    if from_unit == "C":
        celsies = value
    elif from_unit == "F":
        celsies = (value-32)/1.8
    elif from_unit == "K":
        celsies = value - 273.15
    else:
        print("error")
        return

    output = 0
    if to_unit == "C":
        output = celsies
    elif to_unit == "F":
        output = (celsies*9/5)+32
    elif to_unit == "K":
        output = celsies + 273.15
    else:
        return "error"
    return output


print(convert(100, "C", "F"))
print(convert(0, "K", "C"))
print(convert(-40, "C", "F"))
print(convert(20, "C", "X"))
    