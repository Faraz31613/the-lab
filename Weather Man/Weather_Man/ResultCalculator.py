from datetime import datetime


class ResultCaluculator():
    def __init__(self):
        self.highest_temp_in_year = None
        self.lowest_temp_in_year = None
        self.highest_humidity_in_year = None

        self.avg_highest_temp_in_month = None
        self.avg_lowest_temp_in_month = None
        self.avg_mean_humidity_in_month = None

        self.monthly_temperature_chart = None

    def calculate_highest_temp_in_year(self, max_temp_list=[], date_list_of_year=[]):

        # counter for passing empty values
        counter = 0
        while max_temp_list[counter] == '':
            counter = counter+1
        max_temp = int(max_temp_list[counter])
        date_index = 0
        for i in range(1, len(max_temp_list)):
            if max_temp_list[i] == '':
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
        # counter for passing empty values
        counter = 0
        while min_temp_list[counter] == '':
            counter = counter+1
        min_temp = int(min_temp_list[counter])
        date_index = 0
        for i in range(1, len(min_temp_list)):
            if min_temp_list[i] == '':
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
        # counter for passing empty values
        counter = 0
        while max_humidity_list[counter] == '':
            counter = counter+1
        max_humidity = int(max_humidity_list[counter])
        date_index = 0
        for i in range(1, len(max_humidity_list)):
            if max_humidity_list[i] == '':
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

    def calculate_avg_highest_temp_in_month(self, max_temp_list=[]):

        sum_of_temp = 0
        counter_for_month = 0
        empty_data_days_count = 0
        while(counter_for_month < len(max_temp_list)):
            if max_temp_list[counter_for_month] == '':
                empty_data_days_count = empty_data_days_count+1
            else:
                sum_of_temp = sum_of_temp + \
                    int(max_temp_list[counter_for_month])
            counter_for_month = counter_for_month + 1
        if empty_data_days_count == len(max_temp_list):
            self.avg_highest_temp_in_month = "No record exists for this month!"
        else:
            average_max_temp = sum_of_temp / \
                (len(max_temp_list)-empty_data_days_count)
            self.avg_highest_temp_in_month = (
                "Highest Average: {}C".format(average_max_temp))

    def calculate_avg_lowest_temp_in_month(self, min_temp_list=[]):

        sum_of_temp = 0
        counter_for_month = 0
        empty_data_days_count = 0
        while(counter_for_month < len(min_temp_list)):
            if min_temp_list[counter_for_month] == '':
                empty_data_days_count = empty_data_days_count+1
            else:
                sum_of_temp = sum_of_temp + \
                    int(min_temp_list[counter_for_month])
            counter_for_month = counter_for_month + 1
        if empty_data_days_count == len(min_temp_list):
            self.avg_lowest_temp_in_month = "No record exists for this month!"
        else:
            average_min_temp = sum_of_temp / \
                (len(min_temp_list)-empty_data_days_count)
            self.avg_lowest_temp_in_month = (
                "Lowest Average: {}C".format(average_min_temp))

    def calculate_avg_mean_humidity_in_month(self, mean_humidity_list=[]):

        sum_of_mean_humidity = 0
        counter_for_month = 0
        empty_data_days_count = 0
        while(counter_for_month < len(mean_humidity_list)):
            if mean_humidity_list[counter_for_month] == '':
                empty_data_days_count = empty_data_days_count+1
            else:
                sum_of_mean_humidity = sum_of_mean_humidity + \
                    int(mean_humidity_list[counter_for_month])
            counter_for_month = counter_for_month + 1
        if empty_data_days_count == len(mean_humidity_list):
            self.avg_mean_humidity_in_month = "No record exists for this month!"
        else:
            average_mean_humidity = sum_of_mean_humidity / \
                (len(mean_humidity_list)-empty_data_days_count)
            self.avg_mean_humidity_in_month = (
                "Average Mean Humidity: {}%".format(average_mean_humidity))

    def draw_monthly_temperature_chart(self, highest_temp_list, lowest_temp_list):
        month_days_counter = 1
        high_temp_chart = ""
        low_temp_chart = ""
        month_chart = ""
        while month_days_counter <= len(highest_temp_list):
            day = (str(month_days_counter)).zfill(2)
            no_record_message = "No record exists for this day!"

            if highest_temp_list[month_days_counter-1] == '':
                high_temp_chart = ("{0} {1}\n".format(day, no_record_message))
            else:
                max_temp_on_day = highest_temp_list[month_days_counter-1]
                max_temp_on_day_chart = ''.ljust(
                    int(max_temp_on_day), '+')
                high_temp_chart = ("\033[1;37;40m{0}\033[1;31;40m {1} {2}C\n".format(
                    day, max_temp_on_day_chart, max_temp_on_day))

            if lowest_temp_list[month_days_counter-1] == '':
                low_temp_chart = ("{0} {1}\n".format(day, no_record_message))
            else:
                min_temp_on_day = lowest_temp_list[month_days_counter-1]
                min_temp_on_day_chart = ''.ljust(
                    int(min_temp_on_day), '+')
                low_temp_chart = ("\033[1;37;40m{0}\033[1;34;40m {1} {2}C\033[0;37;40m\n".format(
                    day, min_temp_on_day_chart, min_temp_on_day))

            day_chart = ("{0}{1}".format(high_temp_chart, low_temp_chart))
            month_chart = month_chart + day_chart
            month_days_counter = month_days_counter+1
        
        self.monthly_temperature_chart = month_chart

    def draw_monthly_temperature_chart_bonus_task(self, highest_temp_list, lowest_temp_list):
        month_days_counter = 1
        high_temp_chart = ""
        low_temp_chart = ""
        month_chart = ""
        while month_days_counter <= len(highest_temp_list):
            day = (str(month_days_counter)).zfill(2)
            no_record_message = "*No record exists for this day!*"
            max_temp_on_day = None
            max_temp_on_day_chart = ""
            min_temp_on_day = None
            min_temp_on_day_chart = ""
            if highest_temp_list[month_days_counter-1] == '':
                high_temp_chart = ("{0}".format(no_record_message))
            else:
                max_temp_on_day = highest_temp_list[month_days_counter-1]
                max_temp_on_day_chart = ''.ljust(
                    int(max_temp_on_day), '+')
                # high_temp_chart = ("\033[1;31;40m{0} {1} {2}C\n".format(
                #     day, max_temp_on_day_chart, max_temp_on_day))

            if lowest_temp_list[month_days_counter-1] == '':
                low_temp_chart = ("{0}".format(no_record_message))
            else:
                min_temp_on_day = lowest_temp_list[month_days_counter-1]
                min_temp_on_day_chart = ''.ljust(
                    int(min_temp_on_day), '+')
                # low_temp_chart = ("\033[1;34;40m{0} {1} {2}C\033[0;37;40m\n".format(
                #     day, min_temp_on_day_chart, min_temp_on_day))

            if highest_temp_list[month_days_counter-1] != '' and lowest_temp_list[month_days_counter-1] != '':
                day_chart = ("{0} \033[1;34;40m{2}\033[1;31;40m{1}\033[0;37;40m {4}C-{3}C\n".format(day,max_temp_on_day_chart, min_temp_on_day_chart,max_temp_on_day,min_temp_on_day))
                month_chart = month_chart + day_chart
            elif highest_temp_list[month_days_counter-1] == '' and lowest_temp_list[month_days_counter-1] != '':
                day_chart = ("{0} \033[1;31;40m{1}\033[1;34;40m{2}\033[0;37;40m {3}-{4}\n".format(day,high_temp_chart, min_temp_on_day_chart,"No Min Record",min_temp_on_day))
                month_chart = month_chart + day_chart
            elif highest_temp_list[month_days_counter-1] != '' and lowest_temp_list[month_days_counter-1] == '':
                day_chart = ("{0} \033[1;31;40m{1}\033[1;34;40m{2}\033[0;37;40m {3}-{4}\n".format(day,max_temp_on_day_chart, low_temp_chart,max_temp_on_day,"Max"))
                month_chart = month_chart + day_chart
            else:
                day_chart = ("{0} \033[1;31;40m{1}\033[1;34;40m{2}\033[0;37;40m {3}-{4}\n".format(day,high_temp_chart, low_temp_chart,"Min","Max"))
                month_chart = month_chart + day_chart
            month_days_counter = month_days_counter+1
        
        self.monthly_temperature_chart = month_chart
