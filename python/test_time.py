import time
import datetime

t = time.time()

'''
  获取时间戳
'''

print(t)  # 原始时间数据 1578635524.3401906
print(int(t))  # 秒级时间戳 1578635524
print(int(round(t * 1000)))  # 毫秒时间戳 1578635524340

print('*' * 200)

'''
  获取格式化的字符串时间
'''
dt = datetime.datetime.now()

print(dt)  # 年-月-日 时：分：秒：毫秒 2020-01-10 13:52:04.341188
print(dt.strftime('%Y-%m-%d %H:%M:%S'))  # 年-月-日 时：分：秒 2020-01-10 13:52:04

print('*' * 200)

'''
  字符串时间转时间戳
'''
startTime = '2020-01-10 10:40:28'

timeArray = time.strptime(startTime, "%Y-%m-%d %H:%M:%S") # 转换成时间数组 
print(timeArray) # time.struct_time(tm_year=2020, tm_mon=1, tm_mday=10, tm_hour=10, tm_min=40, tm_sec=28, tm_wday=4, tm_yday=10, tm_isdst=-1)
print(type(timeArray)) # time.struct_time(tm_year=2020, tm_mon=1, tm_mday=10, tm_hour=10, tm_min=40, tm_sec=28, tm_wday=4, tm_yday=10, tm_isdst=-1)
ts = time.mktime(timeArray)  # 浮点型的时间 秒
print(ts)  # 1578624028.0
ts = int(ts)
print(ts)   # 1578624028

print('*'*200)

'''
  时间戳转日期时间字符串
'''
ts = 1578635837342
ltime = time.localtime(ts/1000)  # 转换成时间数组 @注意必须是秒
print(ltime) #  time.struct_time(tm_year=2020, tm_mon=1, tm_mday=10, tm_hour=13, tm_min=57, tm_sec=17, tm_wday=4, tm_yday=10, tm_isdst=0)
timeStr = time.strftime('%Y-%m-%d %H:%M:%S', ltime)
print(timeStr) # 2020-01-10 13:57:17s

print('*'*200)

now = datetime.datetime.now()
print(now.strftime('%A')) # Friday 输出完整的星期几
print(now.strftime('%B')) # January 输出月份

print(now.strftime('%c')) # Fri Jan 10 14:33:00 2020 以本地时间显示日期和时间
print(now.strftime('%d')) # 10 显示1-31之间的数，每月的第几天，也就是年月日中的日
print(now.strftime('%H')) # 14 24小时制
print(now.strftime('%I')) # 02 12小时制
print(now.strftime('%j')) # 010 一年中的第几天
print(now.strftime('%m')) # 01 1-12之间的月份
print(now.strftime('%M')) # 54 00-59之间的分钟数
print(now.strftime('%p')) # PM AM/PM上午还是下午
print(now.strftime('%S')) # 49 00-59之间的秒数
print(now.strftime('%U')) # 01 一年中的第几周，星期天为一周的第一天
print(now.strftime('%W')) # 01 一年中的第几周，星期一为一周的第一天
print(now.strftime('%w')) # 5 一周中的第几天，星期天为0，星期一为1
print(now.strftime('%x')) # 01/10/20 当地的日期
print(now.strftime('%X')) # 14:59:34 当地的时间
print(now.strftime('%y')) # 20 00-99的年份
print(now.strftime('%Y')) # 2020 完整的年份









