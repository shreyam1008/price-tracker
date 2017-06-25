import requests
import bs4
import re
#addition
class PriceTrack:
this is some changes
	def __init__(self, link):
		self.link = link
		self.resp = requests.get(self.link)
		self.soup = bs4.BeautifulSoup(self.resp.text, 'lxml')

	def new_price(self, old_price):
		#add .com or .in both using reguarl exp
		site = re.findall(r'www\.(.*)\.com', self.link)[0]
		print('old price {} to new price {}'.format(old_price, self.current_price(site)))

	def current_price(self, site):
		a = []
		if site == 'kaymu':
			for x in self.soup.find_all('meta'): a.append(x.get('data-track-price_local'))
			for x in a: 
				if x != None: a = int(x)
		if site == 'sastodeal':
			for x in self.soup.find_all('span'): a.append(x.string)
			a = int(re.findall(r'(\d*)/-', a[1])[0])
		if site == 'amazon':
			pass
		if site == '':
			pass
		return a


def main():
	a = PriceTrack(link = 'http://www.kaymu.com.np/goldstar-fusion-sport-shoes-for-men-red-blue-1731628.html')
	a.new_price(old_price = 4500)

	# b = PriceTrack(link = 'https://www.sastodeal.com/sastodeal/faces/product.jsp?cts=1&pbi=51&pil=293')
	# b.new_price(old_price = 1000)

# 

if __name__ == "__main__": main()
# 
