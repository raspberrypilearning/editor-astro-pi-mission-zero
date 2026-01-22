# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
z = (153, 50, 204) # Tail and fins
q = (255, 255, 0) # Body
d = (51, 153, 255) # Water
c = (0, 0, 0) # Eye

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # colour the fish eye

    image = [
        d, d, z, d, d, d, d, d,
        d, d, d, z, z, d, d, d,
        z, d, q, q, q, q, d, d,
        z, z, q, q, q, c, q, d,
        z, z, z, q, q, q, q, d,
        z, z, q, q, q, q, q, d,
        z, d, q, z, z, q, d, d,
        d, d, d, z, d, d, d, d
        ]

    # Display the image
    sense.set_pixels(image)
    sleep(1)