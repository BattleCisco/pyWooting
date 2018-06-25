#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from reader import KeyboardReader
from rgb_control import KeyboardRGBControl
from key import WootingKey

import traceback
import time


def main():
	try:
		KeyboardReader.start()
		KeyboardRGBControl.start()
		
		key_presses = {}
		
		def set_black():
			for j in range(6):
				for i in range(17):
					KeyboardRGBControl.direct_set_key(j, i, int(0), int(0), int(0))
					KeyboardRGBControl.direct_set_key(j, i, int(0), int(0), int(0))
		
		set_black()
		while True:
			time.sleep(0.01)
			buffer = KeyboardReader.readFullBuffer(16)
			if buffer is not None:
				scan_codes, analog_value, pressed_keys = buffer
				if WootingKey.ScanCodes.Escape in scan_codes:
					raise Exception("Escape was pressed")
				for scan_code in scan_codes:
					#print(scan_code)
					if scan_code not in key_presses:
						if WootingKey.get_key_coordinates(scan_code) is not None:
							key_presses[scan_code] = (WootingKey.get_key_coordinates(scan_code), time.time())
			
			for key in list(key_presses.keys()):
				coordinates = key_presses[key][0]
				time_pressed = key_presses[key][1]
				
				if time.time() - time_pressed < 2:
					values = [coordinates[0], coordinates[1], 255, 255, 255]
					for i in range(3):
						values[2+i] = int(values[2+i] * ((time.time() - time_pressed) / 2))
					KeyboardRGBControl.direct_set_key(*values)
				elif time.time() - time_pressed >= 2 and time.time() - time_pressed <= 4:
					values = (coordinates[0], coordinates[1], 255, 255, 255)
					KeyboardRGBControl.direct_set_key(*values)
				elif time.time() - time_pressed > 4 and time.time() - time_pressed < 6:
					values = [coordinates[0], coordinates[1], 255, 255, 255]
					for i in range(3):
						values[2+i] = int(values[2+i] * (1 - ((time.time() - time_pressed - 4) / 2)))
					KeyboardRGBControl.direct_set_key(*values)
				elif time.time() - time_pressed >= 6:
					values = (coordinates[0], coordinates[1], 0, 0, 0)
					KeyboardRGBControl.direct_set_key(*values)
					del key_presses[key]
			
	except Exception as e:
		print(e)
		traceback.print_exc()
		KeyboardRGBControl.reset()


if __name__ == "__main__":
	main()