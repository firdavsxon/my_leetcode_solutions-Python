def word_count_engine(document):
	if not document:
		return []

	d = {}

	for i in document:
		if i == '.' or i == '!' or i == ',' or i == "'":
			document= document.replace(i, '')

	# splitted_words = document.split(' ')
	splitted_words = []
	window_start = 0
	for window_end, char in enumerate(document):
		if char == ' ':
			splitted_words.append(document[window_start:window_end])
			window_start = window_end + 1
		if window_end == len(document) - 1:
			splitted_words.append(document[window_start:window_end+1])
	for word in splitted_words:
		d[word.lower()] = d.get(word.lower(), 0) + 1

	sorted_list = sorted(([key, str(value)] for key, value in d.items()), key=lambda x: x[1], reverse=True)

	return sorted_list


document = "Practice makes perfect. you'll onlyget Perfect by practice. just practice!"
print(word_count_engine(document))
print(word_count_engine("Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"))


