# 雙重輸出
# 此題的要點在於將兩個輸入項目轉換為整數同時，也必須保留原本字串的資料型態
# 小提示: input()函式內建的資料型態為字串
a = input() # 建立輸入變數a
b = input() # 建立輸入變數b
int_a = int(a) # 創造新的變數 並將a轉換為整數型態存入其中
int_b = int(b) # b如同a一樣操作

# 依題目要求的將結果打印出來
print(int_a+int_b) # a+b
print(int_a*int_b) # a*b
print(int_a%int_b) # a%b
print(a*int_b) # a輸出b次
print(b*int_a) # b輸出a次