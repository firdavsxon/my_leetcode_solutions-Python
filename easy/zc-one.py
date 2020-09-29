# Take home assignment for Python
import pytest
import datetime

"""
# Let's Build a Vendor Availability system
While this exercise is not timed, spend no more than 50 minutes. Keep it clean,
succinct, and elegant.
## Problem
We need to know if a vendor (restaurant) is available to deliver a meal.
So given a list of upcoming meals, build a function that will tell us if
the vendor (restaurant) is available to take the order.
## Requirements
- input: take a vendor_id and a date
- output: True if the vendor is available, False if not
- A vendor is available if:
  - They have enough drivers for a concurrent delivery
  - As long as the delivery blackout period doesn't overlap 
  (30 minutes before for delivery and setup, and 10 minutes 
  after for returning back)
"""

# A list of meals to be delivered
meals = {
	"results": [
		{
			"vendor_id": 1,  # Vendor 1 will be serving
			"client_id": 10,  # Client 10 on
			"datetime": "2017-01-01 13:30:00"  # January 1st, 2017 at 1:30 pm
		},
		{
			"vendor_id": 1,
			"client_id": 40,
			"datetime": "2017-01-01 14:30:00"
		},
		{
			"vendor_id": 2,
			"client_id": 50,
			"datetime": "2017-01-01 13:30:00"
		},
		{
			"vendor_id": 2,
			"client_id": 60,
			"datetime": "2017-01-01 14:20:00"
		},
		{
			"vendor_id": 2,
			"client_id": 70,
			"datetime": "2017-01-01 15:30:00"
		},
		{
			"vendor_id": 3,
			"client_id": 51,
			"datetime": "2017-01-01 15:30:00"
		},
		{
			"vendor_id": 3,
			"client_id": 52,
			"datetime": "2017-01-01 15:35:00"
		},
		{
			"vendor_id": 3,
			"client_id": 53,
			"datetime": "2017-01-01 16:40:00"
		},
		{
			"vendor_id": 3,
			"client_id": 54,
			"datetime": "2017-01-01 17:20:00"
		},
		{
			"vendor_id": 3,
			"client_id": 55,
			"datetime": "2017-01-01 19:30:00"
		}

	]
}

# Driver information per vendor.
vendors = {
	"results": [
		{
			"vendor_id": 1,
			"drivers": 1
		},
		{
			"vendor_id": 2,
			"drivers": 3
		},
		{
			"vendor_id": 3,
			"drivers": 3
		}

	]
}


def is_vendor_available(vendor_id, date_time):
	meals_results = meals['results']
	drivers_result = vendors['results']
	# finding order times and collecting in the new list called 'meal_order_time'
	meal_order_time = [result['datetime'] for result in meals_results if result['vendor_id'] == vendor_id]
	drivers_count = 0

	for driver in drivers_result:  # finding count of drivers in this vendor
		if driver['vendor_id'] == vendor_id:
			drivers_count = driver['drivers']

	# return true if count of drivers + 1 is more than orders
	if drivers_count + 1 > len(meal_order_time):
		return True

	# we will looking for each time object in the list and insert new order time in proper place in the list,
	# since inserting takes O(n) time complexity to compare appending and sorting which takes O(nlogn)
	amount_of_orders = len(meal_order_time)
	for i in range(amount_of_orders):
		if meal_order_time[i] >= date_time:
			meal_order_time.insert(i, date_time)
			break
	if len(
			meal_order_time) == amount_of_orders:  # if length of the list didn't change, we will just append new date_time
		meal_order_time.append(date_time)

	# converting string format of time to datetime object for easier calculation of time slot
	meal_order_time = [datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S') for date_time_str in meal_order_time]
	# we will create a queue for counting drivers and order datetime objects
	driver_queue = []
	start = 0
	i = 0
	while i < len(meal_order_time):
		interval = i - start  # we will check for interval of drivers availability and orders time
		if interval == drivers_count:  # which means there is no driver in vendor
			# we are going to find time difference between first driver availability and next order
			time_delta = meal_order_time[i] - driver_queue[0]
			minutes = time_delta.total_seconds() / 60
			# since first driver will be coming back first to
			# vendor with rules of this assignment, if time difference of drivers coming back is less than 40 minutes
			# (30 minutes for setup and delivery + 10 minutes to return back to vendor = total 40) which means
			# first driver will not be able to make next order and we return False
			if minutes < 40:
				return False
			driver_queue = []  # first driver made it on time and we will start the queue again
			start = i  # also we will move starting point to start counting drivers availability
		driver_queue.append(meal_order_time[i])  # append order time to the queue
		i += 1
	return True


""" 
	Time complexity will be O(n) since in worst case we will be looping entire time objects list with 
length of n, time complexity for insert() function also will be O(n) in worst case we insert new date_time in the 
beginning of the list.
	Space complexity will be also 0(n) when we make new list of time objects with length of n.
"""


def test_unavailable_vendor():
	assert is_vendor_available(1, "2017-01-01 14:30:00") is False


def test_available_vendor():
	assert is_vendor_available(3, "2017-01-02 20:33:00") is True


test_unavailable_vendor()
test_available_vendor()

"""
Sanity tests
"""


def test_exceptions_get_caught():
	with pytest.raises(Exception) as e_info:
		x = 1 / 0


def test_sanity():
	assert 2 + 2 == 5


pytest.main()
