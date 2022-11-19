# YUVRAJ BANSAL
# TASK 8.1D
# 2110994799


# The Python library for SMBus can be used to communicate with I2C based devices.
import smbus 
# it is for the time complexity of the program
import time

# default address for the BH1750 sensor
BH1750_ADD = 0x23 
RES_MODE = 0x20 

# instance 
bus = smbus.SMBus(1)  

# reads the measurement taken from the device (but the reading comes in the form of 2 byte data)
def light_intensity (address, resolution):
  reading = bus.read_i2c_block_data(address, resolution)
  return conversion(reading)

# Converts the reading into decimal number into two byte data.
def conversion(input):
   return ((input[1] + (256 * input[0])) / 1.2)


def main():
   while True:
       # Reads the  value.
       value = light_intensity(BH1750_ADD, RES_MODE)
       # Prints the value on serial monitor
       print ("Light Intensity: " + str(value)) 

       if(value < 250):
           print("Void")
       elif(value < 650 and value > 250):
           print("Level 1")
       elif(value < 1300 and value > 650):
           print("Level 2")
       elif(value < 2000 and value > 1400):
           print("Level 3")
       elif(value > 2000):
           print("Extreme Level")

       time.sleep(1.0)

# Entry poin of the program
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Computation Stopped!!")