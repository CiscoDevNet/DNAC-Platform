border_dhcp_eg = {
  "category": "Warn",
  "status": "NEW",
  "domain": "Connected",
  "description": "'Co-located Fabric Border and Control Plane' \"cp-br.adamlab.cisco.com\" cannot reach the DHCP server 10.10.10.151 in the Virtual Network VRF 'Things'.",
  "title": "Fabric Devices Connectivity",
  "instanceId": "E-NETWORK-EVENT-AWg3IyZJxFejNYA7pNg0-1547113276740",
  "timestamp": 1547113276740,
  "actualServiceId": "10.10.3.41",
  "tenantId": "5b2859ba4a917a0088dc9c86",
  "priority": "P2",
  "assignedTo": "",
  "version": "1.2.0",
  "source": "DNAC",
  "enrichmentInfo": {
    "connectedDevice": [
      {
        "deviceDetails": {
          "macAddress": "00:1e:e5:0a:d7:00",
          "upTime": "204 days, 23:23:07.29",
          "bootDateTime": "2017-12-16 21:48:14",
          "neighborTopology": [
            {
              "nodes": [
                {
                  "nodeType": "NetworkDevice",
                  "description": "Router",
                  "family": "Routers",
                  "platformId": "CSR1000V",
                  "ip": "10.10.3.41",
                  "id": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "name": "cp-br.adamlab.cisco.com",
                  "level": 0,
                  "softwareVersion": "16.6.2",
                  "deviceType": "Cisco Cloud Services Router 1000V",
                  "healthScore": 10,
                  "role": "BORDER ROUTER"
                },
                {
                  "nodeType": "NetworkDevice",
                  "description": "Router",
                  "family": "Routers",
                  "platformId": "CSR1000V",
                  "ip": "10.10.2.41",
                  "id": "e729576a-ed3a-4a25-87f5-6821262830dd",
                  "name": "fusionRouter.adamlab.cisco.com",
                  "level": 1,
                  "softwareVersion": "16.7.1",
                  "deviceType": "Cisco Cloud Services Router 1000V",
                  "healthScore": 10,
                  "role": "BORDER ROUTER"
                }
              ],
              "links": [
                {
                  "source": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "linkStatus": "UP",
                  "target": "e729576a-ed3a-4a25-87f5-6821262830dd",
                  "label": []
                }
              ]
            }
          ],
          "lastUpdateTime": 1547111954007,
          "snmpContact": "",
          "lineCardCount": "2",
          "series": "Cisco Cloud Services Router 1000V Series",
          "apManagerInterfaceIp": "",
          "lastUpdated": "2019-01-10 09:19:14",
          "cisco360view": "https://10.66.104.84/dna/assurance/home#networkDevice/5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
          "interfaceCount": "19",
          "managementIpAddress": "10.10.3.41",
          "serialNumber": "9EY8G0QR564",
          "reachabilityFailureReason": "",
          "associatedWlcIp": "",
          "instanceUuid": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
          "family": "Routers",
          "reachabilityStatus": "Reachable",
          "hostname": "cp-br.adamlab.cisco.com",
          "memorySize": "2458193040",
          "roleSource": "AUTO",
          "id": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
          "inventoryStatusDetail": "<status><general code=\"SYNC\"/></status>",
          "platformId": "CSR1000V",
          "softwareVersion": "16.6.2",
          "role": "BORDER ROUTER",
          "lineCardId": "a63db3b8-1d8d-45f3-ae8b-ba5fa53b2090, f111eecf-4fe6-4825-8d62-ecf5a8e183eb",
          "snmpLocation": "",
          "collectionInterval": "Global Default",
          "type": "Cisco Cloud Services Router 1000V",
          "tagCount": "0",
          "collectionStatus": "In Progress"
        }
      }
    ],
    "issueDetails": {
      "issue": [
        {
          "issueId": "AWg3IyZJxFejNYA7pNg0",
          "issueCategory": "Connected",
          "issuePriority": "",
          "issueTimestamp": 1547113276740,
          "issueSource": "Cisco DNA",
          "issueDescription": "'Co-located Fabric Border and Control Plane' \"cp-br.adamlab.cisco.com\" cannot reach the DHCP server 10.10.10.151 in the Virtual Network VRF 'Things'.",
          "impactedHosts": [],
          "issueSeverity": "HIGH",
          "issueSummary": "'Co-located Fabric Border and Control Plane' \"10.10.3.41\" Lost Connectivity to the DHCP Server 10.10.10.151 in the Virtual Network Things",
          "issueEntityValue": "10.10.3.41",
          "issueEntity": "network_device",
          "issueName": "fabric_reachability_session",
          "suggestedActions": [
            {
              "message": "Verify whether the DHCP server is up.",
              "steps": []
            },
            {
              "message": "Verify if configuration is compliant on network device",
              "steps": [
                {
                  "entityId": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "command": "show run | sec lisp",
                  "description": "Verify Fabric configuration for the Virtual Network VRF Things",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Check the route from Fabric Border to DHCP server",
              "steps": [
                {
                  "entityId": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "command": "show ip route vrf Things 10.10.10.151",
                  "description": "Check ip route to 10.10.10.151 in vrf Things",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Verify IGP adjacencies from this node to the upstream switches.",
              "steps": [
                {
                  "entityId": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "command": "show isis neighbors",
                  "description": "Check ISIS adjacencies",
                  "stepType": "command-Runner"
                },
                {
                  "entityId": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "command": "show ospf neighbor",
                  "description": "Check OSPF adjacencies",
                  "stepType": "command-Runner"
                },
                {
                  "entityId": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "command": "sh eigrp address-family ipv4 neighbors",
                  "description": "Check EIGRP adjacencies",
                  "stepType": "command-Runner"
                },
                {
                  "entityId": "5f0158bb-10e6-40c3-b9c9-7c1e14e77f2d",
                  "command": "sh ip bgp neighbors",
                  "description": "Check BGP adjacencies",
                  "stepType": "command-Runner"
                }
              ]
            },
            {
              "message": "Contact Cisco TAC World Wide \u2013 https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html",
              "steps": []
            }
          ]
        }
      ]
    }
  },
  "type": "Network",
  "id": "AWg3IyZJxFejNYA7pNg0",
  "severity": "P2"
}