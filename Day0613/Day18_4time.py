import time

print('111')
# time.sleep(2)
print('222')
print(time.time())
# 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S')) #表示年月日时分秒
print(time.strftime('%y-%m-%d %H:%M:%S')) #表示年月日时分秒
print(time.strftime('%c')) #表示年月日时分秒
print(time.localtime())
#查看时间戳时间为200000000时间表示的年月日
# 时间戳 - 结构化 - 格式化
struct_t = time.localtime(200000000)
print(struct_t)
print(time.strftime('%Y-%m-%d',struct_t))

#将2008-8-8 转换为时间戳时间
t = time.strptime('2008-8-8','%Y-%m-%d')
print(time.mktime(t))

#将当前时间月份的一号的时间戳取出来
def func():
    st = time.localtime()
    st2 = time.strptime('%s-%s-1'%(st.tm_year,st.tm_mon),'%Y-%m-%d')
    return time.mktime(st2)
print(func())

str_time1 = '2018-8-19 22:10:8'
str_time2 = '2018-8-20 11:10:8'
struct_t1 = time.strptime(str_time1,'%Y-%m-%d %H:%M:%S')
struct_t2 = time.strptime(str_time2,'%Y-%m-%d %H:%M:%S')
time_stamp1 = time.mktime(struct_t1)
time_stamp2 = time.mktime(struct_t2)
sub_time = time_stamp2-time_stamp1
gm_time = time.gmtime(sub_time)
print('过去了%d年%d月%d日%d时%d分%d秒'%(gm_time.tm_year-1970,gm_time.tm_mon-1,
                               gm_time.tm_mday-1,gm_time.tm_hour,gm_time.tm_min,gm_time.tm_sec))
