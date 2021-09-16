""""
Forrit sem gerir notanda kleift að varpa
hex tölu yfir í tugatölu og öfugt.
"""
#Útfærslan verður að samanstanda af eftirfarandi föllum:
    #def decimal_to_hex(dec_int)
        #Skila hex streng sem samsvarar gefinni tugatölu
    #hex_str_to_decimal(hex_str)
        #Skila tugatölu sem samsvarar gefnum hex streng
    #display_menu()
        #Birti valmöguleika


#Aðalfall
def main():
    display_menu()

#Decimal -> Hex
def decimal_to_hex(dec_int):
    print("Here is your hex")

#Hex to Decimal
def hex_str_to_decimal(hex_str):
    print("Here is your decimal")

#Display Menu
def display_menu():
    print("d. Decimal to hex")
    print("h. Hex to Decimal")
    print("x. Exit\n")

    user_choice = input("Enter option:")
    if user_choice == "d":
        chosen_decimal = int(input("Decimal number: "))
        decimal_to_hex(chosen_decimal)
    elif user_choice == "h":
        hex_str_to_decimal()
    elif user_choice == "x":
        return None




# Main program starts here
if __name__ == "__main__":
    main()