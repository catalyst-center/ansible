#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_edge_device
short_description: Resource module for Sda Fabric Edge Device
description:
- Manage operations create and delete of the resource Sda Fabric Edge Device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description: DeviceIPAddress query parameter. Device IP Address.
    type: str
  payload:
    description: Sda Fabric Edge Device's payload.
    suboptions:
      deviceManagementIpAddress:
        description: Device Management Ip Address.
        type: str
      siteNameHierarchy:
        description: Site Name Hierarchy.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.3.3
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sda Fabric Edge Device reference
  description: Complete reference of the Sda Fabric Edge Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_fabric_edge_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - deviceManagementIpAddress: string
      siteNameHierarchy: string

- name: Delete all
  cisco.dnac.sda_fabric_edge_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceIPAddress: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "executionStatusUrl": "string"
    }
"""
