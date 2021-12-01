#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: projects_details_info
short_description: Information module for Projects Details
description:
- Get all Projects Details.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id query parameter. Id of project to be searched.
    type: str
  name:
    description:
    - Name query parameter. Name of project to be searched.
    type: str
  offset:
    description:
    - Offset query parameter. Index of first result.
    type: int
  limit:
    description:
    - Limit query parameter. Limits number of results.
    type: int
  sortOrder:
    description:
    - SortOrder query parameter. Sort Order Ascending (asc) or Descending (dsc).
    type: str
requirements:
- dnacentersdk >= 2.3.1
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Projects Details reference
  description: Complete reference of the Projects Details object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Projects Details
  cisco.dnac.projects_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    id: string
    name: string
    offset: 0
    limit: 0
    sortOrder: string
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
          "createTime": 0,
          "description": "string",
          "id": "string",
          "isDeletable": true,
          "lastUpdateTime": 0,
          "name": "string",
          "tags": [
            {
              "id": "string",
              "name": "string"
            }
          ],
          "templates": [
            {
              "tags": [
                {
                  "id": "string",
                  "name": "string"
                }
              ],
              "author": "string",
              "composite": true,
              "containingTemplates": [
                {
                  "tags": [
                    {
                      "id": "string",
                      "name": "string"
                    }
                  ],
                  "composite": true,
                  "description": "string",
                  "deviceTypes": [
                    {
                      "productFamily": "string",
                      "productSeries": "string",
                      "productType": "string"
                    }
                  ],
                  "id": "string",
                  "language": "string",
                  "name": "string",
                  "projectName": "string",
                  "rollbackTemplateParams": [
                    {
                      "binding": "string",
                      "customOrder": 0,
                      "dataType": "string",
                      "defaultValue": "string",
                      "description": "string",
                      "displayName": "string",
                      "group": "string",
                      "id": "string",
                      "instructionText": "string",
                      "key": "string",
                      "notParam": true,
                      "order": 0,
                      "paramArray": true,
                      "parameterName": "string",
                      "provider": "string",
                      "range": [
                        {
                          "id": "string",
                          "maxValue": 0,
                          "minValue": 0
                        }
                      ],
                      "required": true,
                      "selection": {
                        "defaultSelectedValues": [
                          "string"
                        ],
                        "id": "string",
                        "selectionType": "string",
                        "selectionValues": {}
                      }
                    }
                  ],
                  "templateContent": "string",
                  "templateParams": [
                    {
                      "binding": "string",
                      "customOrder": 0,
                      "dataType": "string",
                      "defaultValue": "string",
                      "description": "string",
                      "displayName": "string",
                      "group": "string",
                      "id": "string",
                      "instructionText": "string",
                      "key": "string",
                      "notParam": true,
                      "order": 0,
                      "paramArray": true,
                      "parameterName": "string",
                      "provider": "string",
                      "range": [
                        {
                          "id": "string",
                          "maxValue": 0,
                          "minValue": 0
                        }
                      ],
                      "required": true,
                      "selection": {
                        "defaultSelectedValues": [
                          "string"
                        ],
                        "id": "string",
                        "selectionType": "string",
                        "selectionValues": {}
                      }
                    }
                  ],
                  "version": "string"
                }
              ],
              "createTime": 0,
              "customParamsOrder": true,
              "description": "string",
              "deviceTypes": [
                {
                  "productFamily": "string",
                  "productSeries": "string",
                  "productType": "string"
                }
              ],
              "documentDatabase": true,
              "failurePolicy": "string",
              "id": "string",
              "language": "string",
              "lastUpdateTime": 0,
              "latestVersionTime": 0,
              "name": "string",
              "parentTemplateId": "string",
              "projectAssociated": true,
              "projectId": "string",
              "projectName": "string",
              "rollbackTemplateContent": "string",
              "rollbackTemplateParams": [
                {
                  "binding": "string",
                  "customOrder": 0,
                  "dataType": "string",
                  "defaultValue": "string",
                  "description": "string",
                  "displayName": "string",
                  "group": "string",
                  "id": "string",
                  "instructionText": "string",
                  "key": "string",
                  "notParam": true,
                  "order": 0,
                  "paramArray": true,
                  "parameterName": "string",
                  "provider": "string",
                  "range": [
                    {
                      "id": "string",
                      "maxValue": 0,
                      "minValue": 0
                    }
                  ],
                  "required": true,
                  "selection": {
                    "defaultSelectedValues": [
                      "string"
                    ],
                    "id": "string",
                    "selectionType": "string",
                    "selectionValues": {}
                  }
                }
              ],
              "softwareType": "string",
              "softwareVariant": "string",
              "softwareVersion": "string",
              "templateContent": "string",
              "templateParams": [
                {
                  "binding": "string",
                  "customOrder": 0,
                  "dataType": "string",
                  "defaultValue": "string",
                  "description": "string",
                  "displayName": "string",
                  "group": "string",
                  "id": "string",
                  "instructionText": "string",
                  "key": "string",
                  "notParam": true,
                  "order": 0,
                  "paramArray": true,
                  "parameterName": "string",
                  "provider": "string",
                  "range": [
                    {
                      "id": "string",
                      "maxValue": 0,
                      "minValue": 0
                    }
                  ],
                  "required": true,
                  "selection": {
                    "defaultSelectedValues": [
                      "string"
                    ],
                    "id": "string",
                    "selectionType": "string",
                    "selectionValues": {}
                  }
                }
              ],
              "validationErrors": {
                "rollbackTemplateErrors": [
                  {}
                ],
                "templateErrors": [
                  {}
                ],
                "templateId": "string",
                "templateVersion": "string"
              },
              "version": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
