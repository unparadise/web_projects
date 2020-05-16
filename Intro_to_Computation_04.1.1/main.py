# This is the finger exercise in Chapter 4.1.1
# Write a function isIn that accepts two strings
# as arguments and returns True if either string
# occurs in the other, and False otherwise.

import gi

def isIn(stringOne, stringTwo):
	if len(stringOne) > len(stringTwo):
		# print('String one is longer than string two')
		if stringOne.find(stringTwo) == -1:
			return False
		else:
			print('String two is in string one')
			return True
	elif len(stringOne) < len(stringTwo):
		# print('String one is shorter than string two')
		if stringTwo.find(stringOne) == -1:
			return False
		else:
			print('String one is in strnig two')
			return True
	else:
		# print('String one and string two are same length')
		if stringOne != stringTwo:
			return False
		else:
			print('String one and string two are the same')
			return True

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Compare strings")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()



strOne = input('Please enter the first string: ')
strTwo = input('Please enter the second string: ')

print('--------------------------------')
isIn(strOne, strTwo)
