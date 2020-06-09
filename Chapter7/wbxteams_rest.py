#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Webex Teams REST Demo Interaction.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Russell Johnston"
__email__ = "rujohns2@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import os
import random
import requests

# Set target URL and get environement variable for authenticating requests
URL = 'https://webexapis.com/v1/messages'
ACCESS_TOKEN = os.getenv('WEBEX_TEAMS_ACCESS_TOKEN')

ROOM_ID = '{{Enter Room ID}}'
MESSAGE_TEXT = f'Random number sent using native REST: {random.randint(1,999)}'

# format header for request
headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN,
    'Content-Type': 'application/json;charset=utf-8'
}

# store message content to variable
data = {'roomId': ROOM_ID, 'text': MESSAGE_TEXT}

# Sends a message with a random number to the Room ID
response = requests.post(URL, json=data, headers=headers)

# Prints the details of response to the request sent
try:
    response.raise_for_status()
    message_id = response.json()['id']
    message_text = response.json()['text']
    print(f'New message created, with ID:\n{message_id}')
    print(message_text)
except requests.exceptions.HTTPError as error:
    print(error)
