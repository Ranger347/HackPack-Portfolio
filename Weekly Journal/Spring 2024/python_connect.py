from urllib.request import urlopen

def connect():
	url = "http://hackpack.club"
	page = urlopen(url)
	html_bytes = page.read()
	html = html_bytes.decode("utf-8")
	print(html)

#call the function
connect()

for i in range(10):
	if i == 5:
		print("five")
	else:
		connect()

