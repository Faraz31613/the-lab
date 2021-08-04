from WeatherDataExtractor import WeatherDataExtractor
from ResultCalculator import ResultCaluculator
import argparse


def weather_man_Report_Handler():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help="input file", metavar="FILE")
    parser.add_argument("-e", "--year", type=str, action='append')
    parser.add_argument("-a", "--month", type=str, action='append')
    parser.add_argument("-c", "--graph", type=str, action='append')
    args = parser.parse_args()
    file_path = args.path
    years_for_reporting = args.year
    months_for_reporting = args.month
    months_for_graph_report = args.graph
    months_list = ["Jan", "Feb", "Mar", "Apr", "May",
                   "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if not years_for_reporting:
        pass
    else:
        for x in range(len(years_for_reporting)):
            year_weather_data = WeatherDataExtractor
            year_data = year_weather_data.year_data_extractor(
                file_path, years_for_reporting[x], months_list)
            if year_data == None:
                print(f"No data exists for this {years_for_reporting[x]}")
            else:
                result_calculator = ResultCaluculator
                max_temp = result_calculator.calculate_highest_temp_in_year(
                    year_data)
                min_temp = result_calculator.calculate_lowest_temp_in_year(
                    year_data)
                max_humidity = result_calculator.calculate_max_humidity_in_year(
                    year_data)
                print(max_temp)
                print(min_temp)
                print(max_humidity)

    if not months_for_reporting:
        pass
    else:
        for x in range(len(months_for_reporting)):
            year, month = months_for_reporting[x].split("/")
            month = months_list[int(month)-1]
            month_weather_data = WeatherDataExtractor
            month_data = month_weather_data.month_data_extractor(
                file_path, year, month)
            if month_data == None:
                print(f"No data exists for this {month}")
            else:
                result_calculator = ResultCaluculator
                avg_max_temp = result_calculator.calculate_avg_highest_temp_in_month(
                    month_data)
                avg_min_temp = result_calculator.calculate_avg_lowest_temp_in_month(
                    month_data)
                avg_mean_humidity = result_calculator.calculate_avg_mean_humidity_in_month(
                    month_data)
                print(avg_max_temp)
                print(avg_min_temp)
                print(avg_mean_humidity)

    if not months_for_graph_report:
        pass
    else:
        for x in range(len(months_for_graph_report)):
            year, month = months_for_graph_report[x].split("/")
            month = months_list[int(month)-1]
            month_weather_data = WeatherDataExtractor
            month_data = month_weather_data.month_data_extractor(
                file_path, year, month)
            if month_data == None:
                print(f"No data exists for this {month}")
            else:
                result_calculator = ResultCaluculator
                monthly_temp_graph = result_calculator.draw_monthly_temperature_chart(
                    month_data)

                # monthly_temp_graph = result_calculator.draw_monthly_temperature_chart_bonus_task(month_data)
                print(monthly_temp_graph)
