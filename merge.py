
import pandas as pd
from get_xlsx import Get_xlsx
# 此处填写要合并exce所在文件夹 Get_xlsx 用于获取该文件夹所有的xlsx文件
file = Get_xlsx("/Users/yueqi/Desktop/格式一样，需合并到一张表格")
li = []
for i in file:
    # skiprows填写忽略行
    li.append(pd.read_excel(i,skiprows=[0]))
# print(li)
# pd.ExcelWrite填写输出文件地址
writer = pd.ExcelWriter('/Users/yueqi/Desktop/excel5.xlsx',)
# reindex安装li[0]的行排序
r = pd.concat(li,sort=False).reindex(li[0].columns, axis=1)
r.to_excel(writer, 'Sheet1', index=False)

writer.save()
