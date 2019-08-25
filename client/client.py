#!/usr/bin/env python
from __future__ import print_function
import requests
from examples.ap_down_eg import ap_down_eg
from examples.ap_flap_eg import ap_flap_eg
from examples.border_dhcp_eg import border_dhcp_eg
from examples.device_unreachable_eg import device_unreachable_eg
from examples.swim_eg import swim_eg
from examples.new_flap_eg import new_flap_eg

from argparse import ArgumentParser
import logging

import json
requests.packages.urllib3.disable_warnings()
URL="https://localhost:9000"

def send_request(data):
    headers={'content-type': 'application/json'}
    response = requests.post(url=URL, data=json.dumps(data), headers=headers,verify=False)
    print(response.status_code)

if __name__ == "__main__":

    # strange python2 thing, need to reference call outside of the comprehension, otherwise get
    #RuntimeError: dictionary changed size during iteration
    call = ""
    valid_examples = [call for call in globals() if  "_eg" in call]

    parser = ArgumentParser(description='Select options.')

    parser.add_argument('--event', type=str, required=False,
                        help="event to send.  Valid events:[{}]".format(" | ".join(valid_examples)))

    parser.add_argument('-v', action='store_true',
                        help="verbose")
    args = parser.parse_args()
    if args.v:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug("valid examples:{}".format(", ".join(valid_examples)))
    if args.event in valid_examples:
        print("Sending:{}".format(args.event))
        send_request(locals()[args.event])
    else:
        print("Run with --event and a valid example.\nValid Examples:{}".format(", ".join(valid_examples)))
