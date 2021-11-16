import os 
from config import *
class ReadTXT():
    def __init__(self, path_dir_name) -> None:
        self.result_dict = {}
        self.path_dir_name = path_dir_name
            
    def read_result_txt(self):
    # 해당 폴더에 모든 txt 파일을 읽어온다 ( result1.txt, result3.txt, result3.txt .....)
        path_dir_path = os.path.join(RESULT_PATH, self.path_dir_name)
        result_txt_name_list = os.listdir(path_dir_path)
        time_count_var = 0

        for result_txt_name in result_txt_name_list:
            # 해당 txt 파일을 읽는다 
            # RESULT_PATH\\10_Friday\\result1.txt
            result_txt_path = os.path.join(path_dir_path, result_txt_name)
            with open(result_txt_path, 'r') as rd :
                lines = rd.readlines()
                for line in lines:
                    if line.find('min') > 0:
                        # 시간을 나타내면 
                        time_count_var +=1 
                        # self.result_dict[time_count_var] = {}
                        continue
                    elif line.find('->') > 0:
                        # 방향을 나타내면 
                        direction_var = line.strip()
                        if direction_var not in self.result_dict :        
                            self.result_dict[direction_var] = {}
                        self.result_dict[direction_var][time_count_var] = {"car":0, "bus-s":0,"bus-m":0,"truck-s":0,"truck-m":0,"truck-x":0}
                        continue
                    else:
                        # 차종을 나타내면 
                        car_type, count =line.split(":") # "car : 23\n"
                        car_type = car_type.strip() # "car "
                        count = count.strip() # " 23\n"
                        self.result_dict[direction_var][time_count_var][car_type] = int(count)
        return self.result_dict