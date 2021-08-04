class DayWeather:
    def __init__(self, day_data):
        self.pkt = day_data[0]
        self.max_temperature_c = None if day_data[1] == "" else int(
            day_data[1])
        self.mean_temperature_c = day_data[2]
        self.min_temperature_c = None if day_data[3] == "" else int(
            day_data[3])
        self.dew_point_c = day_data[4]
        self.mean_dewpoint_c = day_data[5]
        self.min_dewpoint_c = day_data[6]
        self.max_humidity = None if day_data[7] == "" else int(day_data[7])
        self.mean_humidity = None if day_data[8] == "" else int(day_data[8])
        self.min_humidity = day_data[9]
        self.max_sea_level_pressureh_pa = day_data[10]
        self.mean_sea_level_pressureh_pa = day_data[11]
        self.min_sea_level_pressureh_pa = day_data[12]
        self.max_visibility_km = day_data[13]
        self.mean_visibility_km = day_data[14]
        self.min_visibility_km = day_data[15]
        self.max_wind_speed_km_h = day_data[16]
        self.mean_wind_speed_km_h = day_data[17]
        self.max_gust_speed_km_h = day_data[18]
        self.precipitation_mm = day_data[19]
        self.cloud_cover = day_data[20]
        self.events = day_data[21]
        self.wind_dir_degrees = day_data[22]
