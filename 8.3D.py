import smbus2 #importing necessary libraries
import time

BH1750_ADDRESS = 0x23 #the address of the device

bus = smbus2.SMBus(1) # Initializing the SMBus for communicating

# Read light level
def light_level():
    try:
        # Start measuring
        bus.write_byte(BH1750_ADDRESS, 0x10)

        # Some delay
        time.sleep(0.2)

        # Read light intensity
        data = bus.read_i2c_block_data(BH1750_ADDRESS, 0x00, 2)

        # Lux calculation
        lux = (data[0] << 8 | data[1]) / 1.2

        return lux #the value is returned

    except Exception as e:
        print(f"Error: {str(e)}") #log if there is any error or exception
        return None

if _name_ == "_main_": #script being read
    try:
        while True:
            current_light = light_level() #value of lux from light_level is passed into current_light

            if current_light is not None: 
                print(f"Intensity of light: {current_light:.2f} lux") #the light intensity is printed if the value is not none
                if current_light < 100: #if intensity is less than 100lux 
                    print("Too dark, very dim light.") 
                elif current_light < 1000: #if intensity is between 100 lux and 1000 lux
                    print("Medium level, Optimum light.")
                else:
                    print("Too bright, very intense light.") #if intensity is more than 100lux 

            time.sleep(5)

    except KeyboardInterrupt:
        pass
