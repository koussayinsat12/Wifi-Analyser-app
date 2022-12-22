import subprocess
import re
import math as m
#get the Signal power of each wifi-Hotspot and their ssid in a dictionary using get_dataSignal 
def get_dataSignal():
    p = subprocess.Popen("netsh wlan show networks mode=Bssid", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode("unicode_escape").strip()
    m=re.findall("SSID.*?:.*?([\u0020-\u007e]{8,63}).*?Signal.*?:.*?([0-9]*)%",out,re.DOTALL)
    D_Signal={}
    for i in m:
        ListeSignal=i[0].lstrip()
        D_Signal[ListeSignal]=int(i[1])
    p.communicate()
    return(D_signal)
#get the Reception power 
def get_dataReception():
        p = subprocess.Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode("unicode_escape").strip()
        m=re.findall("R.ception.*?:.*?(\d{1,4}.\d{0,3})",out,re.DOTALL)
        p.communicate()
        return(m[0])
 #get all the SSID of the Wifi-Hotspots nearby you in a liste
def get_dataSSID():
     p = subprocess.Popen("netsh wlan show networks", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     out = p.stdout.read().decode("unicode_escape").strip()
     m=re.findall("SSID.*?:.*?([\u0020-\u007e]{8,63})",out,re.DOTALL)
     p.communicate()
     ListeSSID=[]
     for i in m:
          ListeSSID.append(i.lstrip())
     return(ListeSSID)
