from websocket import create_connection
import pytest
from config import *

""" Tests related to instrument data are present in this test script """

"""
TEST SETUP - Before running the tests
"""


@pytest.fixture(scope="module")
def setup(request):
    global ws
    ws = create_connection(BASE_URL)

    def teardown():
        ws.send(MESSAGE.get("unsubscribe_2"))
        ws.close()
        print('\n End of Tests')

    request.addfinalizer(teardown)


"""
TEST 1: Verify connection fails with invalid connection request.
Tests - 
1. Response contains 'failed' string in response
"""


def test_fail_connection(setup):
    ws.send(MESSAGE.get("invalid_connect"))
    result = ws.recv()
    print('Result is - %s' % result)
    assert 'failed' in result, "Connection didn't fail"


"""
TEST 2: Verify connection is established successfully.
Tests - 
1. Response contains 'connected' string in response
"""


def test_successful_connection():
    ws.send(MESSAGE.get("connect"))
    response_message = ws.recv()
    assert response_message == 'connected', "Connection Failed"


"""
TEST 3: Verify instrument data with correct id and type
Tests - 
1. Response contains A

More relevant tests related to instrument data can be added
"""


def test_instrument_data():
    ws.send(MESSAGE.get("subscribe_2_valid_string"))
    response_message = ws.recv()
    # print('instrument data %s' % response_message)                                #### for debugging
    # print('parsed message %s' % response_message.split(' ')[2])                   #### for debugging
    assert response_message.split(' ')[1] == 'A', "Incorrect Response received"


"""
TEST 3: Verify instrument data with incorrect id
Tests - 
1. Response contains E

More relevant tests related to instrument data can be added
"""


def test_instrument_data_with_invalid_id(setup):
    ws.send(MESSAGE.get("subscribe_2_invalid_string"))
    response_message = ws.recv()
    # print('instrument data %s' % response_message)                                #### for debugging
    # print('parsed message %s' % response_message.split(' ')[2])                   #### for debugging
    assert response_message.split(' ')[1] == 'E', "Incorrect Response received"
