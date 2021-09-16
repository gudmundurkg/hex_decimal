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
        #Birtir valmöguleika


#Aðalfall
def main():
    display_menu()

#Decimal -> Hex
def decimal_to_hex(dec_int):
    user_num = dec_int

    remainder_list = []
    final_list = []
    result = user_num

    #Söfnum afgöngum frá floor deilingu í lista 
    while result != 0:
        remainder = result % 16
        result = result // 16
        remainder_list.append(remainder)

    #Gefum tölum í lista heiti skv. Hex kerfi
    for item in remainder_list:
        if (item == 0):
            final_list.append(0)
        elif (item < 10):
            final_list.append(item) 
        elif (item == 10):
            final_list.append("A")
        elif (item == 11):
            final_list.append("B")
        elif (item == 12):
            final_list.append("C")
        elif (item == 13):
            final_list.append("D")
        elif (item == 14):
            final_list.append("E")
        elif (item == 15):
            final_list.append("F")

    #Reversum lista og prentum án bils/hornklofa        
    final_list.reverse()
    print("The hex is: ",*final_list, sep='')
    print()
    main()

#Hex to Decimal
def hex_str_to_decimal(hex_str):

    user_hex = hex_str

    decimal = int(user_hex, 16)

    print(f"Decimal number: {decimal}")
    main()


#Display Menu
def display_menu():
    print()
    print("d. Decimal to hex")
    print("h. Hex to decimal")
    print("x. Exit\n")

    user_choice = input("Enter option: ")
    if user_choice == "d":
        chosen_decimal = int(input("Decimal number: "))
        decimal_to_hex(chosen_decimal)
    elif user_choice == "h":
        chosen_hex = input("Hex number:")
        hex_str_to_decimal(chosen_hex)
    elif user_choice == "x":
        return None

# Main program starts here
if __name__ == "__main__":
    main()