# Cisco DNA Center  Platform Example
Cisco DNA Center assurance has a powerful network correlation engine to generate network issues or events. 
Cisco DNA Center platform can be used to post these events to a webhook.

The server module is an example of this.

To simulate events coming into the server (so you do not need to break your network) the client program can be used 
to send some mock data.

## Running the server
Install the requirements and then the server can be run as follows

```buildoutcfg
./server.py 
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on https://0.0.0.0:9000/ (Press CTRL+C to quit)

```

You can change the port number in the server.py module.   If you change the server you will also need to change the client.
 
NOTE:  THe server needs to be running https in order for Cisco DNA Center to communicate with it.  I have used an adhoc SSL context in the sample code

## Running the client
If you run the client with no arguments, a list of valid options will be displayed, including the available examples

```buildoutcfg
/client.py 
Run with --event and a valid example.
Valid Examples:ap_down_eg, ap_flap_eg, border_dhcp_eg, device_unreachable_eg, swim_eg
```

When run with a valid example, the example payload it sent to the server to be processed.
```buildoutcfg
./client.py --event device_unreachable_eg
Sending:device_unreachable_eg
200

```

You can check the server logs to see the event being received.

