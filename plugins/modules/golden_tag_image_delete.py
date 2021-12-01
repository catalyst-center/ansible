#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: golden_tag_image_delete
short_description: Resource module for Golden Tag Image Delete
description:
- Manage operation delete of the resource Golden Tag Image Delete.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceFamilyIdentifier:
    description: DeviceFamilyIdentifier path parameter. Device family identifier e.g.
      277696480-283933147, e.g. 277696480.
    type: str
  deviceRole:
    description: DeviceRole path parameter. Device Role. Permissible Values ALL, UNKNOWN,
      ACCESS, BORDER ROUTER, DISTRIBUTION and CORE.
    type: str
  imageId:
    description: ImageId path parameter. Image Id in uuid format.
    type: str
  siteId:
    description: SiteId path parameter. Site Id in uuid format. Set siteId as -1 for
      Global site.
    type: str
requirements:
- dnacentersdk >= 2.3.1
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Golden Tag Image Delete reference
  description: Complete reference of the Golden Tag Image Delete object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.golden_tag_image_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceFamilyIdentifier: string
    deviceRole: string
    imageId: string
    siteId: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
