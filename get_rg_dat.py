import json
import os
import argparse

from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential


def main(rg_ids: str):
    credential = DefaultAzureCredential()
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    client = ResourceManagementClient(credential, subscription_id)
    rg_ids = json.loads(rg_ids)
    for id in rg_ids:
        name = id.split('/')[-1]
        rg = client.resource_groups.get(resource_group_name=name)
        print(rg)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Python script with a given path.')
    parser.add_argument('arg1', type=str, help='The path to the Python script to run.')
    args = parser.parse_args()
    main(args.arg1)