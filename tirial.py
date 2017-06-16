#! shebang
import requests
from bs4 import Beautifuld as bs
import re

# link = 'https://thepiratebay.org/top/48hall'	#for table
# link = 'http://www.sosmath.com/tables/mult/mult.html'
link = 'http://www.amazon.in/gp/product/B01FXJI1OY/ref=s9u_simh_gw_i1?ie=UTF8&pd_rd_i=B01FXJI1OY&pd_rd_r=6MC68A46F4MC0HSTWCN0&pd_rd_w=f7RCQ&pd_rd_wg=aSHq6&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=02TQC36D2EK7QJDC86KN&pf_rd_t=36701&pf_rd_p=2a1cc6da-e857-48b9-afc7-813e8aacf476&pf_rd_i=desktop'
# link = 'https://www.sastodeal.com/product/thule-subterra-15quot-macbook-sleeve'
# link = 'http://www.kaymu.com.np/pack-of-3-check-printed-boxer-multi-color-1732681.html'
resp = requests.get(link).text
d = bs(resp, 'lxml')

table = d.find_all('table', id = 'a-lineitem')

for row in table.find_all('tr'):
	print(row)






# a = []

# for x in d.find_all('span'):
# 	a.append(x.string)
# a = a[:2]
# print(a)
# price = re.findall(r'(\d*)/-', a[1])
# print('price= ', price)
# for x in d.find_all('meta'):
# 	a.append(x.get('data-track-price_local'))
# for x in a: 
# 	if x != None: a = x
# print(a)

# ext = re.findall(r'www\.(.*)\.com', link)[0]
# print(ext)

# table = d.find('table', id = "searchResult")
# # print(table)
# a= []; b = []; c = []
# for row in table.find_all('tr'):
# 	cells = row.find_all('td')
# 	# print(type(cells))
# 	if len(cells) == 6:
# 		a.append(cells)
# 		print(a)



 # d = d.prettify()
print(d.title.string)


