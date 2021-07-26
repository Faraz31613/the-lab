import os
import sys

from FileReader import FileReader
from ResultCalculator import ResultCaluculator


def main():

    file_name = sys.argv[1]
    months_list = ["Jan", "Feb", "Mar", "Apr", "May",
                   "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    year = sys.argv[3]

    if sys.argv[2] == "-e":
        # no of files exits
        file_paths_list = []

        # counter for loop a complete year
        month_counter = 0
        while(month_counter < 12):
            file_path = ('{}_{}_{}.txt'.format(
                file_name, year, months_list[month_counter]))

            if os.path.isfile(file_path):
                file_paths_list.append(file_path)

            month_counter = month_counter+1

        data_obj = FileReader()
        if len(file_paths_list) == 0:
            print("No record exists for this year, Try another year!")
        else:
            # filled the data of the year give
            data_obj.data_filler(file_paths_list)

            # list for only max temperature of all tha days of the year
            highest_temp_list = []
            highest_temp_list = data_obj.max_temperature_c

            # list for only min temperature of all tha days of the year
            lowest_temp_list = []
            lowest_temp_list = data_obj.min_temperature_c

            # list for only max humidity of all tha days of the year
            highest_humidity_list = []
            highest_humidity_list = data_obj.max_humidity

            # list for only all the dates of the year
            date_list_of_year = data_obj.pkt

            result_calculator_obj = ResultCaluculator()
            result_calculator_obj.calculate_highest_temp_in_year(
                highest_temp_list, date_list_of_year)
            result_calculator_obj.calculate_lowest_temp_in_year(
                lowest_temp_list, date_list_of_year)
            result_calculator_obj.calculate_max_humidity_in_year(
                highest_humidity_list, date_list_of_year)

            print(result_calculator_obj.highest_temp_in_year)
            print(result_calculator_obj.lowest_temp_in_year)
            print(result_calculator_obj.highest_humidity_in_year)


main()
