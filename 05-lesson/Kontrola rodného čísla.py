def normalize(birth_number): # — odstraní lomítko a mezery, vrátí řetězec 10 číslic, nebo None, pokud vstup nemá správný tvar,
    birth_number = birth_number.replace(" ","")
    birth_number = birth_number.replace("/","")
    if birth_number.isdigit() and len(birth_number) == 10:
        return birth_number
    else:
        return

def is_valid(birth_number): # — ověří tvar, dělitelnost 11 a platnost měsíce,
    platnost_mnesice = False
    mnesice = birth_number[2]
    mnesice += birth_number[3]


    if 50 <= int(mnesice) <= 62 or 0 <= int(mnesice)<= 12:
        platnost_mnesice = True

    if int(birth_number) % 11 == 0 and platnost_mnesice == True:
        return True
    else:
        return False


def gender(birth_number): # — vrátí "muž" nebo "žena",
    mnesice = birth_number[2]
    mnesice += birth_number[3]

    if int(mnesice) > 49 :
        return "žena"
    else:
        return "můž"
    
def birth_date(birth_number): # — vrátí datum narození jako řetězec.
    day = birth_number[4]
    day += birth_number[5]
    day = int(day)

    month = birth_number[2]
    month += birth_number[3]
    month = int(month)

    year = birth_number[0]
    year += birth_number[1]
    year = int(year)
    if year >= 54:
        year = year + 1900
    else:
        year = year + 2000

    birth = f"{day:00d}. {month:00d}. {year}"
    
    return birth 

print(birth_date(normalize("736028/5163")))


