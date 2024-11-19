#!/usr/bin/env python

import argparse
import logging
import os

import msgraph
import msgraph.graph_service_client

import azure.identity.aio

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
    # https://learn.microsoft.com/en-us/graph/api/group-list

    logger.debug("smgraph version %s", msgraph.__version__)

    credential = azure.identity.aio.ClientSecretCredential(
        tenant_id=os.environ['AZURE_CLIENT_ID'],
        cliing_token=os.environ['AZURE_CLIENT_SECRET'],
        client_secret=os.environ['AZURE_CLIENT_SECRET'],
    )

    client = msgraph.graph_service_client.GraphServiceClient(
        credentials=credential, scopes=SCOPES)

    groups = client.groups.get_by_ids

    print(groups)


if __name__ == '__main__':
    main()
