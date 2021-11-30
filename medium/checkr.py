# Name Matching
#
#   At Checkr, one of the most important aspects of our work is accurately matching records
# to candidates. One of the ways that we do this is by comparing the name on a given record
# to a list of known aliases for the candidate. In this exercise, we will implement a
# `name_match` method that accepts the list of known aliases as well as the name returned
# on a record. It should return True if the name matches any of the aliases and False otherwise.
#
# The name_match method will be required to pass the following tests:
#
# 1. Exact match
#
#   known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']
#   name_match(known_aliases, 'Alphonse Gabriel Capone') => True
#   name_match(known_aliases, 'Al Capone')               => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => False
#
#
# 2. Middle name missing (on alias)
#
#   known_aliases = ['Alphonse Capone']
#   name_match(known_aliases, 'Alphonse Gabriel Capone') => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => True
#   name_match(known_aliases, 'Alexander Capone')        => False
#
#
# 3. Middle name missing (on record name)
#
#   known_aliases = ['Alphonse Gabriel Capone']
#   name_match(known_aliases, 'Alphonse Capone')         => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => False
#   name_match(known_aliases, 'Alexander Capone')        => False
#
#
# 4. More middle name tests
#    These serve as a sanity check of your implementation of cases 2 and 3
#
#   known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']
#   name_match(known_aliases, 'Alphonse Gabriel Capone') => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => True
#   name_match(known_aliases, 'Alphonse Edward Capone')  => False
#
#
# 5. Middle initial matches middle name
#
#   known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
#   name_match(known_aliases, 'Alphonse G Capone')       => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => True
#   name_match(known_aliases, 'Alphonse E Capone')       => False
#   name_match(known_aliases, 'Alphonse Edward Capone')  => False
#   name_match(known_aliases, 'Alphonse Gregory Capone') => False
#
#
# Bonus: Transposition
#
# Transposition (swapping) of the first name and middle name is relatively common.
# In order to accurately match the name returned from a record we should take this
# into account.
#
# All of the test cases implemented previously also apply to the transposed name.
#
#
# 6. First name and middle name can be transposed
#
#   'Gabriel Alphonse Capone' is a valid transposition of 'Alphonse Gabriel Capone'
#
#   known_aliases = ['Alphonse Gabriel Capone']
#   name_match(known_aliases, 'Gabriel Alphonse Capone') => True
#   name_match(known_aliases, 'Gabriel A Capone')        => True
#   name_match(known_aliases, 'Gabriel Capone')          => True
#   name_match(known_aliases, 'Gabriel Francis Capone')  => False
#
#
# 7. Last name cannot be transposed
#
#   'Alphonse Capone Gabriel' is NOT a valid transposition of 'Alphonse Gabriel Capone'
#   'Capone Alphonse Gabriel' is NOT a valid transposition of 'Alphonse Gabriel Capone'
#
#   known_aliases = ['Alphonse Gabriel Capone']
#   name_match(known_aliases, 'Alphonse Capone Gabriel') => False
#   name_match(known_aliases, 'Capone Alphonse Gabriel') => False
#   name_match(known_aliases, 'Capone Gabriel')          => False

def name_match(known_aliases, record_name):
	# Implement me
	if record_name in known_aliases:
		return True

	def middle_name_missing():
		first_name = record_name.split(" ")[0]
		last_name = record_name.split(" ")[1]

		# ['Alphonse Capone', "john doe taylor"]

		for name in known_aliases:

			alias_first_name = name.split(' ')[0]
			alias_last_name = name.split(' ')[-1]
			if alias_first_name != first_name:
				return False
			elif alias_last_name != last_name:
				return False
		return True

	def middle_name_missing_2():
		if record_name in known_aliases:
			return True
		if len(known_aliases.split(" ")) > 2:
			if len(record_name.split(" ")) == 2:
				if known_aliases.split(" ")[0] != record_name.split(" ")[0]:
					return False
			elif known_aliases.split(" ")[-1] != record_name.split(" ")[-1]:
				return False

			if len(record_name.split(" ")) > 2:
				if known_aliases.split(" ")[1] != record_name.split(" ")[1]:
					return False
		return True

	if exact_match() or middle_name_missing():
		return True

	return False


### Tests ###

def assert_equal(expected, result, error_message):
	if expected != result:
		print(error_message)
		print('expected: %s' % expected)
		print('actual: %s' % result)
		print('')


def run_tests():
	known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']
	assert_equal(True, name_match(known_aliases, 'Alphonse Gabriel Capone'), 'error 1.1')
	assert_equal(True, name_match(known_aliases, 'Al Capone'), 'error 1.2')
	assert_equal(False, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 1.3')

	known_aliases = ['Alphonse Capone']
	assert_equal(True, name_match(known_aliases, 'Alphonse Gabriel Capone'), 'error 2.1')
	assert_equal(True, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 2.2')
	assert_equal(False, name_match(known_aliases, 'Alexander Capone'), 'error 2.3')

	known_aliases = ['Alphonse Gabriel Capone']
	assert_equal(True, name_match(known_aliases, 'Alphonse Capone'), 'error 3.1')
	assert_equal(False, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 3.2')
	assert_equal(False, name_match(known_aliases, 'Alphonse Edward Capone'), 'error 3.3')

	known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']
	assert_equal(True, name_match(known_aliases, 'Alphonse Gabriel Capone'), 'error 4.1')
	assert_equal(True, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 4.2')
	assert_equal(False, name_match(known_aliases, 'Alphonse Edward Capone'), 'error 4.3')

	known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
	assert_equal(True, name_match(known_aliases, 'Alphonse G Capone'), 'error 5.1')
	assert_equal(True, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 5.2')
	assert_equal(False, name_match(known_aliases, 'Alphonse E Capone'), 'error 5.3')
	assert_equal(False, name_match(known_aliases, 'Alphonse Edward Capone'), 'error 5.4')
	assert_equal(False, name_match(known_aliases, 'Alphonse Gregory Capone'), 'error 5.5')

	known_aliases = ['Alphonse Gabriel Capone']
	assert_equal(True, name_match(known_aliases, 'Gabriel Alphonse Capone'), 'error 6.1')
	assert_equal(True, name_match(known_aliases, 'Gabriel A Capone'), 'error 6.2')
	assert_equal(True, name_match(known_aliases, 'Gabriel Capone'), 'error 6.3')
	assert_equal(False, name_match(known_aliases, 'Gabriel Francis Capone'), 'error 6.4')

	known_aliases = ['Alphonse Gabriel Capone']
	assert_equal(False, name_match(known_aliases, 'Alphonse Capone Gabriel'), 'error 7.1')
	assert_equal(False, name_match(known_aliases, 'Capone Alphonse Gabriel'), 'error 7.2')
	assert_equal(False, name_match(known_aliases, 'Capone Gabriel'), 'error 7.3')

	print('Test run finished')


if __name__ == "__main__":
	run_tests()
