#!/usr/bin/env python

import argparse
import logging

import azure.identity.aio
import msgraph
import msgraph.graph_service_client

DESCRIPTION = """
List Entra ID groups.
"""

logger = logging.getLogger(__name__)

SCOPES = list()


def get_args() -> argparse.Namespace:
    """
    Command-line arguments
    https://docs.python.org/3/howto/argparse.html
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(
        format="%(name)s:%(asctime)s:%(levelname)s:%(message)s",
        level=logging.INFO if args.verbose else logging.WARNING
    )

    # https://github.com/microsoftgraph/msgraph-sdk-python

    logger.debug("smgraph version %s", msgraph.__version__)

    # Use the service connection to authenticate
    # https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.environmentcredential
    credential = azure.identity.aio.DefaultAzureCredential()
    # credential = azure.identity.aio.EnvironmentCredential()

    # Initialise Microsoft Graph API client
    client = msgraph.graph_service_client.GraphServiceClient(
        credentials=credential, scopes=SCOPES)

    # Get all the Entra ID groups
    # https://learn.microsoft.com/en-us/graph/api/group-list
    groups = client.groups.get_by_ids

    # Display information about each group
    print(groups)


if __name__ == '__main__':
    main()
