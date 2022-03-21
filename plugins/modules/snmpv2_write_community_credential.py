#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: snmpv2_write_community_credential
short_description: Resource module for Snmpv2 Write Community Credential
description:
- Manage operations create and update of the resource Snmpv2 Write Community Credential.
- Adds global SNMP write community.
- Updates global SNMP write community.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Comments to identify the credential.
    type: str
  credentialType:
    description: Credential type to identify the application that uses the credential.
    type: str
  description:
    description: Name/Description of the credential.
    type: str
  instanceUuid:
    description: Snmpv2 Write Community Credential's instanceUuid.
    type: str
  writeCommunity:
    description: SNMP write community. NO!$DATA!$ for no value change.
    type: str
requirements:
- dnacentersdk >= 2.4.6
- python >= 3.5
notes:
  - SDK Method used are
    discovery.Discovery.create_snmp_write_community,
    discovery.Discovery.update_snmp_write_community,

  - Paths used are
    post /dna/intent/api/v1/global-credential/snmpv2-write-community,
    put /dna/intent/api/v1/global-credential/snmpv2-write-community,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.snmpv2_write_community_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    writeCommunity: string

- name: Update all
  cisco.dnac.snmpv2_write_community_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    instanceUuid: string
    writeCommunity: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""