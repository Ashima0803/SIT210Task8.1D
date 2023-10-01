import smbus2
import time

BH1750_ADDRESS = 0x23

bus = smbus2.SMBus(1)

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

        return lux

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if _name_ == "_main_":
    try:
        while True:
            current_light = light_level()

            if current_light is not None:
                print(f"Intensity of light: {current_light:.2f} lux")
                if current_light < 100:
                    print("Too dark, very dim light.")
                elif current_light < 1000:
                    print("Medium level, Optimum light.")
                else:
                    print("Too bright, very intense light.")

            time.sleep(5)

    except KeyboardInterrupt:
        pass
