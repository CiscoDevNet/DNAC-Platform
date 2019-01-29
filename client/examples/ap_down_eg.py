ap_down_eg={
  "category": "Warn",
  "status": "NEW",
  "domain": "Availability",
  "severity": "P2",
  "title": "AP Down",
  "instanceId": "E-NETWORK-EVENT-AWfQE8aJowzDvHZ5iroE-1545384195506",
  "timestamp": 1545384195506,
  "actualServiceId": "CC:16:7E:92:2B:40",
  "tenantId": "5c1b2facb982eb004c36c5bd",
  "priority": "P2",
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
          "issueDescription": "This AP \"3800.63D4\" is no longer connected to a WLC. This AP was previously connected to the switch \"\" and port \"\".",
          "issueCategory": "Availability",
          "issueSeverity": "MEDIUM",
          "issueSummary": "AP \"3800.63D4\" went down.",
          "issuePriority": "",
          "issueTimestamp": 1545384195506,
          "issueEntityValue": "CC:16:7E:92:2B:40",
          "issueSource": "Cisco DNA",
          "issueEntity": "network_device",
          "issueName": "ap_down",
          "suggestedActions": [
            {
              "message": "Use the \"show cdp neighbor\" command on the switch to verify if the AP is still up, connected to the switch and the AP hostname has not changed. If the AP hostname has reset to the default value (in the form AP{mac-address}), this indicates that the AP has lost its configuration.",
              "steps": []
            },
            {
              "message": "Use the \"show cdp neighbor <portId> detail\" command on the switch to see if the AP has a valid IP address. If it doesn't have an IP address, check the DHCP server.",
              "steps": []
            },
            {
              "message": "Test the Ethernet cable by performing a cable diagnostic check on the switch \"\" and port \"\". Use the following commands: test cable-diagnostics tdr interface \"\" and show cable-diagnostics tdr interface \"\".",
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
              "message": "Use the show power inline \"\" command to verify whether PoE is enabled on the switchport \"\".",
              "steps": [
                {
                  "entityId": "Unknown",
                  "command": "show power inline ",
                  "description": "show if PoE is enabled",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Use the Path Trace tool to verify whether the AP can communicate with the WLC via UDP ports: 5246 & 5247 (CAPWAP).",
              "steps": []
            },
            {
              "message": "Reboot the AP so it can rejoin the WLC.",
              "steps": []
            }
          ],
          "issueId": "AWfQE8aJowzDvHZ5iroE"
        }
      ]
    }
  },
  "assignedTo": "",
  "type": "Network",
  "id": "AWfQE8aJowzDvHZ5iroE",
  "description": "This AP \"3800.63D4\" is no longer connected to a WLC. This AP was previously connected to the switch \"\" and port \"\"."
}