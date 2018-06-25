#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import traceback
import typing
import ctypes
import time


def started_and_connected(func):
	"""Wraps around the function to only run when the Wooting keyboard is connected.
	
	Args:
		func(function): The function to ONLY run when the keyboard is connected and the DLL loaded.

	Returns:
		function: But with an wrapper that only runs the function if the keyboard is detected.

	"""
	
	def wrapper(*args, **kwargs):
		"""Runs this code before the function."""
		if KeyboardReader.wooting_dll is None:
			print("WootingReader was not started.")
			return None
		
		if not KeyboardReader.is_wooting_connected():
			print("Wooting keyboard is not connected.")
			return None
		
		return func(*args, **kwargs)
	
	return wrapper


class KeyboardReader:
	"""A wrapper to allow for communicating with a Wooting Keyboard."""
	
	wooting_dll = None
	
	@classmethod
	def start(cls, dll_file: str="wooting-analog-reader.dll")->bool:
		"""This needs to be called before anything else.
		
		Args:
			dll_file(str): The filepath to the reader DLL file

		Returns:
			bool: True if it managed to load the DLL. False if it doesnt find the file.
		
		"""
		try:
			cls.wooting_dll=ctypes.cdll.LoadLibrary(dll_file)
			return True
		
		except OSError as e:
			traceback.print_exc()
		
		return False
	
	@classmethod
	def is_wooting_connected(cls)->bool:
		"""Returns if a Wooting keyboard is detected.
		
		Returns:
			bool: True for connected, False for not connected.
		
		"""
		if cls.wooting_dll is not None:
			return bool(cls.wooting_dll.wooting_kbd_connected())
		return False
	
	@classmethod
	@started_and_connected
	def read_analog(cls, row: int, column: int)->typing.Union[int, None]:
		"""Reads the analog value for a key on the specified row and column.
		
		Args:
			row(int): Row for the key. 0 to 5
			column(int): Column for the key. 0 to 17 (21 for Wooting Two)

		Returns:
			int: Analog value for the key corresponding to the row and column.
		
		"""
		return int(cls.wooting_dll.wooting_read_analog(*(ctypes.c_ubyte(v) for v in [row, column])))
	
	@classmethod
	@started_and_connected
	def read_full_buffer(cls, items: int)->typing.Union[typing.Tuple[typing.List[int], typing.List[int], int], None]:
		"""Reads the buffer and returns the keys scan code and analog value.
		
		Args:
			items: The maximum items it will read. MUST be between 1 and 32

		Returns:
			tuple: The data in each positions of the tuple, more specified after the function. List can be empty ([scan codes], [analog values], keys in buffer)
		
		"""
		items = min(max(1, items), 32)  # type: int
		
		data = (ctypes.c_uint8 * (items * 2))(*(0 for i in range(items * 2)))
		items_returned = cls.wooting_dll.wooting_read_full_buffer(data, ctypes.c_uint32(items))
		if data:
			return [data[2 * i] for i in range(items_returned)], \
			       [data[2 * i + 1] for i in range(items_returned)], \
			       items_returned
		return [], [], 0

def main():
	"""Testing the module."""
	KeyboardReader.read_analog(0, 0)
	
	if KeyboardReader.start():
		print("Wooting KeyboardReader started.")
	else:
		print("Failed to start KeyboardReader")
		quit()
	
	i = 0
	t0 = time.time()
	while True:
		ret = KeyboardReader.read_full_buffer(32)
		i += 1
		print(ret)
		scan_codes, analog_values, buffer = ret
		print(round(i/(time.time()-t0), 3), scan_codes, analog_values, buffer)
		
if __name__ == "__main__":
	main()
