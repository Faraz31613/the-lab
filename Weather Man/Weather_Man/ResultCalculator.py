from datetime import datetime


class ResultCaluculator:
    def calculate_highest_temp_in_year(year_data):
        months_in_year = list(year_data.keys())
        if len(months_in_year) == 0:
            print("No data exists for this year!")
            return
        max_temps = []
        max_temps_including_empty_values = []
        year_dates = []
        for month in range(len(months_in_year)):
            for day_data in year_data[months_in_year[month]]:
                if day_data.max_temperature_c != None:
                    max_temps.append(day_data.max_temperature_c)
                max_temps_including_empty_values.append(
                    day_data.max_temperature_c)
                year_dates.append(day_data.pkt)
        max_temp = max(max_temps)
        index_of_max_temp = max_temps_including_empty_values.index(max_temp)
        max_temp_date = year_dates[index_of_max_temp]

        year, month, day = max_temp_date.split("-")
        date_converted = datetime(int(year), int(
            month), int(day))
        month_day = (date_converted.strftime("%B %d"))

        highest_temp = (f"Highest: {max_temp}C on {month_day}")
        return highest_temp

    def calculate_lowest_temp_in_year(year_data):
        months_in_year = list(year_data.keys())
        if len(months_in_year) == 0:
            print("No data exists for this year!")
            return
        min_temps = []
        min_temps_including_empty_values = []
        year_dates = []
        for month in range(len(months_in_year)):
            for day_data in year_data[months_in_year[month]]:
                if day_data.min_temperature_c != None:
                    min_temps.append(day_data.min_temperature_c)
                min_temps_including_empty_values.append(
                    day_data.min_temperature_c)
                year_dates.append(day_data.pkt)
        min_temp = min(min_temps)
        index_of_min_temp = min_temps_including_empty_values.index(min_temp)
        min_temp_date = year_dates[index_of_min_temp]

        year, month, day = min_temp_date.split("-")
        date_converted = datetime(int(year), int(
            month), int(day))
        month_day = (date_converted.strftime("%B %d"))

        lowest_temp = (f"Lowest: {min_temp}C on {month_day}")
        return lowest_temp

    def calculate_max_humidity_in_year(year_data):
        months_in_year = list(year_data.keys())
        if len(months_in_year) == 0:
            print("No data exists for this year!")
            return
        max_humidities = []
        max_humidities_including_empty_values = []
        year_dates = []
        for month in range(len(months_in_year)):
            for day_data in year_data[months_in_year[month]]:
                if day_data.max_humidity != None:
                    max_humidities.append(day_data.max_humidity)
                max_humidities_including_empty_values.append(
                    day_data.max_humidity)
                year_dates.append(day_data.pkt)
        max_humidity = max(max_humidities)
        index_of_max_humidity = max_humidities_including_empty_values.index(
            max_humidity)
        max_humidity_date = year_dates[index_of_max_humidity]

        year, month, day = max_humidity_date.split("-")
        date_converted = datetime(int(year), int(
            month), int(day))
        month_day = (date_converted.strftime("%B %d"))

        highest_humidity = (f"Humidity: {max_humidity}% on {month_day}")
        return highest_humidity

    def calculate_avg_highest_temp_in_month(month_data):
        month = (list(month_data.keys()))[0]
        max_temps = []
        for day_data in month_data[month]:
            if day_data.max_temperature_c != None:
                max_temps.append(day_data.max_temperature_c)

        sum_of_max_temp = sum(max_temps)
        avg_of_max_temp = sum_of_max_temp / len(max_temps)
        return f"Highest Average: {avg_of_max_temp:.1f}C"

    def calculate_avg_lowest_temp_in_month(month_data):
        month = (list(month_data.keys()))[0]
        min_temps = []
        for day_data in month_data[month]:
            if day_data.min_temperature_c != None:
                min_temps.append(day_data.min_temperature_c)

        sum_of_min_temp = sum(min_temps)
        avg_of_min_temp = sum_of_min_temp / len(min_temps)
        return f"Lowest Average: {avg_of_min_temp:.1f}C"

    def calculate_avg_mean_humidity_in_month(month_data):
        month = (list(month_data.keys()))[0]
        mean_humidities = []
        for day_data in month_data[month]:
            if day_data.mean_humidity != None:
                mean_humidities.append(day_data.mean_humidity)

        sum_of_mean_humidities = sum(mean_humidities)
        avg_of_mean_humidity = sum_of_mean_humidities / len(mean_humidities)
        return f"Average Mean Humidity: {avg_of_mean_humidity:.0f}%"

    def draw_monthly_temperature_chart(month_data):
        month = (list(month_data.keys()))[0]
        max_temps = []
        min_temps = []
        for day_data in month_data[month]:
            max_temps.append(day_data.max_temperature_c)
            min_temps.append(day_data.min_temperature_c)

        high_temp_chart = ""
        low_temp_chart = ""
        month_chart = ""
        for day_counter in range(len(max_temps) or len(min_temps)):
            day = (str(day_counter+1)).zfill(2)
            no_record_message = "No record exists for this day!"

            if max_temps[day_counter] == None:
                high_temp_chart = f"{day} {no_record_message}\n"
            else:
                max_temp_on_day = max_temps[day_counter]
                max_temp_on_day_chart = ''.ljust(
                    max_temp_on_day, '+')
                high_temp_chart = f"\033[1;37;40m{day}\033[1;31;40m {max_temp_on_day_chart} {max_temp_on_day}C\n"

            if min_temps[day_counter] == None:
                low_temp_chart = f"{day} {no_record_message}\n"
            else:
                min_temp_on_day = min_temps[day_counter]
                min_temp_on_day_chart = ''.ljust(
                    min_temp_on_day, '+')
                low_temp_chart = f"\033[1;37;40m{day}\033[1;34;40m {min_temp_on_day_chart} {min_temp_on_day}C\033[0;37;40m\n"

            day_chart = f"{high_temp_chart}{low_temp_chart}"
            month_chart = month_chart + day_chart

        return month_chart

    def draw_monthly_temperature_chart_bonus_task(month_data):
        month = (list(month_data.keys()))[0]
        max_temps = []
        min_temps = []
        for day_data in month_data[month]:
            max_temps.append(day_data.max_temperature_c)
            min_temps.append(day_data.min_temperature_c)

        high_temp_chart = ""
        low_temp_chart = ""
        month_chart = ""
        for day_counter in range(len(max_temps) or len(min_temps)):
            day = (str(day_counter+1)).zfill(2)
            no_record_message = "*No record exists!*"
            max_temp_on_day = None
            max_temp_on_day_chart = ""
            min_temp_on_day = None
            min_temp_on_day_chart = ""
            if max_temps[day_counter] == None:
                high_temp_chart = no_record_message
            else:
                max_temp_on_day = max_temps[day_counter]
                max_temp_on_day_chart = ''.ljust(
                    max_temp_on_day, '+')
                # high_temp_chart = ("\033[1;31;40m{0} {1} {2}C\n".format(
                #     day, max_temp_on_day_chart, max_temp_on_day))

            if min_temps[day_counter] == None:
                low_temp_chart = no_record_message
            else:
                min_temp_on_day = min_temps[day_counter]
                min_temp_on_day_chart = ''.ljust(
                    min_temp_on_day, '+')
                # low_temp_chart = ("\033[1;34;40m{0} {1} {2}C\033[0;37;40m\n".format(
                #     day, min_temp_on_day_chart, min_temp_on_day))

            if max_temps[day_counter] != None and min_temps[day_counter] != None:
                day_chart = f"{day} \033[1;34;40m{min_temp_on_day_chart}\033[1;31;40m{max_temp_on_day_chart}\033[0;37;40m {min_temp_on_day}C - {max_temp_on_day}C\n"
                month_chart = month_chart + day_chart
            elif max_temps[day_counter] == None and min_temps[day_counter] != None:
                day_chart = f"{day} \033[1;34;40m{high_temp_chart}\033[1;31;40m{min_temp_on_day_chart}\033[0;37;40m Min - {min_temp_on_day}\n"
                month_chart = month_chart + day_chart
            elif max_temps[day_counter] != None and min_temps[day_counter] == None:
                day_chart = f"{day} \033[1;34;40m{max_temp_on_day_chart}\033[1;31;40m{low_temp_chart}\033[0;37;40m {max_temp_on_day} - Max\n"
                month_chart = month_chart + day_chart
            else:
                day_chart = f"{day} \033[1;34;40m{high_temp_chart}\033[1;31;40m{low_temp_chart}\033[0;37;40m Min - Max\n"
                month_chart = month_chart + day_chart

        return month_chart
