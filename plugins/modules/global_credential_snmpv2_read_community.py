#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: global_credential_snmpv2_read_community
short_description: Manage GlobalCredentialSnmpv2ReadCommunity objects of Discovery
description:
- Adds global SNMP read community.
- Updates global SNMP read community.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            comments:
                description:
                - It is the global credential snmpv2 read community's comments.
                type: str
            credentialType:
                description:
                - It is the global credential snmpv2 read community's credentialType.
                type: str
            description:
                description:
                - It is the global credential snmpv2 read community's description.
                type: str
            id:
                description:
                - It is the global credential snmpv2 read community's id.
                type: str
            instanceTenantId:
                description:
                - It is the global credential snmpv2 read community's instanceTenantId.
                type: str
            instanceUuid:
                description:
                - It is the global credential snmpv2 read community's instanceUuid.
                type: str
            readCommunity:
                description:
                - It is the global credential snmpv2 read community's readCommunity.
                type: str
                required: True

    comments:
        description:
        - SNMPv2ReadCommunityDTO's comments.
        type: str
    credentialType:
        description:
        - SNMPv2ReadCommunityDTO's credentialType.
        - Available values are 'GLOBAL' and 'APP'.
        type: str
    description:
        description:
        - SNMPv2ReadCommunityDTO's description.
        type: str
    id:
        description:
        - SNMPv2ReadCommunityDTO's id.
        type: str
    instanceTenantId:
        description:
        - SNMPv2ReadCommunityDTO's instanceTenantId.
        type: str
    instanceUuid:
        description:
        - SNMPv2ReadCommunityDTO's instanceUuid.
        type: str
    readCommunity:
        description:
        - SNMPv2ReadCommunityDTO's readCommunity.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv2_read_community
# Reference by Internet resource
- name: GlobalCredentialSnmpv2ReadCommunity reference
  description: Complete reference of the GlobalCredentialSnmpv2ReadCommunity object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialSnmpv2ReadCommunity reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Adds global SNMP read community.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SNMPv2ReadCommunityDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential snmpv2 read community's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential snmpv2 read community's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: SNMPv2ReadCommunityDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Updates global SNMP read community.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SNMPv2ReadCommunityDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential snmpv2 read community's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential snmpv2 read community's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: SNMPv2ReadCommunityDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv2_read_community import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "create":
        dnac.disable_validation()
        dnac.exec("post")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()