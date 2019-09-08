import time

# publish_Time = "2018年10月10日"
# array = time.strptime(publish_Time, u"%Y年%m月%d日")
# publishTime = time.strftime("%Y-%m-%d", array)
# print(publishTime)


time1 = '2017年7月19日'
array = time.strptime(time1, u"%Y年%m月%d日")
publishTime = time.strftime("%Y-%m-%d", array)
print(publishTime)

print(publishTime,'张三')
print(publishTime,'张三')
print(publishTime,'张三')
print(publishTime,'张三')
print(publishTime,'张三')
print(publishTime,'张三')