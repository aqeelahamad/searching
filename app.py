import requests
from requests_oauthlib import OAuth1

BASE_URL = u'https://api.twitter.com/1.1/'

client_key = u'OWEFrGWjcUPyTFHhHnT2Q'
client_secret = u'b120PIQFjz8l2TNijVxf3vkyK1o7f7sFaBqhyeTFc'
resource_owner_key = u'1746056306-2QatczLqgaO5XMGyBuxqPaPVHN8JW5R6kJcEx9g'
resource_owner_secret = u'SsWUGJOcJtSaS9zRQz9I8bkgMvF21DpxUcTmgbM'

oauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret)

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')


queryoauth = OAuth1(client_key, client_secret,
                    resource_owner_key, resource_owner_secret,
                    signature_type='query')


bodyoauth = OAuth1(client_key, client_secret,
                   resource_owner_key, resource_owner_secret,
                   signature_type='body')

				   

payload = {'q': 'afeezaziz'}
url = 'https://api.twitter.com/1.1/search/tweets.json?q=afeezaziz'
r = requests.get(url, auth=oauth)
print r.json() 
