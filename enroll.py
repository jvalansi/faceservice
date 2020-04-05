from urllib2 import Request, urlopen
import re


img_reg = '<img src="([^\"]+)" alt="([^\"]+)"[^>]*>'
url = "https://www.pornhub.com/pornstars"

def enroll(link, name):
    values = """
      {
        "image": "%s",
        "subject_id": "%s",
        "gallery_name": "MyGallery"
      }
    """ % (link, name)
    print(values)
    headers = {
      'Content-Type': 'application/json',
      'app_id': '0f3787a6',
      'app_key': 'c956c35367fe23b2918914ea22b91c47'
    }
    request = Request('https://api.kairos.com/enroll', data=values, headers=headers)

    response_body = urlopen(request).read()
    print response_body


if __name__ == "__main__":

    html = urlopen(url).read()
    images = re.findall(img_reg, html)
    for link, name in images:
        print(link)
        enroll(link, name)
