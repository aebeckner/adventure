import adventure
import unittest
from io import StringIO
from unittest.mock import patch

class TestAdventure(unittest.TestCase):

	def test_get_room_desc(self):
		expected = "You're currently in the control center of your spacecraft good ole Betsy. Try taking off!\n"

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.get_room_desc(1,0)
			self.assertEqual(fake_out.getvalue(), expected)

	def test_valid_connection(self):
		self.assertTrue(adventure.valid_connection(4))
		self.assertFalse(adventure.valid_connection(3))

	def test_check_user_input_invalid(self):
		expected = "Invalid input. Try again.\n"
		adventure.user_input = "invalid"

		#fake_out variable = mock object in this case invalid output value
		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)
	
	def test_check_user_input_quit(self):	
		expected = "Goodbye!\n\n"
		adventure.user_input = "quit"

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)

	def test_check_user_input_up(self):
		adventure.valid_connection(2)
		adventure.user_input = "up"
		expected = "You cannot move up\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)

	def test_check_user_input_down(self):
		adventure.valid_connection(3)
		adventure.user_input = "down"
		expected = "You cannot move down\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)	

	def test_check_user_input_north(self):
		adventure.valid_connection(4)
		adventure.user_input = "north"
		expected = "You cannot move north\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)

	def test_check_user_input_south(self):
		adventure.valid_connection(5)
		adventure.user_input = "south"
		expected = "You cannot move south\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)

	def test_check_user_input_east(self):
		adventure.valid_connection(6)
		adventure.user_input = "east"
		expected = "You've landed on planet Nuthinmuch. Not much 'round these parts best we head back to the ship.\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)

	def test_check_user_input_west(self):
		adventure.valid_connection(7)
		adventure.user_input = "west"
		expected = "You're currently in the control center of your spacecraft good ole Betsy. Try taking off!\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)

	def test_check_user_input_look(self):
		adventure.user_input = "look"
		expected = "You've landed on planet Nuthinmuch. Not much 'round these parts best we head back to the ship.\n" 

		with patch('sys.stdout', new = StringIO()) as fake_out: 
			adventure.check_user_input()
			self.assertEqual(fake_out.getvalue(), expected)


	#mock check input to check if it was called
	@patch("adventure.check_user_input")
	def test_run_main_loop(self, mock):
		adventure.user_input = "quit"
		adventure.run_main_loop()
		self.assertFalse(mock.called)

	#mock run loop to check if it was called
	@patch("adventure.run_main_loop")
	def test_main(self, mock):
		adventure.main()
		self.assertTrue(mock.called)
		
if __name__ == '__main__':
	unittest.main()