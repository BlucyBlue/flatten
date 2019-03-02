import unittest
from itertools import zip_longest

from flatten import flatten_all, flatten_all_no_dupl, flatten_all_it, flatten_all_it_no_dupl

class TestFlat(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('Setting up class')

	@classmethod
	def tearDownClass(cls):
		print('Tearing down class')

	def setUp(self):
		print('Setting up test')

		self.l1 = ['2',['4',67,'cvsadf'], ['mck',[['r'],],],]
		self.l1_flat = {i for i in ['2','4',67,'cvsadf', 'mck','r',]}
		self.l1_flat_all = {i for i in self.l1_flat}

		self.l2 = [(1,2),[('g','p',6),[[7,8,9],],],2390, 357]
		self.l2_flat = {i for i in [(1,2),('g','p',6),7,8,9,2390, 357]}
		self.l2_flat_all = {i for i in [(1,2),('g','p',6),7,8,9,2390, 357]}


	def tearDown(self):
		print('Dismantling test')

	def is_longest(self, l1, l2):
		if len(l1) > len(l2):
			return (l1, l2)
		return (l2, l1)

	def have_same_members(self, l1, l2):
		lists = self.is_longest(list(l1), list(l2))
		for i in lists[0]:
			if i not in lists[1]:
				return False
		return True


	def test_flatten_all(self):
		self.assertTrue(self.have_same_members(flatten_all(self.l1),self.l1_flat))
		self.assertTrue(self.have_same_members(flatten_all(self.l2),self.l2_flat))

	# l2 excluded because it cotnains a dict.
	def test_flatten_all_no_dupl(self):
		self.assertTrue(self.have_same_members(flatten_all_no_dupl(self.l1),set(self.l1_flat)))
		self.assertTrue(self.have_same_members(flatten_all_no_dupl(self.l2),set(self.l2_flat)))


	def test_flatten_all_it(self):
		self.assertTrue(self.have_same_members(flatten_all_it(self.l1),self.l1_flat_all))
		self.assertTrue(self.have_same_members(flatten_all(self.l2),self.l2_flat_all))


	# l2 excluded because it cotnains a dict.
	def test_flatten_all_it_no_dupl(self):
		self.assertTrue(self.have_same_members(flatten_all_it_no_dupl(self.l1),set(self.l1_flat_all)))
		self.assertTrue(self.have_same_members(flatten_all_it_no_dupl(self.l2),set(self.l2_flat_all)))

if __name__ == '__main__':
	unittest.main()