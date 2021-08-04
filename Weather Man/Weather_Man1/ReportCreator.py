import os
import sys

from FileReader import FileExtractor
from ResultCalculator import ResultCaluculator


class ReportCreator:

    def year_report(self, file_name, year, months_list):  # first test case report generator

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

        data_obj = FileExtractor()
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

            print("Yearly Report:\n")
            print(result_calculator_obj.highest_temp_in_year)
            print(result_calculator_obj.lowest_temp_in_year)
            print(result_calculator_obj.highest_humidity_in_year)
            print("End Of Yearly Report\n______________\n")

    def monthly_report(self, file_name, year, month):  # second test case report generator

        # no of files exits
        file_paths_list = []

        # counter for loop a complete year
        file_path = ('{}_{}_{}.txt'.format(
            file_name, year, month))

        if os.path.isfile(file_path):
            file_paths_list.append(file_path)

        data_obj = FileExtractor()
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
            mean_humidity_list = []
            mean_humidity_list = data_obj.mean_humidity

            result_calculator_obj = ResultCaluculator()
            result_calculator_obj.calculate_avg_highest_temp_in_month(
                highest_temp_list)
            result_calculator_obj.calculate_avg_lowest_temp_in_month(
                lowest_temp_list)
            result_calculator_obj.calculate_avg_mean_humidity_in_month(
                mean_humidity_list)

            print("Monthly Report:\n")
            print(result_calculator_obj.avg_highest_temp_in_month)
            print(result_calculator_obj.avg_lowest_temp_in_month)
            print(result_calculator_obj.avg_mean_humidity_in_month)
            print("End Of Monthly Report\n______________\n")

    def monthly_graph(self, file_name, year, month):  # second test case report generator

        # no of files exits
        file_paths_list = []

        # counter for loop a complete year
        file_path = ('{}_{}_{}.txt'.format(
            file_name, year, month))

        if os.path.isfile(file_path):
            file_paths_list.append(file_path)

        data_obj = FileExtractor()
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

            result_calculator_obj = ResultCaluculator()
            result_calculator_obj.draw_monthly_temperature_chart(
                highest_temp_list, lowest_temp_list)

            print("Monthly Chart:\n")
            print(result_calculator_obj.monthly_temperature_chart)
            print("End Of Monthly Chart\n______________\n")

    def monthly_graph_bonus_task(self, file_name, year, month):  # second test case report generator

        # no of files exits
        file_paths_list = []

        # counter for loop a complete year
        file_path = ('{}_{}_{}.txt'.format(
            file_name, year, month))

        if os.path.isfile(file_path):
            file_paths_list.append(file_path)

        data_obj = FileExtractor()
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

            result_calculator_obj = ResultCaluculator()
            result_calculator_obj.draw_monthly_temperature_chart_bonus_task(
                highest_temp_list, lowest_temp_list)

            print("Monthly Chart:\n")
            print(result_calculator_obj.monthly_temperature_chart)
            print("End Of Monthly Chart\n______________\n")
