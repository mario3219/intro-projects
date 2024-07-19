def calculate_avg_temp(list):
    if len(list) == 0:
        return 0
    sum = 0
    length = 0
    for x in list:
        sum += x
        length += 1
    return sum/length

def when_is_spring(temp_list):

    #ska hitta indexet i temperatur_data.csv då våren börjar. Gör detta genom att kolla om temperaturen i 7
    #efter varandra följande dagar är över 0. Om sant, returnerar indexet.

    #obs att jämförelse med temperatur_data.csv så ska idx som returneras adderas med 3 för att få ut rätt datum
    #pga rubriker i rad 1, så rad 2 blir index 0, dvs 3 index hoppas över när listan används som parameter i funktionen
    
    first_found = False #?? var bara med i uppgiften att det ska nyttjas
    n = 0 #håller koll på hur många följande dagar över 0 som hittats hitills

    #kollar att listan inte är tom
    if len(temp_list) == 0:
            return -1
    
    #returnerar -1 om listan innehåller bara nollor
    for idx, x in enumerate(temp_list):
         if temp_list[idx] != 0:
            break
         elif idx == len(temp_list)-1:
             return -1

    #kollar när våren börjar
    for idx, x in enumerate(temp_list):
        if temp_list[idx] > 0.0:  
            n += 1
            if n == 7:
                return idx-6
        else:
            n = 0