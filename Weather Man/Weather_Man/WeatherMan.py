import os
import sys

from ReportCreator import ReportCreator


def main():

    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
        arguments_counter = 2
        while (arguments_counter < len(sys.argv)):
            year = sys.argv[arguments_counter+1]
            months_list = ["Jan", "Feb", "Mar", "Apr", "May",
                           "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            if sys.argv[arguments_counter] == "-e":
                print("Yearly Report:\n")
                yearly_report = ReportCreator()
                yearly_report.year_report(file_name, year, months_list)
                print("End Of Yearly Report\n______________\n")
            elif sys.argv[arguments_counter] == "-a":
                print("Monthly Report:\n")
                year_month = year.split("/")
                year = year_month[0]
                month = months_list[int(year_month[1])-1]
                monthly_report = ReportCreator()
                monthly_report.monthly_report(file_name, year, month)
                print("End Of Monthly Report\n______________\n")
            elif sys.argv[arguments_counter] == "-c":
                print("Monthly Chart:\n")
                year_month = year.split("/")
                year = year_month[0]
                month = months_list[int(year_month[1])-1]
                monthly_report = ReportCreator()
                monthly_report.monthly_graph(file_name, year, month)
                print("End Of Monthly Chart\n______________\n")
            arguments_counter = arguments_counter+2
    else:
        print("No argument is passed to Weather Man")


main()
