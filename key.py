import typing
import enum

_i = -1

def i(): # Horrible way to Enum, but I'm lazy, sorry.
	global _i
	_i += 1
	return _i

class WootingKey:
	"""Represents a Wooting Key, not meant to be initialized."""
	
	class ScanCodes(enum.Enum):
		"""Scan Codes with an ugly Enum, sorry."""
		Escape=i()
		F1=i()
		F2=i()
		F3=i()
		F4=i()
		F5=i()
		F6=i()
		F7=i()
		F8=i()
		F9=i()
		F10=i()
		F11=i()
		F12=i()
		Printscreen=i()
		Pause=i()
		Mode=i()
		Tilde=i()
		Number1=i()
		Number2=i()
		Number3=i()
		Number4=i()
		Number5=i()
		Number6=i()
		Number7=i()
		Number8=i()
		Number9=i()
		Number0=i()
		Underscore=i()
		Plus=i()
		Backspace=i()
		Insert=i()
		Home=i()
		Tab=i()
		Q=i()
		W=i()
		E=i()
		R=i()
		T=i()
		Y=i()
		U=i()
		I=i()
		O=i()
		P=i()
		OpenBracket=i()
		CloseBracket=i()
		Backslash=i()
		Delete=i()
		End=i()
		CapsLock=i()
		A=i()
		S=i()
		D=i()
		F=i()
		G=i()
		H=i()
		J=i()
		K=i()
		L=i()
		Colon=i()
		Quote=i()
		Enter=i()
		PageUp=i()
		PageDown=i()
		Up=i()
		ModifierLeftShift=i()
		Z=i()
		X=i()
		C=i()
		V=i()
		B=i()
		N=i()
		M=i()
		Comma=i()
		Dot=i()
		Slash=i()
		ModifierRightShift=i()
		Left=i()
		Down=i()
		Right=i()
		ModifierRightCtrl=i()
		ModifierLeftCtrl=i()
		ModifierLeftUi=i()
		ModifierLeftAlt=i()
		Spacebar=i()
		ModifierRightAlt=i()
		ModifierRightUi=i()
		FnKey=i()
		ExtraIso=i()
		
	@staticmethod
	def get_key_coordinates(scan_code: int)->typing.Union[tuple, None]:
		"""This returns the coordinates for any scan code.
		
		Args:
			scan_code: The int for the key's scan code.

		Returns:
			tuple: Containing the coordinates of the corresponding key.
			None: If the scan code is not recognized.

		"""
		if scan_code in wooting_key_dict:
			return wooting_key_dict[scan_code]
		return None

del _i # No longer needed, so deleted.

