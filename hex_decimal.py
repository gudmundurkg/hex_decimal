""""
Höfundur: Guðmundur Kristján

Forrit sem gerir notanda kleift að varpa
hex tölu yfir í tugatölu og öfugt.
"""

# Valseðill notanda
def display_menu():

    print("\nd. Decimal to hex")
    print("h. Hex to decimal")
    print("x. Exit\n")

    
# Decimal -> Hex_str
def decimal_to_hex_str(dec_int):
    # Ítrum yfir inputtið og vistum sem streng
    created_hex_str = ""
    while dec_int != 0:
        remainder = dec_int % 16
        dec_int = dec_int // 16
        remainder_str = str(hex_str_to_proper_hex(remainder))
        created_hex_str += remainder_str
    created_hex_str = created_hex_str[::-1]
    return created_hex_str

# Hex_str er gefið rétt nafn skv. Hex kerfi
def hex_str_to_proper_hex(hex_str):
    if (hex_str == 0):
        hex_str = 0
    elif (hex_str < 10):
        hex_str = hex_str
    elif (hex_str == 10):
        hex_str = ("A")
    elif (hex_str == 11):
        hex_str = ("B")
    elif (hex_str == 12):
        hex_str = ("C")
    elif (hex_str == 13):
        hex_str = ("D")
    elif (hex_str == 14):
        hex_str = ("E")
    elif (hex_str == 15):
        hex_str = ("F")
    return hex_str

# Hex_string breytt í Decimal tölu
def hex_str_to_decimal(hex_str):

    try:
        decimal = int(hex_str, 16)
        return decimal
    except: # Skilar None ef input er ekki Hex gildi
        result = None
        return result

# Aðalfall
def main():
    user_choice = ("")
    while user_choice != ("x"):
        display_menu()
        user_choice = input("Enter option: ")
        if user_choice == "d":
            chosen_decimal = int(input("Decimal number: "))
            hex_string = decimal_to_hex_str(chosen_decimal)
            print(f"The hex is {hex_string}")    
        elif user_choice == "h":
            # Leyfum upper og lower gildi í chosen_hex:
            chosen_hex = input("Hex number: ") 
            chosen_hex_lower = chosen_hex.lower()
            converted_int = hex_str_to_decimal(chosen_hex_lower)
            print(f"The decimal is {converted_int}")
        elif user_choice == "x":
            return None
        else:
            print("Invalid option!")

# Aðalforrit:
if __name__ == "__main__":
    main()