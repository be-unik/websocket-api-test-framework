from datetime import datetime

import json
import pytest
import pytz
import time
from websocket import create_connection

from config import *

""" Tests related to instrument ticker are present in this test script """

"""
TEST SETUP - Before running the tests
"""


@pytest.fixture(scope="module")
def setup(request):
    global ws
    ws = create_connection(BASE_URL)
    ws.settimeout(15)

    def teardown():
        ws.send(MESSAGE.get("unsubscribe_4"))
        ws.close()
        print('\n End of Tests')

    request.addfinalizer(teardown)


"""
Helper Function
"""


def time_passed(old_time):
    return time.time() - old_time


"""
TEST 1: Verify connection is established successfully.
Tests - 
1. Response contains 'connected' string in response
"""


def test_successful_connection(setup):
    ws.send(MESSAGE.get("connect"))
    response_message = ws.recv()
    assert response_message == 'connected', "Connection Failed"


"""
TEST 2: Verify ticker data with invalid id fields.
Tests - 
1. Response contains E
2. Response contains error

More relevant tests or cases related to invalid ticker can be added
"""


def test_instrument_ticker_with_invalid_id():
    ws.send(MESSAGE.get("subscribe_4_invalid_string"))
    response_message = ws.recv()
    data = json.loads(response_message.split(' ')[2])
    # print('instrument ticker error %s' % response_message)                                #### for debugging
    assert response_message.split(' ')[1] == 'E', "Incorrect Response received"
    assert "error" in data.keys(), "Error information not in response"


"""
TEST 3: Verify ticker data with valid id fields.
Tests - 
1. Response contains bid key
2. Response contains last key
3. Response is received between 8hrs an 24 hrs CET

More relevant tests related to ticker can be added
"""


def test_instrument_ticker_with_valid_id(setup):
    ws.send(MESSAGE.get("subscribe_4_valid_string"))
    old_time = time.time()
    msg_count = 0
    current_time_cet = datetime.now(pytz.timezone('Europe/Berlin'))
    today8hrs = datetime.now(pytz.timezone('Europe/Berlin')).replace(hour=8, minute=0, second=0, microsecond=0)
    today22hrs = datetime.now(pytz.timezone('Europe/Berlin')).replace(hour=22, minute=0, second=0, microsecond=0)
    while time_passed(old_time) < 10:
        response_message = ws.recv()
        data = json.loads(response_message.split(' ')[2])
        # print('instrument ticker response %s' % response_message)                        #### for debugging
        assert response_message.split(' ')[1] == 'A', "Incorrect Response received"
        assert "bid" in data.keys(), "Bid information not in response"
        assert "last" in data.keys(), "Last information not in response"
        msg_count += 1
    if today8hrs < current_time_cet < today22hrs:
        assert msg_count > 0, 'Message count < 0 in operating hours'
    else:
        assert msg_count <= 0, 'Message count > 0 in non-operating hours'
