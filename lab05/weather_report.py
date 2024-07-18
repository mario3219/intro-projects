from pathlib import Path
import file_reader 

# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'

#read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 2)
