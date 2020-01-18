# Fuel Consumption - Python Script to Domoticz
Python script to handle Fuel Consumption in Domoticz
If you like this project, or you wants to support the development, you can do that with the paypal link https://www.paypal.me/GModla. Or simply invite me a Coffee. :)
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/mgabor74)

## Prerequisites

Tested and works with Domoticz v4.x.

If you do not have a working Python >=3.5 installation, please install it first! 


## Installation
1. Create 6 Virtual Sensor in Domoticz
	- Total distance (km)
	- Fuel (liter)
	- Total cost (Euro or $ or..)
	- Actual distance (km)
	- Fuel consumption (Euro/100km)
	- Actual cost (Euro/km)

Note down the IDX value for the virtual sensor.

2. Clone repository into your domoticz/scripts/python folder
```
cd domoticz/scripts/python
git clone https://github.com/mgabor-bp/FuelConsumption.git
```
3. Modify the Fuel.py 
	- set the Domoticz server parameter
	- change the IDX of virtual sensor
	
4. Run the script
e.g. python3 fuel.py 100 2 5
	- where 100 Total distance
	- where 2 Fuel
	- where 5 Total cost
