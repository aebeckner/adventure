# Nano Adventure
import csv
from PIL import Image

room_id = 1
desc = 1
user_input = ""

with open('space_cowboy.csv','r') as csv_file:
	# read all lines of file
	reader=csv.reader(csv_file)
	# use list to find wanted row in file
	row=[r for r in reader]

def get_room_desc(new_id, conn):
	global room_id
	global im
	room_id = int(row[new_id][conn])
	print(row[room_id][desc])
	#im = Image.open(row[room_id][8])
	#im.show()

def valid_connection(direction):
	if row[room_id][direction] != "0":
		return True
	else:
		return False

def check_user_input():
	if user_input == "up" and valid_connection(2):
		get_room_desc(room_id, 2)
	elif user_input == "down" and valid_connection(3):
		get_room_desc(room_id, 3)
	elif user_input == "north" and valid_connection(4):
		get_room_desc(room_id, 4)
	elif user_input == "south" and valid_connection(5):
		get_room_desc(room_id, 5)
	elif user_input == "east" and valid_connection(6):
		get_room_desc(room_id, 6)
	elif user_input == "west" and valid_connection(7):
		get_room_desc(room_id, 7)
	elif user_input == "look":
		get_room_desc(room_id, 0)
	elif user_input == "quit":
		print("Goodbye!\n")
	elif user_input != "up" and user_input != "down" and user_input != "north" and user_input != "south" and user_input != "east" and user_input != "west" and user_input != "look" and user_input != "quit":
		print("Invalid input. Try again.")
	else:
		print("You cannot move " + user_input)

def run_main_loop():
	global user_input
	while user_input != "quit":
		user_input = input("> ").lower().strip()
		print("")
		check_user_input()

def main():
	global im
	print("\nHowdy Space Cowboy! There's a wanted Martian on the loose and it's your mission to find him! Gather your favorite spurs and get ready to take off!\n")
	print(row[room_id][desc])
	im = Image.open("spacecowboy.jpg")
	im.show()
	run_main_loop()

if __name__ == '__main__':
	main()