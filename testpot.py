# Potentiometer test 
# This works! 
# Need to wire input into Channel 0. 
# Potentiometer has three pins -- Vin, OUT and GND 

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time 

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P1)

# percentages using excel and spot readings appear to be:
# 1% = 1.115629v 
# 50% = 1.573429v 
# 100% = 2.040571v 
# observations seem to be fairly linear 
# 
# v = 1.106286 + (0.009343 * p)
# percentage = (voltage - 1.106286) / 0.009343
def percentage_from_voltage(voltage):
    return (voltage - 1.106286) / 0.009343 

while True: 
    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')
    print('% full:'+str(percentage_from_voltage(chan.voltage))+'%')
    time.sleep(0.5)
    

