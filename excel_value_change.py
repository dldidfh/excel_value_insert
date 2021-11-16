from config import * 
from line_info import LINE_INFO_LIST
def change_time_cell_value(current_sheet, init_times):
    # 요일별 07~09시 등 12~ 18시 등 변경하는 코드  
    for number_of_direction in range(4):
        for init_coord , init_time in enumerate(init_times):
            time_cell_coord = 5 + init_coord*12 + number_of_direction*39

            for unit_time in range(1,9):
                start_time = init_time + (unit_time-1)*ANALYSIS_UNIT
                end_time = init_time + unit_time * ANALYSIS_UNIT

                start_hour = start_time // 60
                start_minute = start_time % 60 
                end_hour = end_time // 60
                end_minute = end_time % 60

                if start_hour < 10 : 
                    start_hour = "0"+str(start_hour)
                if start_minute < 10:
                    start_minute = "0"+ str(start_minute)
                if end_hour < 10 : 
                    end_hour = "0"+str(end_hour)
                if end_minute < 10:
                    end_minute = "0"+ str(end_minute)

                current_sheet.cell(time_cell_coord,2).value = "{}:{} ~ {}:{}".format(start_hour, start_minute, end_hour, end_minute)
                if unit_time % 4 == 0:
                    time_cell_coord += 3 
                else:
                    time_cell_coord += 1
def change_count_cell_value(current_sheet, data, camera_number ):
    # key = 방향, value = {시간: 차량}
    for key, value in data.items():
        # 해당 key가 존재하는지 확인한다 
        if key in LINE_INFO_LIST[camera_number][1]:
            # 시트에 작성 시작할 셀의 좌표를 가져옴 
            cell_pointer = EXCEL_CELL_COORD[LINE_INFO_LIST[camera_number][1][key]]
            y, x = cell_pointer[0], cell_pointer[1]
            # k = 시간 (1,2,3,4.....), v = {'car':0, 'bus-s':0 .... }
            for k, v in value.items():
                # 차종은 6종으로 분류 
                car_type_6 = 1
                for c_type, count in v.items():
                    if car_type_6 % 7 ==  0 : break 
                    current_sheet.cell(y,x).value = count
                    # print(current_sheet.cell(y,x+1).value)
                    x +=1 
                    car_type_6 += 1 
                x = cell_pointer[1]
                if int(k) > 24 : break 
                if int(k) % 4 == 0: 
                    y += 3
                else:y+= 1
def change_PCU_cell_value(current_sheet, init_times):
    # y +=7 x+=8
    y = 7
    x = [41, 49, 57]
    y2 = 49
    for i in range(6):
        start_time = init_times[i//2] + ((i%2)*60)
        start_hour = start_time //60
        end_hour = start_time //60 + 1
        start_cell = [[y,x[0]], [y,x[1]], [y,x[2]]]
        
        
        if start_hour < 10:
            start_hour = "0"+ str(start_hour)
        if end_hour < 10:
            end_hour = "0" + str(end_hour)
        
        current_sheet.cell(y2,38).value = "{}시-{}시".format(start_hour, end_hour)
        y2+=1        
        for cell in start_cell:
            current_sheet.cell(cell[0],cell[1]).value = "{}시-{}시".format(start_hour, end_hour)
        y = y + 7


# x = 38 y = 49