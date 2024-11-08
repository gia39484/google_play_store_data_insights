import pandas as pd
# csv格式讀取成DataFame
data = pd.read_csv('googleplaystore.csv')
# 觀察資料
print('資料數量', data.shape)
print('資料欄位', data.columns)
# 分析資料：發現資料異常
print('平均數', data['Rating'].mean())
print('中位數', data['Rating'].median())
print('前一百個應用程式的平均', data['Rating'].nlargest(100).mean())
print('＝＝＝＝＝＝＝＝＝＝＝排除異常評分值資料＝＝＝＝＝＝＝＝＝＝＝')
condition = data['Rating'] <= 5
data1 = data[condition]
print('平均數', data1['Rating'].mean())
print('中位數', data1['Rating'].median())
print('取得前一百個應用程式的平均', data1['Rating'].nlargest(100).mean())
print('取得前一千個應用程式的平均', data1['Rating'].nlargest(1000).mean())
print('＝＝＝＝＝＝＝＝＝＝尋找異常異常評分資料＝＝＝＝＝＝＝＝＝＝＝＝')
condition1 = data['Rating'] > 5
data2 = data[condition1]
print('異常資料', data2, sep='\n')
print('異常資料評分', data2['Rating'], sep='\n')

# 分析資料：安裝數量的各種統計數據
print('＝＝＝＝＝＝＝＝＝＝清理資料＝＝＝＝＝＝＝＝＝＝＝＝')
print(data['Installs'])
data['Installs'] = pd.to_numeric(data["Installs"].str.replace('[,+]', '').replace('Free', ''))
print(data['Installs'])
print('平均數', round(data['Installs'].mean(), 2))
condition = data['Installs'] > 100_000
print('安裝次數大於100,000的應用程式有幾個：', data[condition].shape[0])

# 基於資料的應用：關鍵字搜尋應用程式名稱
keyword = input('請輸入關鍵字：')
condition = data['App'].str.contains(keyword, case=False)
print('包含關鍵字的應用程式有哪些：', data[condition]['App'], sep='\n')
print('包含關鍵字的應用程式數量：', data[condition].shape[0])


