## 日期、时间、时间戳处理


### 1.获取时间戳

```py

import time
import datetime

# 获取13位毫秒的时间戳 `1578635524340`
ts = int(round(time.time() * 1000)) 

# 获取10位秒的时间戳 `1578635524`
ts = int(round(time.time()))

```

### 2.获取格式化的字符串日期时间

```py

import time
import datetime

# 年-月-日 时：分：秒 `2020-01-10 13:52:04`
stime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

```


### 3.字符串日期时间转时间戳

```py

import time
import datetime

startTime = '2020-01-10 10:40:28'

# 转换成10位秒的时间戳 `1578624028`
struct_time = time.strptime(startTime, "%Y-%m-%d %H:%M:%S")
ts = int(time.mktime(struct_time)

ts = int(time.mktime(timeArr)*1000 # 转换成13位毫秒的时间戳 `1578624028000`

```

### 4.时间戳转字符串日期时间

```py

import time
import datetime

ts = 1578635837342

# 先转换成时间结构，再格式化时间  @注意必须是秒  `2020-01-10 13:57:17`
struct_time = time.localtime(ts/1000)  
stime = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)

```

### 5.其他
```py

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

```
