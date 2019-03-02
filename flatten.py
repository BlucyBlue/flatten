"""
I needed to extract nested lists for a personal project, so I came up with a couple of solutions.

Should be easy to customize and modify result format as needed.

If you find the need to, use as you wish.
"""


"""
Flattens all nested lists (all levels), but does not extract members of other iterables.
For eficiensy in working with larger datasets, returns a generator object.
"""

def flatten_all(my_list):
	for element in my_list:
		if isinstance(element, list):
			for nested_element in flatten_all(element):
				yield nested_element
		else:
			yield element


"""
Returns a set object from the generator resulting from flatten_all.
Will throw an exception if my_list contains dictionaries.
"""

def flatten_all_no_dupl(my_list):
	return set(flatten_all(my_list))


"""
Flattens all nested lists (all levels), and breaks down all iterables except strings.
For eficiensy in working with larger datasets, returns a generator object.
"""

def flatten_all_it(my_list):
	for element in my_list:
		if isinstance(element, list):
			for nested_element in flatten_all(element):
				yield nested_element
		else:
			try:
				# Checks if the element is an iterable.
				iter(element)
				# If the element is a dictionary, extracts the values.
				if isinstance(element, dict):
					for nested_element in flatten_all_iterables((element[member] for member in element)):
						yield nested_element
				# If the element is a string, yields the string without braking it into separate chars.
				elif isinstance(element, str):
					yield element
				# If the element is another type of iterable, extracts all the elements.
				else:
					for nested_element in flatten_all_iterables((member for member in element)):
						yield nested_element
			except:
				yield element


"""
Returns a set object from the generator resulting from flatten_all_iterables
Will throw an exception if my_list contains dictionaries.
"""

def flatten_all_it_no_dupl(my_list):
	return set(flatten_all_it(my_list))