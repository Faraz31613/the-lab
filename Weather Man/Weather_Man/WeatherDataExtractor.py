from types import new_class
from DayWeather import DayWeather
import os
import csv


class WeatherDataExtractor:
    def year_data_extractor(file_path, year, months_list):
        # no of files exits
        file_paths = []

        # counter for loop a complete year
        month_counter = 0
        while(month_counter < 12):
            file_name = f'{file_path}_{year}_{months_list[month_counter]}.txt'

            if os.path.isfile(file_name):
                file_paths.append(file_name)

            month_counter = month_counter+1

        if len(file_paths) == 0:
            print("No record exists for this year, Try another year!")
            return
        else:
            year_data = {}
            i = 0
            month = months_list[i]
            for x in range(len(file_paths)):
                month_data = []
                with open(file_paths[x]) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0:
                            pass
                            line_count += 1
                        else:
                            day_data = DayWeather(row)
                            month_data.append(day_data)
                            line_count += 1
                    while month not in file_paths[x]:
                        i = i+1
                        month = months_list[i]
                    year_data[month] = month_data
            return year_data

    def month_data_extractor(file_path, year, month):

        file_name = f'{file_path}_{year}_{month}.txt'
        if not os.path.isfile(file_name):
            print("No record exists for this month, Try another month!")
            return
        else:

            month_data = []
            with open(file_name) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        pass
                        line_count += 1
                    else:
                        day_data = DayWeather(row)
                        month_data.append(day_data)
                        line_count += 1
                month_weather_data = {}
                month_weather_data[month] = month_data
        return month_weather_data
