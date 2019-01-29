#!/usr/bin/env python

import requests
import examples
from argparse import ArgumentParser
import logging

import json
requests.packages.urllib3.disable_warnings()
URL="https://localhost:9000"

def send_request(data):
    headers={'content-type': 'application/json'}
    response = requests.post(url=URL, data=json.dumps(data), headers=headers,verify=False)
    print response.status_code

if __name__ == "__main__":
    valid_examples = [call for call in dir(examples) if not "__" in call]

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
        print "Sending:{}".format(args.event)
        send_request(getattr(examples, args.event))
    else:
        print("Run with --event and a valid example.\nValid Examples:{}".format(", ".join(valid_examples)))
