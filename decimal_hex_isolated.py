

user_num = input("Input a number")

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
print(*final_list, sep='')