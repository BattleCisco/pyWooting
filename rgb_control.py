#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import traceback
import typing
import ctypes
import time


def started_and_connected(func):
	"""Wraps around the function to only run when the Wooting keyboard is connected."""
	
	def wrapper(*args, **kwargs):
		"""Runs this code before the function."""
		if KeyboardRGBControl.wooting_dll is None:
			print("WootingReader was not started.")
			return None
		
		if not KeyboardRGBControl.is_wooting_connected():
			print("Wooting keyboard is not connected.")
			return None
		
		return func(*args, **kwargs)
	
	return wrapper  # Wrapper function add something to the passed function and decorator returns the wrapper function


class KeyboardRGBControl:
	"""A Basic reader to allow for communicating with the Wooting (One) Keyboard. TODO: Support for Wooting Two when it arrives.
	
	Attributes:
		wooting_dll(): The loaded DLL file.
	"""

	wooting_dll = None

	@classmethod
	def start(cls, dllfile: str = "wooting-rgb-control.dll")->bool:
		"""This needs to be called before anything else.
		
		Args:
			dll_file(str): The filepath to the reader DLL file

		Returns:
			bool: True if it managed to load the DLL. False if it doesnt find the file.
		"""
		try:
			cls.wooting_dll = ctypes.cdll.LoadLibrary(dllfile)
			return True
		
		except OSError as e:
			traceback.print_exc()
		
		return False

	@classmethod
	def is_wooting_connected(cls)->bool:
		"""Returns if a wooting keyboard is detected or not.
		
		Returns:
			bool: True for detected, False otherwise.

		"""
		if cls.wooting_dll is not None:
			return bool(cls.wooting_dll.wooting_rgb_kbd_connected())
		return False

	@classmethod
	@started_and_connected
	def reset(cls)->typing.Union[bool, None]:
		"""Resets the keyboard to a the profile you've selected.
		
		Returns:
			bool: If any of the keys were changed, it returns True, False otherwise.
		"""
		return bool(cls.wooting_dll.wooting_rgb_reset())

	@classmethod
	@started_and_connected
	def direct_set_key(cls, row: int, column: int, red: int, green: int, blue: int)->typing.Union[bool, None]:
		"""Directly sets a key's lightning based on the RGB supplied.
		
		Args:
			row(int): Row for the key. 0 to 5
			column(int): Column for the key. 0 to 17 (21 for Wooting Two)
			red(int): Red value for the key. 0 to 255
			green(int): Green value for the key. 0 to 255
			blue(int): Blue value for the key. 0 to 255

		Returns:
			bool: True if the colour is set, False otherwise.
		"""
		return bool(cls.wooting_dll.wooting_rgb_direct_set_key(*(ctypes.c_byte(v) for v in [row, column, red, green, blue])))

	@classmethod
	@started_and_connected
	def direct_reset_key(cls, row: int, column: int)->typing.Union[bool, None]:
		"""Directly sets a key's lightning based on the RGB supplied.
		
		Args:
			row(int): Row for the key. 0 to 5
			column(int): Column for the key. 0 to 17 (21 for Wooting Two)
		
		Returns:
			bool: True if the colour is updated, False otherwise.
		"""
		return bool(cls.wooting_dll.wooting_rgb_direct_reset_key(*(ctypes.c_ubyte(v) for v in [row, column])))
	
	@classmethod
	@started_and_connected
	def set_auto_update(cls, auto_update: bool)->None:
		"""Sets if the keyboard should change after each set_array_** function, default is False.
		
		Args:
			auto_update(bool): If it should update after each change.

		Returns:
			None
			
		"""
		cls.wooting_dll.wooting_rgb_array_auto_update(ctypes.c_bool(auto_update))
	
	@classmethod
	@started_and_connected
	def set_array_key(cls, row: int, column: int, red: int, green: int, blue: int)->typing.Union[bool, None]:
		"""Sets an key within the rgb array stored on the keyboard, and changes the keyboard if the (set_auto_update) flag is set.
		
		Args:
			row(int): Row for the key. 0 to 5
			column(int): Column for the key. 0 to 17 (21 for Wooting Two)
			red(int): Red value for the key. 0 to 255
			green(int): Green value for the key. 0 to 255
			blue(int): Blue value for the key. 0 to 255

		Returns:
			bool: True if the colour is set, False otherwise.
		"""
		return bool(cls.wooting_dll.wooting_rgb_array_set_single(*(ctypes.c_byte(v) for v in [row, column, red, green, blue])))

	@classmethod
	@started_and_connected
	def set_array(cls, array: typing.List[int])->typing.Union[bool, None]:
		"""Sets the rgb array stored on the keyboard, size must be specifically 6*21*3 (rows * colums * rgb)
		
		Args:
			array(list): List containing all the values for all the RGB on the keyboard.

		Returns:
			bool: True if colours are changed, False otherwise.
		"""
		if len(array) == 6*21*3:
			c_array = (ctypes.c_uint8 * (6*21*3))(*(v for v in array))
			return bool(cls.wooting_dll.wooting_rgb_array_set_full(c_array))
	
	@classmethod
	@started_and_connected
	def update_rgb_array(cls)->typing.Union[bool, None]:
		return bool(cls.wooting_dll.wooting_rgb_array_update_keyboard())
	
def main():
	"""A simple test on all the LED's"""
	print("Starting")
	KeyboardRGBControl.start()
	print("Loaded DLL file")
	
	print("Keyboard connected", KeyboardRGBControl.is_wooting_connected())
	
	print("Setting entire keyboard to 0")
	KeyboardRGBControl.set_array([0 for v in range(6*21*3)])
	print("Updating keyboard")
	KeyboardRGBControl.update_rgb_array()
	print("Updated!")
	
	print("Settings RGB on 0, 0 to Red")
	KeyboardRGBControl.direct_set_key(8, 25, 600, 0, 0)
	print("Written the changes.")
	
	print("Waiting 1 sec")
	time.sleep(1)
	for j in range(15):
		for i in range(17):
			for k in range(6):
				KeyboardRGBControl.direct_set_key(
					k,
					i,
				    255 if i % 3 == 0 else 0,
					255 if i % 3 == 1 else 0,
					255 if i % 3 == 2 else 0)
				
			time.sleep(0.05 * (1 - j/15))
			for k in range(6):
				KeyboardRGBControl.direct_set_key(k, i, 0, 0, 0)
	
	print("Waiting 5 sec")
	time.sleep(5)
	print("Waited.")
	print("Resetting keyboard.")
	KeyboardRGBControl.reset()
	print("Keyboard resetted.")
	
if __name__ == "__main__":
	main()