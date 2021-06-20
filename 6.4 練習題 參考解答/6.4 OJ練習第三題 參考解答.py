# 幸運數字
# 此題的重點在於轉換輸入字串為整數型態進行運算同時，也必須保留原本的字串
# 小提示: input()函式內建的資料型態為字串

month = input() # 輸入兩筆資料 分別為月和日
day = input()

int_month = int(month) # 將兩者轉換資料型態為整數
int_day = int(day) 

lucky = int_month+int_day # 命名新變數lucky,結果為兩者加法運算

print("你的生日是",month,"/",day) # 依題目指定輸出格式輸出
print("幸運數字是",lucky) # 依題目指定輸出格式輸出