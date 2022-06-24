"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Sample Input
07:05:45PM

Sample Output
19:05:45

"""


input_time: str = '12:00:00AM'
time:str = input_time[0:-2]
time_level: str = input_time.replace(time,'')
time_slot = time.split(':')
hh:str = time_slot[0]
mm:str = time_slot[1]
ss:str = time_slot[2]
if ((time_level != 'AM' and time_level != 'PM') or (int(time_slot[0]) > 12) or (int(time_slot[1]) > 59) or (int(time_slot[2]) > 59)): raise Exception('Invalid Time Input')
if(int(time_slot[0]) == 12 and time_level == 'AM'): hh = '00'
elif(int(time_slot[0]) < 12 and time_level == 'PM'): hh = str(int(time_slot[0]) + 12)
print(str(hh)+':'+str(time_slot[1])+':'+str(time_slot[2]))