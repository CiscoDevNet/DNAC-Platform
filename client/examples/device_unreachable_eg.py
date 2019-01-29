device_unreachable_eg={
  "category": "Warn",
  "status": "NEW",
  "domain": "Availability",
  "severity": "P1",
  "title": "Device unreachable",
  "instanceId": "E-NETWORK-EVENT-AWfPwITHowzDvHZ5irk1-1545378759808",
  "timestamp": 1545378759808,
  "actualServiceId": "192.168.200.80",
  "tenantId": "5c1b2facb982eb004c36c5bd",
  "priority": "P1",
  "source": "DNAC",
  "version": "1.2.0",
  "enrichmentInfo": {
    "connectedDevice": [
      {
        "deviceDetails": {
          "macAddress": "24:7e:12:50:db:00",
          "upTime": "55 days, 4:16:00.40",
          "bootDateTime": "2018-10-27 03:20:37",
          "family": "Switches and Hubs",
          "snmpContact": "",
          "lineCardCount": "1",
          "series": "Cisco Catalyst 9300 Series Switches",
          "errorCode": "DEV-UNREACHED",
          "interfaceCount": "65",
          "id": "44e52201-6133-4d6f-b3a6-e0ce24c19d26",
          "inventoryStatusDetail": "<status><general code=\"DEV_UNREACHED\"/></status>",
          "associatedWlcIp": "",
          "instanceUuid": "44e52201-6133-4d6f-b3a6-e0ce24c19d26",
          "lastUpdateTime": 1545378759827,
          "reachabilityStatus": "Unreachable",
          "hostname": "encs-9k.adamlab.cisco.com",
          "memorySize": "889822112",
          "roleSource": "AUTO",
          "managementIpAddress": "192.168.200.80",
          "platformId": "C9300-48P",
          "collectionStatus": "Partial Collection Failure",
          "role": "ACCESS",
          "lineCardId": "d25ce2f9-1675-4638-86c2-bcf5aadc40b9",
          "type": "Cisco Catalyst 9300 Switch",
          "apManagerInterfaceIp": "",
          "neighborTopology": [
            {
              "nodes": [
                {
                  "nodeType": "NetworkDevice",
                  "name": "encs-9k.adamlab.cisco.com",
                  "family": "Switches and Hubs",
                  "level": 1,
                  "platformId": "C9300-48P",
                  "ip": "192.168.200.80",
                  "softwareVersion": "16.6.2",
                  "deviceType": "Cisco Catalyst 9300 Switch",
                  "healthScore": 10,
                  "role": "ACCESS",
                  "id": "44e52201-6133-4d6f-b3a6-e0ce24c19d26"
                }
              ],
              "links": []
            }
          ],
          "errorDescription": "SNMP timeouts are occurring with this device. Either the SNMP credentials are not correctly provided to controller or the device is responding slow and snmp timeout is low. If its a timeout issue, controller will attempt to progressively adjust the timeout in subsequent collection cycles to get device to managed state. User can also run discovery again only for this device using the discovery feature after adjusting the timeout and snmp credentials as required. Or user can update the timeout and snmp credentials as required using update credentials.",
          "lastUpdated": "2018-12-21 07:52:39",
          "cisco360view": "https://10.10.10.181/dna/assurance/home#networkDevice/44e52201-6133-4d6f-b3a6-e0ce24c19d26",
          "collectionInterval": "Global Default",
          "serialNumber": "FCW2148G04P",
          "reachabilityFailureReason": "SNMP Connectivity Failed",
          "softwareVersion": "16.6.2",
          "snmpLocation": "",
          "tagCount": "0"
        }
      }
    ],
    "issueDetails": {
      "issue": [
        {
          "impactedHosts": [],
          "issueDescription": "This network device encs-9k.adamlab.cisco.com is unreachable from controller. The device role is ACCESS.",
          "issueCategory": "Availability",
          "issueSeverity": "HIGH",
          "issueSummary": "Network Device 192.168.200.80 Is Unreachable From Controller",
          "issuePriority": "",
          "issueTimestamp": 1545378759808,
          "issueEntityValue": "192.168.200.80",
          "issueSource": "Cisco DNA",
          "issueEntity": "network_device",
          "issueName": "snmp_device_down",
          "suggestedActions": [
            {
              "message": "From the controller, verify whether the last hop is reachable.",
              "steps": []
            },
            {
              "message": "Verify that the physical port(s) on the network device associated with the network device discovery(IP) is UP.",
              "steps": []
            },
            {
              "message": "Verify access to the device.",
              "steps": []
            }
          ],
          "issueId": "AWfPwITHowzDvHZ5irk1"
        }
      ]
    }
  },
  "assignedTo": "",
  "type": "Network",
  "id": "AWfPwITHowzDvHZ5irk1",
  "description": "This network device encs-9k.adamlab.cisco.com is unreachable from controller. The device role is ACCESS."
}