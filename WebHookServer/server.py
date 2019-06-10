#!/usr/bin/env python
from __future__ import print_function
from flask import Flask
from flask import request
app = Flask(__name__)

from webex_teams import post_message
#from gmail import send_mail


def format_event(event):

    header = 'Event:{}, Severity:{}, Category:{}\n'.format(event['title'],
                                                      event['severity'],
                                                      event['category'])
    message = '{}\n'.format(event['description'])

    message += "\nSuggested Actions:\n"
    if event['title'] == "Device Image Outdated":
        device = event['enrichmentInfo']['connectedDevice'][0]['deviceDetails']
        image = event['enrichmentInfo']['imageDetails']['goldenImage']['imageVersion']
        message += "Update device {}[{}] running {} to {}\n".format(device['hostname'],
                                                             device['managementIpAddress'],
                                                             device['softwareVersion'],
                                                             image)
    else:
        for action in event['enrichmentInfo']['issueDetails']['issue'][0]['suggestedActions']:
            message += " -{}\n".format(action['message'])
    return header, message

def handle(event):
    '''
    handles and event.  Can send an email, or message to webex.
    :param event:
    :return:
    '''
    header, message = format_event(event)
    print(message)

    # send to webex
    post_message("*******\n" + header + message)

    # send an email
    #send_mail(header,message)

@app.route('/', defaults={'path': ''}, methods=['GET','POST'])
@app.route('/<path:path>', methods=["GET","PUT","POST","DELETE"])
def get_all(path):
    print("Method {}, URI {}".format(request.method,path))
    if request.method == "POST":
        print (request.headers)
        print (request.json)
        handle(request.json)
    return ("OK")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9000", ssl_context='adhoc')
