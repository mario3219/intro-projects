from pathlib import Path
import file_reader 
import weather_functions

# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'

#read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 2)
#avg_temp = sum(temp_list)/len(temp_list)
#print(avg_temp)
#print(temp_list)

avg_temp = weather_functions.calculate_avg_temp(temp_list)
#print(avg_temp)

temp_list = file_reader.read_from_file(file_path, 0)
spring_idx = weather_functions.when_is_spring(temp_list)
#print(spring_idx)

user_input = input('Vad vill du göra? Tryck 1 för medeltemperatur och 2 för vårens ankomst' + '\n')
if int(user_input) == 1:
    user_input = int(input('Vilken månad vill du beräkna medeltemperaturen för? Ange månadsnummer' + '\n'))
    temp_list = file_reader.read_from_file(file_path, user_input)
    avg_temp = weather_functions.calculate_avg_temp(temp_list)
    print('Medeltemperaturen var ' + str(avg_temp) + ' grader i månad ' + str(user_input))
elif int(user_input) == 2 :
    print('Letar efter våren...' + '\n')
    temp_list = file_reader.read_from_file(file_path, 0)
    spring_idx = weather_functions.when_is_spring(temp_list)
    print('Våren infaller på index ' + str(spring_idx))
