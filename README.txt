To use this code on your Pi, download as ZIP (or git clone if you wish) and extract. Next, install Apache web server with PHP:
(the $ character at the start of the line is simply to show this is a terminal command, do not copy the $ character)

$ sudo apt-get install apache2 php5

Next, the contents of the "www" folder must be copied into /var/www. So /var/www/index.html and so on. You may have to use a "sudo cp" command for this. On some systems (Raspbian Jessie?) this might be /var/www/html/index.html instead. The PHP file is also important and must be placed in this folder.
For example:

$ sudo cp index.html /var/www/

Now, connect the Pi to any network (using a router with a wired cable or WiFi adapter) and check the Pi's network address with

$ ifconfig

You are looking for a line next to eth0(wired) or wlan0(WiFi) beginning with "inet addr:". It will be 4 numbers with 3 dots in between, for example 192.168.1.70.

You must go into the code and change the 192.168.1.70 in index.html for your Pi's correct IP address. You may want to set a static ip address so it will not change in future: 

Once this is done, open a terminal (SSH in, plug in a screen and keyboard or otherwise), cd into the python directory and run

$ sudo python recv_lights.py 
