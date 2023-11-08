import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read data
datas = pd.read_csv('carseats.csv')

#抓大小
x = datas['Population']
y = datas['Sales']

# 圖一
# 設定軸大小
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(x, y)
plt.show()


Baddata = datas[datas['ShelveLoc'] =='Bad']
x_B = Baddata['Population']
y_B = Baddata['Sales']

Gooddata = datas[datas['ShelveLoc'] =='Good']
x_G = Gooddata['Population']
y_G = Gooddata['Sales']

Meddata = datas[datas['ShelveLoc'] =='Medium']
x_M = Meddata['Population']
y_M = Meddata['Sales']

# 圖二
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_B, y_B, label = 'Bad')
ax.scatter(x_G, y_G, label = 'Good')
ax.scatter(x_M, y_M, label = 'Medium')
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2)
plt.show()

# 因為有些Advertising欄位原本是0，下一步要將Size去做乘法，這樣就怎麼乘都是0，那這個點就會消失
Size_B = Baddata['Advertising'] +1
Size_G = Gooddata['Advertising']+1
Size_M = Meddata['Advertising']+1

# 圖三
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_B, y_B, s=Size_B*5, label = 'Bad')
ax.scatter(x_G, y_G, s=Size_G*5, label = 'Good')
ax.scatter(x_M, y_M, s=Size_M*5, label = 'Medium')
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2)
plt.title('Advertising budget')
plt.xlim(0,530) #設定x軸顯示範圍
plt.ylim(0,17) #設定y軸顯示範圍
plt.xlabel('Population')
plt.ylabel('Sales')
plt.show()


# 圖四
'''
1. 有利潤的點 size
2. AD ROI > ? 的點
3. 利潤是正/負的點
4. 預算高，有利潤 vs 預算高，沒利潤

'''

#mu, sigma = (datas['Price'].mean()-25), 10
#s = np.random.normal(mu, sigma, len(datas['Price']))
#datas['cost'] = s


# 問題：將Sales - Advertising，淨利＝毛利-廣告費用
datas['profit'] = datas['Sales'] * (datas['Price'] -datas['cost'] ) - datas['Advertising'] 

# 問題：將AD profit轉換到圖三的size

Baddata = datas[datas['ShelveLoc'] =='Bad']
x_B = Baddata['Population']
y_B = Baddata['Sales']

Gooddata = datas[datas['ShelveLoc'] =='Good']
x_G = Gooddata['Population']
y_G = Gooddata['Sales']

Meddata = datas[datas['ShelveLoc'] =='Medium']
x_M = Meddata['Population']
y_M = Meddata['Sales']


# 因有些淨利太大了，會導致圈圈面積過大，因此透過等比例除以50來做調整
Size_B = Baddata['profit'] / 50
Size_G = Gooddata['profit']/ 50
Size_M = Meddata['profit']/ 50

# 圖四
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_B, y_B, s=Size_B*10, label = 'Bad')
ax.scatter(x_G, y_G, s=Size_G*10, label = 'Good')
ax.scatter(x_M, y_M, s=Size_M*10, label = 'Medium')
lgnd = plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[2]._sizes = [30]
plt.title('profit point')
plt.xlim(0,530) #設定x軸顯示範圍
plt.ylim(0,17) #設定y軸顯示範圍
plt.xlabel('Population')
plt.ylabel('Sales')
plt.show()

#datas.to_csv('carseats2.csv', index= False)
#datas = datas.rename(columns = {'Unnamed: 0':'ID' })

# 圖五
# ROI 投資報酬率：每花一塊錢他可以幫你賺回來多少錢
datas['total_cost'] =  datas['Sales'] *datas['cost'] + datas['Advertising'] 
#datas['Revenue'] =  datas['Sales'] *datas['Price']
datas['ROI'] =datas['profit']/ datas['total_cost']


Baddata = datas[datas['ShelveLoc'] =='Bad']
x_B = Baddata['Population']
y_B = Baddata['Sales']

Gooddata = datas[datas['ShelveLoc'] =='Good']
x_G = Gooddata['Population']
y_G = Gooddata['Sales']

Meddata = datas[datas['ShelveLoc'] =='Medium']
x_M = Meddata['Population']
y_M = Meddata['Sales']

Size_B = Baddata['ROI']  
Size_G = Gooddata['ROI']
Size_M = Meddata['ROI']

# 圖五
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_B, y_B, s=Size_B*70, label = 'Bad')
ax.scatter(x_G, y_G, s=Size_G*70, label = 'Good')
ax.scatter(x_M, y_M, s=Size_M*70, label = 'Medium')
lgnd = plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[2]._sizes = [30]
plt.title('ROI point')
plt.xlim(0,530) #設定x軸顯示範圍
plt.ylim(0,17) #設定y軸顯示範圍
plt.xlabel('Population')
plt.ylabel('Sales')
plt.show()


# 名單
'''
0. 要產出bad, good, medium三種貨架資料
1. ROI大於0.5
2. ROI由大排到小
3. 老闆只要看['ID', 'Sales','Advertising','total_cost', 'profit', 'ROI']這幾個欄位

'''

Baddata = Baddata.sort_values('ROI', ascending  = False)
Baddata_list = Baddata[Baddata['ROI'] > 0.5] 
Baddata_list[['ID', 'Sales','Advertising','total_cost', 'profit', 'ROI']].to_csv('Baddata_list.csv', encoding = 'cp950')

Gooddata = Gooddata.sort_values('ROI', ascending  = False)
Gooddata_list = Gooddata[Gooddata['ROI'] > 0.5] 
Gooddata_list[['ID', 'Sales','Advertising','total_cost', 'profit', 'ROI']].to_csv('Gooddataa_list.csv', encoding = 'cp950')

Meddata = Meddata.sort_values('ROI', ascending  = False)
Meddata_list = Meddata[Meddata['ROI'] > 0.5] 
Meddata_list[['ID', 'Sales','Advertising','total_cost', 'profit', 'ROI']].to_csv('Meddata_list.csv', encoding = 'cp950')

