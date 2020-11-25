""" 
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

Example

For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]
For
  dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Chicken", "Chicken Curry", "Quesadilla"],
                            ["Nuts", "Fried Rice", "Salad"],
                            ["Onions", "Fried Rice", "Pasta"]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string dishes

An array of dishes, where dishes[i] for each valid i contains information about the ith dish: dishes[i][0] is the name of the dish, and all the elements after it are the ingredients of that dish. Both the dish name and the ingredient names consist of English letters and spaces. It is guaranteed that all dish names are different. It is also guaranteed that the ingredient names for any one dish are also pairwise distinct.

Guaranteed constraints:
1 ≤ dishes.length ≤ 500,
2 ≤ dishes[i].length ≤ 10,
1 ≤ dishes[i][j].length ≤ 50.

[output] array.array.string

The array containing the grouped dishes.
"""


def groupingDishes(dishes):
	hash_map = {}
	for l in dishes:
		hash_map[l[0]] = l[1:]
	ingridients = []
	for list in dishes:
		for ing in list[1:]:
			ingridients.append(ing)
	ingridients_count = {}

	temp = []
	for ingridient in ingridients:
		if ingridient not in ingridients_count:
			ingridients_count[ingridient] = 1
		elif ingridient in ingridients_count:
			ingridients_count[ingridient] += 1
		if ingridients_count[ingridient] > 1 and ingridients_count[ingridient] not in temp:
			temp.append(ingridient)
	temp.sort()

	output = {}


	for key, val in hash_map.items():
		for j in temp:
			if j not in output:
				output[j] = []
			if j in val:
				output[j].append(key)

	out = []
	for key, val in output.items():
		val.sort()
	for key, val in output.items():
		temp = []
		temp.append(key)
		for v in val:
			temp.append(v)
		out.append(temp)


	return out


dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
print(groupingDishes(dishes))











