import re

mylist = ['https://localhost:8080/search?q=how+to+dispose+of+a+corpse&oq=how+to+dispose+of+a+corpse&aqs=chrome..69i57j69i64.4925j1j7&sourceid=chrome&ie=UTF-8',
    'http://www.google.com/101-things-to-do-with-a-dead-body_9780997711639?utm_source=google-shopping&utm_medium=cpc#dfsdfj8877']
def url_parser(s):
    
    try:
        scheme = re.findall('(\w+)://', s)[0]
    except IndexError: return "Enter the complete URL"
    
    try:
        host = re.findall('://([\da-z\.-]+)/?', s)
    except IndexError: host = ''
    
    port = []
    try:
        port = re.findall('://[\da-z.]*:([0-9]+)/?',s)[0]
    except IndexError:
        if not port:
            if scheme == 'http': port = '80'
            elif scheme == 'https' : port = '443'
            else: port = ''
        
   
    try:
        path = re.findall('\w(/[\d\w\-\_/]+)', s)[0]
    except IndexError: path = ''
   
    try:
        query = re.findall('\?([\w=\+&._:-]+)', s)[0]
    except IndexError: query = ''
   
    try:
        fragment = re.findall('#([\w=&._-]+)', s)[0]
    except IndexError: fragment = ''
   
   
    elements = {
        'scheme': scheme ,
        'host':  host,
        'port' : port ,
        'path': path ,
        'query': query,
        'fragment': fragment 
    }
   
    return elements
   
for x in mylist:
    print(url_parser(x))