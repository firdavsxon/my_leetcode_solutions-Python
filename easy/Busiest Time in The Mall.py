def find_busiest_period(data):
	max_people_time = {}
	people = 0

	for i in range(len(data)):
		if data[i][0] not in max_people_time:
			max_people_time[data[i][0]] = 0

	for i in range(len(data)):

		if data[i][2] == 1:
			people += data[i][1]
			max_people_time[data[i][0]] = people

		elif data[i][2] == 0:
			people -= data[i][1]
			max_people_time[data[i][0]] = people
	max_time = 0
	people_amount = 0
	for key, value in max_people_time.items():
		if value > people_amount:
			people_amount = value
			max_time = key

	return max_time


# print(find_busiest_period(data = [ [1487799425, 14, 1],
#                  [1487799425, 4,  0],
#                  [1487799425, 2,  0],
#                  [1487800378, 10, 1],
#                  [1487801478, 18, 0],
#                  [1487801478, 18, 1],
#                  [1487901013, 1,  0],
#                  [1487901211, 7,  1],
#                  [1487901211, 7,  0] ]))
# print(find_busiest_period([[1487799425,21,1],[1487799425,4,0],[1487901318,7,0]]))


def remove_duplicate(nums):
	next_not_duplicate = 1
	i = 1
	while i < len(nums):
		if nums[next_not_duplicate - 1] != nums[i]:
			nums[next_not_duplicate] = nums[i]
			next_not_duplicate += 1
		i += 1
	return next_not_duplicate


# print(remove_duplicate([2, 3, 3, 3, 6, 9, 9]))

def flatten_dictionary(dictionary):
	final_dict = {}
	for key, value in dictionary.items():
		if isinstance(value, dict):
			rec_func(key, value, final_dict)
		else:
			final_dict[key] = value

	return final_dict


def rec_func(key, val, final_dict):
	for rec_key, rec_val in val.items():
		if not isinstance(rec_val, dict):
			temp_name = key
			temp_name = temp_name + '.' + rec_key
			final_dict[temp_name] = rec_val

		if isinstance(rec_val, dict):
			key = key + '.' + rec_key
			rec_func(key, rec_val, final_dict)


dictio = {
	"Key1": "1",
	"Key2": {
		"a": "2",
		"b": "3",
		"c": {
			"d": "3",
			"e": {
				"": "1"
			}
		}
	}
}

d = {"Key1": "1", "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": "1"}}}
print(flatten_dictionary(d))


def amazon_q(states, days):
	temp = states[:]
	while days > 0:
		states = temp[:]

		if temp[0] == 1 and states[1] == 0:
			temp[0] = 0
		elif states[0] == 0 and states[1] == 1:
			temp[0] = 1

		if states[len(states)-1] == 1 and states[len(states)-2] == 0:
			temp[len(states)-1] = 0
		elif states[len(states)-1] == 0 and states[len(states)-2] == 1:
			temp[0] = 1
		
		for cell in range(1, len(states)-2+1):
			if states[cell-1] == 1 and states[cell+1] == 0:
				temp[cell] = 1
			elif states[cell-1] == 0 and states[cell+1] == 1:
				temp[cell] = 1
			elif states[cell-1] == 0 and states[cell+1] == 0:
				temp[cell] = 0
			elif states[cell-1] == 1 and states[cell+1] == 1:
				temp[cell] = 0
		days -= 1
	return temp


states = [1, 0, 0, 0, 0, 1, 0, 0]
states1 = [1, 1, 1, 0, 1, 1, 1, 1]
print(amazon_q(states, 1))
print(amazon_q(states1, 2))