wooting_key_dict = {
	#Row 0
	WootingKey.ScanCodes.Escape: (0, 0),
	WootingKey.ScanCodes.F1: (0, 2),
	WootingKey.ScanCodes.F2: (0, 3),
	WootingKey.ScanCodes.F3: (0, 4),
	WootingKey.ScanCodes.F4: (0, 5),
	WootingKey.ScanCodes.F5: (0, 6),
	WootingKey.ScanCodes.F6: (0, 7),
	WootingKey.ScanCodes.F7: (0, 8),
	WootingKey.ScanCodes.F8: (0, 9),
	WootingKey.ScanCodes.F9: (0, 10),
	WootingKey.ScanCodes.F10: (0, 11),
	WootingKey.ScanCodes.F11: (0, 12),
	WootingKey.ScanCodes.F12: (0, 13),
	WootingKey.ScanCodes.Printscreen: (0, 14),
	WootingKey.ScanCodes.Pause: (0, 15),
	WootingKey.ScanCodes.Mode: (0, 16),
	#Row 1
	WootingKey.ScanCodes.Tilde: (1, 0),
	WootingKey.ScanCodes.Number1: (1, 1),
	WootingKey.ScanCodes.Number2: (1, 2),
	WootingKey.ScanCodes.Number3: (1, 3),
	WootingKey.ScanCodes.Number4: (1, 4),
	WootingKey.ScanCodes.Number5: (1, 5),
	WootingKey.ScanCodes.Number6: (1, 6),
	WootingKey.ScanCodes.Number7: (1, 7),
	WootingKey.ScanCodes.Number8: (1, 8),
	WootingKey.ScanCodes.Number9: (1, 9),
	WootingKey.ScanCodes.Number0: (1, 10),
	WootingKey.ScanCodes.Underscore: (1, 11),
	WootingKey.ScanCodes.Plus: (1, 12),
	WootingKey.ScanCodes.Backspace: (1, 13),
	WootingKey.ScanCodes.Insert: (1, 14),
	WootingKey.ScanCodes.Home: (1, 15),
	WootingKey.ScanCodes.PageUp: (1, 16),
	#Row 2
	WootingKey.ScanCodes.Tab: (2, 0),
	WootingKey.ScanCodes.Q: (2, 1),
	WootingKey.ScanCodes.W: (2, 2),
	WootingKey.ScanCodes.E: (2, 3),
	WootingKey.ScanCodes.R: (2, 4),
	WootingKey.ScanCodes.T: (2, 5),
	WootingKey.ScanCodes.Y: (2, 6),
	WootingKey.ScanCodes.U: (2, 7),
	WootingKey.ScanCodes.I: (2, 8),
	WootingKey.ScanCodes.O: (2, 9),
	WootingKey.ScanCodes.P: (2, 10),
	WootingKey.ScanCodes.OpenBracket: (2, 11),
	WootingKey.ScanCodes.CloseBracket: (2, 12),
	#WootingKey.ScanCodes.Backslash: (2, 13),
	WootingKey.ScanCodes.Delete: (2, 14),
	WootingKey.ScanCodes.End: (2, 15),
	WootingKey.ScanCodes.PageDown: (2, 16),
	#Row 3
	WootingKey.ScanCodes.CapsLock: (3, 0),
	WootingKey.ScanCodes.A: (3, 1),
	WootingKey.ScanCodes.S: (3, 2),
	WootingKey.ScanCodes.D: (3, 3),
	WootingKey.ScanCodes.F: (3, 4),
	WootingKey.ScanCodes.G: (3, 5),
	WootingKey.ScanCodes.H: (3, 6),
	WootingKey.ScanCodes.J: (3, 7),
	WootingKey.ScanCodes.K: (3, 8),
	WootingKey.ScanCodes.L: (3, 9),
	WootingKey.ScanCodes.Colon: (3, 10),
	WootingKey.ScanCodes.Quote: (3, 11),
	WootingKey.ScanCodes.Backslash: (3, 12),
	WootingKey.ScanCodes.Enter: (3, 13),
	#Row 4
	WootingKey.ScanCodes.ModifierLeftShift: (4, 0),
	WootingKey.ScanCodes.ExtraIso: (4, 1),
	WootingKey.ScanCodes.Z: (4, 2),
	WootingKey.ScanCodes.X: (4, 3),
	WootingKey.ScanCodes.C: (4, 4),
	WootingKey.ScanCodes.V: (4, 5),
	WootingKey.ScanCodes.B: (4, 6),
	WootingKey.ScanCodes.N: (4, 7),
	WootingKey.ScanCodes.M: (4, 8),
	WootingKey.ScanCodes.Comma: (4, 9),
	WootingKey.ScanCodes.Dot: (4, 10),
	WootingKey.ScanCodes.Slash: (4, 11),
	#WootingKey.ScanCodes.Slash: (4, 11),
	WootingKey.ScanCodes.ModifierRightShift: (4, 13),
	#Empty
	WootingKey.ScanCodes.Up: (4, 15),
	#Empty
	#Row 5
	WootingKey.ScanCodes.ModifierLeftCtrl: (5, 0),
	WootingKey.ScanCodes.ModifierLeftUi: (5, 1),
	WootingKey.ScanCodes.ModifierLeftAlt: (5, 2),
	#Empty
	#Empty
	#Empty
	WootingKey.ScanCodes.Spacebar: (5, 6),
	#Empty
	#Empty
	#Empty
	WootingKey.ScanCodes.ModifierRightAlt: (5, 10),
	WootingKey.ScanCodes.ModifierRightUi: (5, 11),
	WootingKey.ScanCodes.FnKey: (5, 12),
	WootingKey.ScanCodes.ModifierRightCtrl: (5, 13),
	WootingKey.ScanCodes.Left: (5, 14),
	WootingKey.ScanCodes.Down: (5, 15),
	WootingKey.ScanCodes.Right: (5, 16),
	
	#WootingKey.ScanCodes.ExtraIso: (5, 17)
}