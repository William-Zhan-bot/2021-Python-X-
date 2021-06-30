# 商品檢驗表
shop = dict() # 建立字典以儲存題目
while True: # 多重輸入 以while來計算 每個輸入是一個項目對應一個價格
    name = input() 
    if name == 'end': # 條件式--中斷迴圈
        break
    cost = int(input()) # 價格
    shop[name] = cost # 字典 指定價格

i = input() # 輸入查找的品項
print(shop[i]) # 輸出價格
    