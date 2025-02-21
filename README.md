On Nanopi Neo3 armbian:
1. install docker
2. docker pull ubuntu
3. docker run -t -d --privileged --network host --name oled_info ubuntu
4. docker exec -it oled_info /bin/bash

Inside oled_info container:
apt-get update && apt-get upgrade -y && apt autoremove -y
DEBIAN_FRONTEND=noninteractive apt install python3 python3-pip python3-pil python3-numpy python3-setuptools git htop nano curl wget i2c-tools python3-smbus iproute2 gawk mawk coreutils -y
pip3 install luma.oled pillow smbus2 --break-system-packages
mkdir oled
wget https://raw.githubusercontent.com/techscapades/nanopi-neo3-ssd1306-display/main/oled-display.py -O /oled/oled-display.py
python3 /oled/oled-display.py

Start the container:
docker start oled_info
