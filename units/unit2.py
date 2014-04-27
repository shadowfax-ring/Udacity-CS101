def get_next_target(page):
	start_link = page.find('<a href=')
	if (start_link == -1):
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

def print_all_links(page):
	while True:
		url, end_pos = get_next_target(page)
		if url:
			print url
			page = page[end_pos:]
		else:
			break 

def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"

# Examples
print_all_links(get_page('http://xkcd.com/353'))

url, end_pos = get_next_target('good')	# Multiple assignment in python
print url, end_pos

if (url):
	print "Yes"
else:
	print "No"

