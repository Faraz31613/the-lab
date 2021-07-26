from datetime import datetime


class ResultCaluculator():
    def __init__(self):
        self.highest_temp_in_year = None
        self.lowest_temp_in_year = None
        self.highest_humidity_in_year = None

    def calculate_highest_temp_in_year(self, max_temp_list=[], date_list_of_year=[]):
        
        #counter for passing empty values
        counter=0
        while max_temp_list[counter]=='':
            counter=counter+1
        max_temp = int(max_temp_list[counter])
        date_index = 0
        for i in range(1, len(max_temp_list)):
            if max_temp_list[i]=='':
                pass
            elif(int(max_temp_list[i]) > max_temp):
                max_temp = int(max_temp_list[i])
                date_index = i

        date_separator = date_list_of_year[date_index].split("-")
        date_converted = datetime(int(date_separator[0]), int(
            date_separator[1]), int(date_separator[2]))
        month_day = (date_converted.strftime("%B %d"))

        highest_temp = ("Highest: {}C on {}".format(max_temp, month_day))
        self.highest_temp_in_year = highest_temp

    def calculate_lowest_temp_in_year(self, min_temp_list=[], date_list_of_year=[]):
        #counter for passing empty values
        counter=0
        while min_temp_list[counter]=='':
            counter=counter+1
        min_temp = int(min_temp_list[counter])
        date_index = 0
        for i in range(1, len(min_temp_list)):
            if min_temp_list[i]=='':
                pass
            elif(int(min_temp_list[i]) < min_temp):
                min_temp = int(min_temp_list[i])
                date_index = i

        date_separator = date_list_of_year[date_index].split("-")
        date_converted = datetime(int(date_separator[0]), int(
            date_separator[1]), int(date_separator[2]))
        month_day = (date_converted.strftime("%B %d"))

        lowest_temp = ("Lowest: {}C on {}".format(min_temp, month_day))
        self.lowest_temp_in_year = lowest_temp

    def calculate_max_humidity_in_year(self, max_humidity_list=[], date_list_of_year=[]):
        #counter for passing empty values
        counter=0
        while max_humidity_list[counter]=='':
            counter=counter+1
        max_humidity = int(max_humidity_list[counter])
        date_index = 0
        for i in range(1, len(max_humidity_list)):
            if max_humidity_list[i]=='':
                pass
            elif(int(max_humidity_list[i]) > max_humidity):
                max_humidity = int(max_humidity_list[i])
                date_index = i

        date_separator = date_list_of_year[date_index].split("-")
        date_converted = datetime(int(date_separator[0]), int(
            date_separator[1]), int(date_separator[2]))
        month_day = (date_converted.strftime("%B %d"))

        highest_humidity = (
            "Humidity: {}'%' on {}".format(max_humidity, month_day))
        self.highest_humidity_in_year = highest_humidity
