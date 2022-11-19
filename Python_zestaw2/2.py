import datetime
import time

while True:
    now = datetime.datetime.now()
    t = str(now.second)
    if len(t) == 1:
        t = '0' + t
    print('\r',chr(16),now.hour,':',now.minute,':',t,chr(17),end='')
    time.sleep(0.5)
