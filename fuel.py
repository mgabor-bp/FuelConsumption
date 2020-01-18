# Tested in Python 3.5.3
import datetime  # Importing the datetime library
from time import sleep      # Importing the time library to provide the delays in program
import json
import urllib.request
import requests
import base64
import time
import sys

# Settings for the domoticz server

domoticzserver   = "127.0.0.1:8080"
domoticzusername = ""
domoticzpassword = ""


# Create virtual sensors in dummy hardware

# Sensor IDs
idx_act_tkm="44"
idx_act_fuel="45"
idx_act_tcost="46"
idx_act_km="47"
idx_act_consumption="48"
idx_act_cost="49"


base64string = base64.encodestring(('%s:%s' % (domoticzusername, domoticzpassword)).encode()).decode().replace('\n', '')


def domoticzrequest (url):
  print(url)
  request = urllib.request.Request(url)
  request.add_header("Authorization", "Basic %s" % base64string)
  response = urllib.request.urlopen(request)
  return response.read()

def domoticzread(idx,RData):
    url = "http://" + domoticzserver + "/json.htm?type=devices&rid=" + idx
    response = requests.get(url)
    jsonData = json.loads(response.text)
    #print(jsonData)
    result = jsonData["result"][0][RData]
    return result;

def domoticzrequest (url):
    #print(url)
    request = urllib.request.Request(url)
    request.add_header("Authorization", "Basic %s" % base64string)
    response = urllib.request.urlopen(request)
    return response.read()

def domoticzread2(idx,RData):
    url = "http://" + domoticzserver + "/json.htm?type=devices&rid=" + idx
    response = requests.get(url)
    jsonData = json.loads(response.text)
    #print(jsonData)
    result = jsonData["result"][0][RData]
    result2=result.split(" ",1)
    return result2[0];

def domoticzwrite(idx,WData):
    domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx + "&nvalue=0&svalue=" + WData)
    
def calculation_fuel(act_tkm,act_fuel,act_tcost):
    err=""
    last_km=domoticzread2(idx_act_tkm,"Data")
    try:
      act_km=round(float(act_tkm)-float(last_km),2)
    except: err = err+"act_km err;"
    try:
      act_consumption=round((float(act_fuel)/act_km)*100,2)
    except: err = err+"act_consuption err;"
    try:
      act_cost=round(float(act_tcost)/act_km,2)
    except: err =err+"act_cost err;"  
    if err =="":
      domoticzwrite(idx_act_tkm,str(act_tkm))
      domoticzwrite(idx_act_fuel,str(act_fuel))
      domoticzwrite(idx_act_tcost,str(act_tcost))
      domoticzwrite(idx_act_km,str(act_km))
      domoticzwrite(idx_act_consumption,str(act_consumption))
      domoticzwrite(idx_act_cost,str(act_cost))
      result=str(act_km) + " km;" + str(act_consumption) + " l/100km;" + str(act_cost) + " Ft/km"
      return result
    else: return err

print(len(sys.argv))
if len(sys.argv)==4:
  result=calculation_fuel(sys.argv[1],sys.argv[2],sys.argv[3])
  print(result)
else:
  print("Missing parameter")
