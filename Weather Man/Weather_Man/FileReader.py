class FileReader():
    def __init__(self):
        self.pkt = []
        self.max_temperature_c = []
        self.mean_temperature_c = []
        self.min_temperature_c = []
        self.dew_point_c = []
        self.mean_dewpoint_c = []
        self.min_dewpoint_c = []
        self.max_humidity = []
        self.mean_humidity = []
        self.min_humidity = []
        self.max_sea_level_pressureh_pa = []
        self.mean_sea_level_pressureh_pa = []
        self.min_sea_level_pressureh_pa = []
        self.max_visibility_km = []
        self.mean_visibility_km = []
        self.min_visibility_km = []
        self.max_wind_speed_km_h = []
        self.mean_wind_speed_km_h = []
        self.max_gust_speed_km_h = []
        self.precipitation_mm = []
        self.cloud_cover = []
        self.events = []
        self.wind_dir_degrees = []

    def data_filler(self, file_path_list=[]):
        i = 0
        while(i < len(file_path_list)):
            with open(file_path_list[i]) as read_file:
                next(read_file)
                for line in read_file:
                    one_day_data = line.split(",")

                    self.pkt.append(one_day_data[0])
                    self.max_temperature_c.append(one_day_data[1])
                    self.mean_temperature_c.append(one_day_data[2])
                    self.min_temperature_c.append(one_day_data[3])
                    self.dew_point_c.append(one_day_data[4])
                    self.mean_dewpoint_c.append(one_day_data[5])
                    self.min_dewpoint_c.append(one_day_data[6])
                    self.max_humidity.append(one_day_data[7])
                    self.mean_humidity.append(one_day_data[8])
                    self.min_humidity.append(one_day_data[9])
                    self.max_sea_level_pressureh_pa.append(one_day_data[10])
                    self.mean_sea_level_pressureh_pa.append(one_day_data[11])
                    self.min_sea_level_pressureh_pa.append(one_day_data[12])
                    self.max_visibility_km.append(one_day_data[13])
                    self.mean_visibility_km.append(one_day_data[14])
                    self.min_visibility_km.append(one_day_data[15])
                    self.max_wind_speed_km_h.append(one_day_data[16])
                    self.mean_wind_speed_km_h.append(one_day_data[17])
                    self.max_gust_speed_km_h.append(one_day_data[18])
                    self.precipitation_mm.append(one_day_data[19])
                    self.cloud_cover.append(one_day_data[20])
                    self.events.append(one_day_data[21])
                    self.wind_dir_degrees.append(one_day_data[22])

            i = i+1
