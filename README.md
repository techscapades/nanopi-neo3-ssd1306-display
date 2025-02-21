On Nanopi Neo3 armbian:
1. install docker
2. docker pull ubuntu
3. wget https://raw.githubusercontent.com/techscapades/nanopi-neo3-ssd1306-display/main/oled_setup.sh -O /home/$USER/oled_setup.sh
4. docker run -t -d --privileged --network host --name oled_info -v /home/$USER/oled_setup.sh:/oled_setup.sh ubuntu
5. docker exec -it oled_info /bin/bash
6. bash oled_setup.sh

Start the container:

docker start oled_info && docker exec -d oled_info python3 /oled/oled-display.py
