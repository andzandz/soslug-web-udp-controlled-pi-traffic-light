This code is by Andy K, SoSLUG, largely aimed at teachers and educators getting started but is suitable for anyone. Use as you wish.

To use this code on your Raspberry Pi, download as ZIP (or git clone if you wish) and extract. Next, open a Terminal and install Apache web server with PHP:
(the $ character at the start of the line is simply to show this is a terminal command, do not copy the $ character)

$ sudo apt-get install apache2 php5

Now, connect the Pi to any network (using a router with a wired cable or WiFi adapter) and check the Pi's network address with

$ ifconfig

You are looking for a line next to eth0(wired) or wlan0(WiFi) beginning with "inet addr:". It will be 4 numbers with 3 dots in between, for example 192.168.1.70. If you don't see the IP address (4 numbers with 3 dots) then you aren't connected to any network yet; you need to fix your network configuration.

You must go into the code in index.html and change the 192.168.1.70 in index.html for your Pi's correct IP address. You may want to set a static ip address so it will not change in future: 
http://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address

Next, the contents of the "www" folder must be copied into /var/www. So /var/www/index.html and so on. You may have to use a "sudo cp" command for this. On some systems (Raspbian Jessie?) this might be /var/www/html/index.html instead. The PHP file is also important and must be placed in this folder.
For example: (cd into the extracted www folder first)

$ sudo cp index.html /var/www/

Once this is done, open a terminal (SSH in, plug in a screen and keyboard or otherwise), cd into the python directory and run

$ sudo python recv_lights.py 

You will want a PiStop or LEDs connected to pins 8,10,12 and ground(pin 6).

On a computer or smartphone on the same wired/wireless network, browse to http://your-pi-ip-address. For example http://192.168.1.70. Do not search or google for the IP address, it will not be found as it is not on the internet. On this page, press the traffic light buttons and if configured correctly it will work!

I made a more elaborate, complicated version, uploaded on our SoSLUG site: http://soslug.org/andys-udp-rpi-traffic-light-system-demo/
