# 回測
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import tensorflow.keras as keras
from tensorflow.keras.models import load_model

# 最近股價圖
df2 = pd.read_csv('台積電7月股價.csv',index_col=['Date'])

# 資料預處理(縮小) preprocessing
from sklearn.preprocessing import StandardScaler
# 讀取的特徵
df_scaled = df2[['Open','Low','High','Volume','Close']]


# 標準化
ss = StandardScaler()
df_scaled = ss.fit_transform(df2)
df_scaled = pd.DataFrame(df_scaled,index=df2.index,columns = df2.columns)

# 導入訓練好的模型
model = load_model('stockpredict_model.h5')

# 製作x,y 訓練集
n = 3 # 這以3天的特徵去預測之後的return
# 特徵 除了return之外的5個都是
feature_names = ['Open','Low','High','Volume','Close']
print(feature_names)
x = []
indexes = []
df_scaled_x = df_scaled[feature_names]
# testcases是n天 m維的x(這裡m為5 昨日: 開盤 最低價 最高價 成交量 收盤價) 配上一組y(收盤價)

# 3天的資料 包成一組x 對應到第四天(3天後的y) 因為會是在收盤才得到所有的資訊 
for i in range(3,len(df_scaled)): # 三個三個打包
    #i :i+n
    x.append(df_scaled_x.iloc[i-3:i].values) 
    # i+n-1
    indexes.append(df_scaled.index[i])
print(x)
print(indexes)

"""
print(x,"\n\n\n特徵x共",len(x),"筆")
print("資料集共有",len(indexes),"筆資料")
"""
# 塑型 X.Y 以貼合模組
# 最終shape x.shape = (376,3,5) y.shape=(376,1)
# 以三天的5個特徵 預測隔日股票的收盤價
import numpy as np
X = np.array(x)

# 預測
y_pred = model.predict(X) # 回傳的值為一組係數 代表Y的z分數
## 最後回歸資料用 

# 以Scale 去重新 inverse資料為原本的值 必須貼合原先的矩陣大小 (5,3,5)
new_y = np.reshape(y_pred,(1,5)) ##### 重塑原先的資料形狀
zero_array = np.zeros((2,5)) 
new_y = np.vstack([new_y,zero_array]) # 之後以0矩陣補充為 (3,5)
print(new_y)

for_inverse_arraytype = np.zeros((3,5)) # 之後建立 (3,5) 的0矩陣去做疊加 跌到符合5,3,5
print(for_inverse_arraytype)
for times in range(len(indexes)-1):
    new_y = np.vstack([new_y,for_inverse_arraytype]) 
print(new_y)
# inverse_transform 只貼合根原本未入的矩陣資料格式相同的
y_pred = ss.inverse_transform(new_y)
print(y_pred)
print("預測出的股價",y_pred[0][0:-1]) 
# 建立畫圖清單
y_pred_for_picture = []
for y in y_pred[0][0:-1]:
    y_pred_for_picture.append(round(y))
print(y_pred_for_picture)
import statistics
# 處理z分數的還原
def data_regression(data):
    mean = statistics.mean(data)
    std = statistics.stdev(data)
    return mean,std
final_close = df2['Close']

# 自己求平均數 標準差 去還原分數

mean,std = data_regression(final_close)
print(mean,std)
stock_close_value = []
for z_score_y in y_pred:
    stock_close_value.append(float(z_score_y*std+mean))

print("最後一項為明天的股價，",stock_close_value)

# index日期多加一天 
# 先處理年 datetime只有西元年才可轉換
vids_year = []
print(indexes)
for year in indexes:
    year_lst = year.split("/") # 拆分日期的index 形式為列表
    transfer_year = str(int(year_lst[0]) + 1911) # 將第一項 年的項目整數化 進行轉換
    year_lst.pop(0) # 去除第一項
    year_lst.insert(0,transfer_year) # 插入轉換後的
    year = "-".join(year_lst) # 重新合併成文字
    vids_year.append(year) # 新增到新的列表

import datetime # 以7/15.14.13預測 7/16收盤價
new_date = [] # 輸出圖表用
for vids in vids_year: # 檢驗預測日期 一般來說都加一天 
    year = datetime.datetime.strptime(vids,'%Y-%m-%d')
    if int(year.strftime("%w")) == 5: # 週五要加3天 預測出來是周一的
        years = year + datetime.timedelta(days=3,hours=13,minutes=30) # 加上收盤時間
        new_date.append(str(years))
    else: # 其他加1天就好
        years = year + datetime.timedelta(days=1,hours=13,minutes=30)# 加上收盤時間
        new_date.append(str(years))

plt.title('2330.ai.predict',fontsize=16)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Close',fontsize=16)
plt.plot(indexes[1:], y_pred_for_picture)
plt.show()