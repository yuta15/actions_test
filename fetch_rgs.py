import os
import sys
import json

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


def fetch_rgs():
    SUBSCRIPTION_ID = os.environ.get("AZURE_SUBSCRIPTION_ID")
    credentail = DefaultAzureCredential()
    client = ResourceManagementClient(credential=credentail, subscription_id=SUBSCRIPTION_ID)
    resource_groups = client.resource_groups.list()
    rgs = []
    for rg in resource_groups:
        rgs.append(rg.id)
    json.dump(rgs, sys.stdout, indent=4)

fetch_rgs()