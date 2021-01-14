import mh_z19
import random
import string
import os
import sys
import fileinput
import calendar
import time

from asciimatics.screen import Screen

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def update_ssid():
	new_ssid = get_random_alphanumeric_string(5)

	for line in fileinput.input('/etc/hostapd/hostapd.conf', inplace=True):
	    if line.strip().startswith('ssid='):
	        line = 'ssid=CO2-' + new_ssid + '\n'
	    sys.stdout.write(line)

def restart_wifi():
	os.popen('sudo systemctl stop dnsmasq')
	os.popen('sudo systemctl stop hostapd')
	
	os.popen('sudo service hostapd start')
	os.popen('sudo service dnsmasq start')
	os.popen('sudo clear')
	
def store_new_CO2_read(reading):
	for line in fileinput.input('/etc/nodogsplash/htdocs/splash.html', inplace=True):
		if line.strip().startswith('<!-- CURRENT_READING -->'):
			line = '<!-- CURRENT_READING --><h1 style="text-align: center;">' + str(reading) + ' PPM</h1>\n'

		if line.strip().startswith('<!-- CURRENT_ADVICES -->'):
			if reading <= 700 and reading < 1000:
				line = '<!-- CURRENT_ADVICES --><h2 style="text-align: center;"><span style="color: #008000;">Medición dentro de los valores adecuados</span></h2>\n'
			elif reading >= 1000 and reading <= 1400:
				line = '<!-- CURRENT_ADVICES --><h2 style="text-align: center;"><span style="color: #CCCC00;">La medición comienza a ser demasiado elevada</span></h2>\n'
			elif reading > 1400:
				line = '<!-- CURRENT_ADVICES --><h2 style="text-align: center;"><span style="color: #DC143C;">Medición por encima del umbral recomendado. Solicite ventilación inmediata</span></h2>\n'

		sys.stdout.write(line)

def setup_screen(screen):
	ssid = 'ERROR'
	
	hostapd_conf = open('/etc/hostapd/hostapd.conf', 'r') 
	hostapd_conf_lines = hostapd_conf.readlines()
	
	for line in hostapd_conf_lines:
	    if line.strip().startswith('ssid='):
	        ssid = line.split('=')[1]
	        break
	
	while True:
		new_reading = mh_z19.read()['co2']
		store_new_CO2_read(new_reading)
		
		new_reading_color_code = 7
		if new_reading <= 700 and new_reading < 1000:
			new_reading_color_code = 2
		elif new_reading >= 1000 and new_reading <= 1400:
			new_reading_color_code = 3
		elif new_reading > 1400:
			new_reading_color_code = 1
		
		screen.print_at(' WiFi:         ', 0, 1, 6, 2)
		screen.print_at('╔══════════════════╗', 0, 2, 7, 2)
		screen.print_at('  Red: ' + ssid, 0, 4, 2, 1)
		screen.print_at('╚══════════════════╝', 0, 6, 7, 2)
		screen.print_at(' Medición CO2:         ', 0, 9, 6, 2)
		screen.print_at('╔══════════════════╗', 0, 10, 7, 2)
		screen.print_at('  ' + str(new_reading) + ' PPM', 0, 12, new_reading_color_code, 1)
		screen.print_at('╚══════════════════╝', 0, 14, 7, 2)
		screen.refresh()
		time.sleep(1)

update_ssid()
restart_wifi()

Screen.wrapper(setup_screen)
