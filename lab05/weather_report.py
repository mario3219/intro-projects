from pathlib import Path
import file_reader 

# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'

#read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 2)
avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)

def calculate_avg_temp(list):
    sum = 0
    length = 0
    for x in list:
        sum += x
        length += 1
    return sum/length

avg_temp = calculate_avg_temp(temp_list)
print(avg_temp)