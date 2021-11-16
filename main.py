from datetime import time
import pandas as pd
import numpy as np 
from config import *
import os 
import sys 
import re 
import copy
from excel_read import ExcelControl
from read_result_txt import ReadTXT
from line_info import LINE_INFO_LIST
from excel_value_change import *
# car_type_dict = {"car":0, "bus-s":0,"bus-m":0,"truck-s":0,"truck-m":0,"truck-x":0}

# 엑셀을 관리하는 클레스 생성 
excel_controler = ExcelControl()

# 설정된 경로에 모든 폴더를 읽어온다 (10_Friday, 10_Sunday, 11_Friday, 11_Sunday .....)
path_dir_name_list = os.listdir(RESULT_PATH)

for sheet_num, path_dir_name in enumerate(path_dir_name_list):
    # path_dir_name = 10_Friday  ..... 
    read_txt_object = ReadTXT(path_dir_name)
    data = read_txt_object.read_result_txt()
    # 해당 카메라가 어느 지점의 카메라인지 변수 설정     
    camera_number = path_dir_name.split('_')[0]
    write_sheet_name = LINE_INFO_LIST[camera_number][0]
    # 현재 작업 sheet를 변경한다  (Friday, Sunday)
    day_key_word = path_dir_name.split('_')[1]
    # 요일에 맞는 시트 생성 (01. 복용네거리 금요일, 01. 복용네거리 일요일)
    location_name_day = excel_controler.copy_new_sheets(camera_number, day_key_word)

    current_sheet = excel_controler.loaded_workbook[location_name_day]# [write_sheet_name]
    if day_key_word == "Friday":
        init_times = FRIDAY_TIMES
    elif day_key_word == "Sunday":
        init_times = SUNDAY_TIMES
    # 셀 위치에 값 넣기 
    change_time_cell_value(current_sheet, init_times)
    change_count_cell_value(current_sheet, data, camera_number )
    change_PCU_cell_value(current_sheet, init_times)

# 복사를 위해 가져왔던 시트 삭제 
del excel_controler.loaded_workbook['Sheet1']

# 시트 정렬해서 1번부터 차례대로 

excel_controler.loaded_workbook._sheets.sort(key=lambda ws: ws.title)
# 시트 저장 
excel_controler.write_excel()














# time_dict = {}
# for qwe in range(1,30):
#     if qwe < 10:        
#         time_dict[str(qwe*15) + " min"] = qwe
#     else: 
#         time_dict[str(qwe*15) + " min"] = qwe
# # for dir_name in path_dir_names:
# dir_name = '8_Sunday'
# one_dir_path = os.path.join(RESULT_PATH, dir_name)
# result_file_names = os.listdir(one_dir_path)
# dict1 = {}
# df = pd.DataFrame(columns=car_type)
# for result_file_name in result_file_names:
#     path_result_file = os.path.join(one_dir_path, result_file_name)
#     with open(path_result_file, 'r') as rd :
#         counting_result = rd.readlines()
#         for i, temp in enumerate(counting_result):
#             if i == 0:
#                 time_var = temp.strip()
#                 # dict1[time_var] = {}
#                 continue
#             if temp.find('>') > 0 :
#                 # 방향을 가르킴 
#                 direction_var = temp.strip()
#                 if direction_var not in dict1 :                
#                     dict1[direction_var] = {}
#                 dict1[direction_var][time_dict[time_var]] = {} 
#                 continue
#             else:
#                 # 카운팅을 가르킴 
#                 temp = temp.strip().split(':')
#                 car_type = temp[0].strip()
#                 count = temp[1].strip()
#                 dict1[direction_var][time_dict[time_var]][car_type] = count 
#                 # df[]

# # 데이터 없는거 지우기 
# dict2 = copy.deepcopy(dict1)
# for key, value in dict2.items():  
#     if len(value) == 0:
#         dict1.pop(key)
#         continue
#     # for k, v in value.items():
#     #     if len(v) == 0:
#     #         dict1[key].pop(k)



# df = pd.DataFrame(dict1)
# print(df)


