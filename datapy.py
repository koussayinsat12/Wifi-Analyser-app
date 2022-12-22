import func as f
import time
import csv
from datetime import datetime
fieldnames=[]
fieldnames.append("time")
for i in f.get_dataSSID():
    fieldnames.append(i)

#create a dataset of the SSID and the power Signal of each Wifi-Hotspot 
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info={}
        l=[]
        for i in fieldnames:
            if(i not in f.get_dataSSID()):
                l.append(i)
        for i in fieldnames:
            if(i!="time"):
                if(i not in l)&(i in f.get_dataSignal()):
                    info[i]=(f.get_dataSignal()[i])
                else:
                    info[i]=0
            else:
                t = datetime.now().time()
                seconds = (t.hour * 60 + t.minute) * 60 + t.second
                info[i]=seconds
        print(info)
        csv_writer.writerow(info)
    time.sleep(1)
