import logging
from ckanext.harvest.harvesters.ckanharvester import CKANHarvester

log = logging.getLogger(__name__)

class DVRPCHarvester(CKANHarvester):

    def info(self):
        return {
            'name': 'dvrpc_internal',
            'title': 'DVRPC Internal',
            'description': 'Harvests public datasets from inernal DVRPC Data Catalog',
            'form_config_interface': 'Text'
        }

    def modify_package_dict(self, package_dict, harvest_object):

        # delete the "Network Location" resource (in GIS datasets)
        resource_to_delete = ""
        for i, resource in enumerate(package_dict["resources"]):
            if resource["name"] == "Network Location":
                resource_to_delete = i

        del package_dict["resources"][resource_to_delete]

        return package_dict
