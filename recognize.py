from urllib2 import Request, urlopen

values = """
  {
    "image": "https://scontent-sjc2-1.xx.fbcdn.net/v/t1.0-9/22552436_10155828210329321_2867180897686600177_n.jpg?oh=3852b4fcf5d0b8026b041408aed9144e&oe=5ACC21BF",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': '0f3787a6',
  'app_key': 'ic956c35367fe23b2918914ea22b91c47'
}
request = Request('https://api.kairos.com/recognize', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
