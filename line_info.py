from config import EXCEL_SHEET_NAEMS
LINE_INFO_LIST = {
    
        "1" : [ # 1_Friday or 1_Sunday
            EXCEL_SHEET_NAEMS[0],
            {"0->1" : 1, "0->2" : 2 ,
             "3->0" : 4, "3->1" : 5, "3->2" : 6,
             "2->3" : 7, "2->0" : 8, "2->1" : 9,
             "1->2" : 10, "1->3" : 11, "1->0" : 12,
             "5->6" : "10U"
            }
        ],
        "2" : [ # 2_Friday or 2_Sunday
            EXCEL_SHEET_NAEMS[0],
            { }
        ],
        "3" : [
            EXCEL_SHEET_NAEMS[0],
            {"1->4" : 3,
            "2->3" : "4U",
             }
        ],
        "4" : [
            EXCEL_SHEET_NAEMS[3],
            {"3->4": 9}
        ],
        "5" : [
            EXCEL_SHEET_NAEMS[1],
            {"2->1" : 1, "2->0" : 2 ,"7->6" : 3,
             "3->2" : 4, "3->1" : 5, "3->0" : 6,
             "0->3" : 7, "0->2" : 8, "0->1" : 9,
             "1->0" : 10, "1->3" : 11, "4->5" : 12,
             "8->9" : "4U"
             }
        ],
        "6" : [
            EXCEL_SHEET_NAEMS[2],
            {"3->2" : 1,"3->1" : 2,"3->4" : 3,
             "0->3" : 4, "0->2" : 5, "0->1" : 6,
             
             "2->1" : 10, "2->0" : 11, 
             "5->6" : "10U",
             }
        ],
        "7" : [
            EXCEL_SHEET_NAEMS[0],
            {}
        ],
        "8" : [
            EXCEL_SHEET_NAEMS[2],
            {
             
             "5->6" : "4U",
             "4->0" : 7, "4->2" : 8, 
             "3->2" : 12,
             }
        ],
        "9" : [
            EXCEL_SHEET_NAEMS[2],
            {"2->3" : 9}
        ],
        "10" : [
            EXCEL_SHEET_NAEMS[3],
            { "2->1" : "4U"}
        ],
        "11" : [
            EXCEL_SHEET_NAEMS[4],
            {"4->3":5,
            "3->4" : 11}
        ],
        "12" : [
            EXCEL_SHEET_NAEMS[3],
            # 3,4,5,6,6,7,8,10,11,12,"10U"
            {  "4->5" : 3,
            "6->7" : 4, "6->9" : 5, "6->8" : 6,
            "8->5" : 7, "8->4" : 8, 
            "3->7" : 10, "3->5" : 11, "3->4" : 12,
            "2->1" : "10U"
            }
        ],
        "13" : [
            EXCEL_SHEET_NAEMS[5],
            {"6->7" : 2,"4->3" : 3,
            "3->7" : 4, "3->1" : 6,
            "0->2" : "7U",
            "1->3" : 7, "1->7" : 8,}
        ],
        "14" : [
            EXCEL_SHEET_NAEMS[6],
            { "10->11" : 9, 
            "7->8" : 10, "8->9" : 11, "4->3" : 12,
            "0->1" : "10U",}
        ],
        "15" : [
            EXCEL_SHEET_NAEMS[6],
            {"1->3" : 1, "1->2" : 2, "1->0" : 3,
            "0->1" : 4, "0->3" : 5, "0->2" : 6,
            "2->0" : 7, "2->1" : 9, 
            }
        ],
        "16" : [
            EXCEL_SHEET_NAEMS[7],
            { "4->5" : 3, 
            "10->9" : 4, "14->13" : 5, "18->17" : 6,
            "8->7" : "4U",
             }
        ],
        "17" : [
            EXCEL_SHEET_NAEMS[7],
            {"7->8" : 1,
            "3->4" : 9,
            "11->10" : 10,"14->13" : 11,"17->16" : 12,
            "2->1" : "10U",}
        ],
        "18" : [
            EXCEL_SHEET_NAEMS[8],
            {  "2->1" : 5,
            "1->2" : 11,}
        ],
        
}
