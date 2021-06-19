""" Configuration for Environments can be specified here """

""" [Production] """
""" {'api_url': '', 'token': ''} """

""" [Staging] """
""" {'api_url': '', 'token': ''} """

""" [Dev] """
""" {'api_url': '', 'token': ''} """

BASE_URL = "wss://api.dev.neontrading.com"
MESSAGE = {
    "connect": b'connect 21 {"device": "FDF93099-8A6B-4C95-AC5C-463937AFF51D", "clientId": "cta", "clientVersion": "1.0.1", "platformId": "ios", "platformVersion": "10.2", "locale": "de"}',
    "invalid_connect": b'connect 12 {"locale": "de"}',
    "subscribe_4_valid_string": b'sub 4 {"type":"ticker","id":"US36467W1099.LSX"}',
    "subscribe_4_invalid_string": b'sub 4 {{"type":"ticker"},"id":"US36467W1099.LSX"}',
    "subscribe_2_valid_string": b'sub 2 {"type":"instrument","id":"US36467W1099"}',
    "subscribe_2_invalid_string": b'sub 2 {{"type":"instrument"},"id":"US367W1099"}',
    "unsubscribe_2": b'unsub 2',
    "unsubscribe_4": b'unsub 4'}
