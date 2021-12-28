
# class for buying and selling with offers
class Operation:
	def __init__(self):
		self.buying_offers = {}  # collection of buying offers
		self.selling_offers = {}  # collection of selling offers

	def buy(self, offer):   # buying operation
		if len(self.selling_offers) == 0:  # means if there is no selling offers yet
			self.buying_offers[offer] = self.buying_offers.get(offer, 0) + 1 # we add
			print(f"There is no selling offer yet")
			return
		min_selling_offer = min(self.selling_offers)
		if offer < min_selling_offer:
			self.buying_offers[offer] = self.buying_offers.get(offer, 0) + 1
			print(f"Could not find selling offer for this buying offer")
			return
		elif offer >= min_selling_offer:
			self.selling_offers[min_selling_offer] -= 1
			if self.selling_offers[min_selling_offer] == 0:
				del self.selling_offers[min_selling_offer]
			print(f"Selling offer with price ${min_selling_offer} has been found and accepted")
			return

	def sell(self, offer):
		if len(self.buying_offers) == 0:
			self.selling_offers[offer] = self.selling_offers.get(offer, 0) + 1
			print(f"No buying offers exists")
			return
		max_buying_offer = max(self.buying_offers)
		if offer > max_buying_offer:
			self.selling_offers[offer] = self.selling_offers.get(offer, 0) + 1
			print("No buyer offer exits at this price range")
			return
		if offer <= max_buying_offer:
			self.buying_offers[max_buying_offer] -= 1
			if self.buying_offers[max_buying_offer] == 0:
				del self.buying_offers[max_buying_offer]
			print(f"Offer accepted with price ${max_buying_offer}")
			return

	def __str__(self):
		return f"Total selling offers: {self.selling_offers} \nTotal buying offers: {self.buying_offers}"


buy_sell_book = Operation()
print(buy_sell_book)
buy_sell_book.buy(100)
buy_sell_book.buy(120)

buy_sell_book.sell(100)
buy_sell_book.sell(1000)
buy_sell_book.sell(1000)
buy_sell_book.sell(300)
buy_sell_book.sell(400)
buy_sell_book.sell(300)
buy_sell_book.buy(450)
print(buy_sell_book)

