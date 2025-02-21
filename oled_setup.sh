#!/bin/bash

# Update and upgrade system packages
apt-get update && apt-get upgrade -y && apt autoremove -y

# Install necessary packages
DEBIAN_FRONTEND=noninteractive apt install python3 python3-pip python3-pil python3-numpy python3-setuptools git htop nano curl wget i2c-tools python3-smbus iproute2 gawk mawk coreutils -y

# Install Python dependencies
pip3 install luma.oled pillow smbus2 --break-system-packages

# Create the /oled directory
mkdir -p /oled

# Download the OLED display script
wget https://raw.githubusercontent.com/techscapades/nanopi-neo3-ssd1306-display/main/oled-display.py -O /oled/oled-display.py

exit 0
