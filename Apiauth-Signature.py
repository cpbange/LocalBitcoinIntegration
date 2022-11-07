import hmac
import time
import hashlib


hmac_key = ""
hmac_secret = ""

nonce = int(time.time())


'''Change to Desired Endpoint'''
api_endpoint ="/api/notifications/"


'''Change'''
url = "https://localbitcoins.com/api/notifications"


get_or_post_params_urlencoded = "application/x-www-form-urlencoded"

message = str(nonce) + hmac_key + api_endpoint + get_or_post_params_urlencoded

message_bytes = message.encode('utf-8')

signature = hmac.new(hmac_secret.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()
