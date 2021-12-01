#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery_job_info
short_description: Information module for Discovery Job
description:
- Get all Discovery Job.
- Get Discovery Job by id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter.
    type: int
  limit:
    description:
    - Limit query parameter.
    type: int
  ipAddress:
    description:
    - IpAddress query parameter.
    type: str
  name:
    description:
    - Name query parameter.
    type: str
  id:
    description:
    - Id path parameter. Discovery ID.
    type: str
requirements:
- dnacentersdk >= 2.3.3
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Discovery Job reference
  description: Complete reference of the Discovery Job object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Discovery Job
  cisco.dnac.discovery_job_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    offset: 0
    limit: 0
    ipAddress: string
    name: string
  register: result

- name: Get Discovery Job by id
  cisco.dnac.discovery_job_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    offset: 0
    limit: 0
    ipAddress: string
    id: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "attributeInfo": {},
          "cliStatus": "string",
          "discoveryStatus": "string",
          "endTime": "string",
          "httpStatus": "string",
          "id": "string",
          "inventoryCollectionStatus": "string",
          "inventoryReachabilityStatus": "string",
          "ipAddress": "string",
          "jobStatus": "string",
          "name": "string",
          "netconfStatus": "string",
          "pingStatus": "string",
          "snmpStatus": "string",
          "startTime": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""
