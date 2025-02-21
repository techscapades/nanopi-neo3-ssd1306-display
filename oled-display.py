import time
import subprocess
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont

# Adjustable settings
mac_label_font_size = 10  # Font size for 'MAC: ' string
mac_address_font_size = 15  # Font size for MAC address string
mac_label_position = (0, 2)  # Position for 'MAC: ' string
mac_address_position = (0, 17)  # Position for MAC address string

# Initialize I2C interface (check if your bus is /dev/i2c-0 or /dev/i2c-1)
serial = i2c(port=0, address=0x3C)  # Change port to 1 if using /dev/i2c-1

# Initialize SSD1306 display
oled = ssd1306(serial, width=128, height=32)

# Clear display
oled.clear()

# Create an image to draw on
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load fonts (adjust size based on the respective font size variables)
try:
    mac_label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", mac_label_font_size)
    mac_address_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", mac_address_font_size)
except:
    mac_label_font = ImageFont.load_default()
    mac_address_font = ImageFont.load_default()

# Get the MAC address from the command output
try:
    result = subprocess.check_output("ip link show end0 | awk '/ether/ {print $2}' | tr -d ':'", shell=True)
    mac_address = result.decode('utf-8').strip()  # Decode and strip any extra whitespace/newline
except subprocess.CalledProcessError as e:
    mac_address = "Error fetching MAC"

# Draw the 'MAC: ' label with its font size and position
draw.text(mac_label_position, "DEVICE ID: ", font=mac_label_font, fill=255)

# Draw the MAC address with its font size and position
draw.text(mac_address_position, mac_address, font=mac_address_font, fill=255)

# Display image on OLED
oled.display(image)

# Show for 5 seconds, then clear
time.sleep(5)
oled.clear()

