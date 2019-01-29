ap_flap_eg={
  "category": "Warn",
  "status": "NEW",
  "domain": "Availability",
  "severity": "P3",
  "title": "AP Flap",
  "instanceId": "E-NETWORK-EVENT-AWfQFFNEowzDvHZ5iroF-1545384240398",
  "timestamp": 1545384240398,
  "actualServiceId": "CC:16:7E:92:2B:40",
  "tenantId": "5c1b2facb982eb004c36c5bd",
  "priority": "P3",
  "source": "DNAC",
  "version": "1.2.0",
  "enrichmentInfo": {
    "connectedDevice": [
      {
        "deviceDetails": {
          "cisco360view": "https://10.10.10.181/dna/assurance/home#networkDevice/undefined"
        }
      }
    ],
    "issueDetails": {
      "issue": [
        {
          "impactedHosts": [],
          "issueDescription": "This AP \"3800.63D4\" has disconnected from WLC \"WLC9800.adamlab.cisco.com\" and reconnected to WLC \"WLC9800.adamlab.cisco.com\".",
          "issueCategory": "Availability",
          "issueSeverity": "MEDIUM",
          "issueSummary": "AP \"3800.63D4\" has flapped.",
          "issuePriority": "",
          "issueTimestamp": 1545384240398,
          "issueEntityValue": "CC:16:7E:92:2B:40",
          "issueSource": "Cisco DNA",
          "issueEntity": "network_device",
          "issueName": "ap_flap",
          "suggestedActions": [
            {
              "message": "Test the Ethernet cable by performing a cable diagnostic check on the switch \"\" and port \"\". Use the following commands: test cable-diagnostics tdr interface \"\" show cable-diagnostics tdr interface \"\"",
              "steps": [
                {
                  "entityId": "Unknown",
                  "command": "test cable-diagnostics tdr interface ",
                  "description": "perform cable diagnostic check",
                  "stepType": "command-Runner"
                },
                {
                  "entityId": "Unknown",
                  "command": "show cable-diagnostics tdr interface ",
                  "description": "show cable diagnostic check",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Use the show controller Ethernet-controller \"\" command to verify if there is any increase in packet drops/errors on switch \"\" and port \"\" to which AP \"3800.63D4\" is connected.",
              "steps": [
                {
                  "entityId": "Unknown",
                  "command": "show interfaces  summary",
                  "description": "Verify if there are any packet drops/errors",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Use the show power inline \"\" detail command to check POE status/errors to see if power was supplied to the AP \"3800.63D4\".",
              "steps": [
                {
                  "entityId": "Unknown",
                  "command": "show power inline  detail",
                  "description": "Check POE status/errors",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Check if there has been any problems in the network path between the AP and the WLC.",
              "steps": []
            }
          ],
          "issueId": "AWfQFFNEowzDvHZ5iroF"
        }
      ]
    }
  },
  "assignedTo": "",
  "type": "Network",
  "id": "AWfQFFNEowzDvHZ5iroF",
  "description": "This AP \"3800.63D4\" has disconnected from WLC \"WLC9800.adamlab.cisco.com\" and reconnected to WLC \"WLC9800.adamlab.cisco.com\"."
}
