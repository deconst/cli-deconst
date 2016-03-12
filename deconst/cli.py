# Copyright (c) 2016 Rackspace, Inc.
#
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
import json
import requests
from requests.utils import quote
from tabulate import tabulate


@click.group()
@click.version_option()
def cli():
    """Deconst, docs deconstructed.
    
    This is the command-line script for using the content API for
    developer.rackspace.com.
    """
    output = "fred"
    print(output)

def deconst():
    """Command for calling the Content API read-only operations."""

@deconst.command('list')
def deconst_list():
    """List pulled from the nexus-control repo and could change.
    
    Uses a hand-built list for now.
    """    
    
    allContentIds = [    
	'https://github.com/rackerlabs/docs-core-infra-user-guide',
	'https://github.com/rackerlabs/rs-heat-docs', 
	'https://github.com/rackspace/rack', 
	'https://github.com/rackerlabs/docs-cloud-images', 
	'https://github.com/rackerlabs/docs-cloud-load-balancers/v1', 
	'https://github.com/rackerlabs/docs-cloud-load-balancers/v2', 
	'https://github.com/rackerlabs/docs-cloud-block-storage',
	'https://github.com/rackerlabs/docs-cloud-dns/v1', 
	'https://github.com/rackerlabs/docs-cloud-dns/v2', 
	'https://github.com/rackerlabs/docs-cloud-cdn', 
	'https://github.com/rackerlabs/docs-cloud-databases/v1', 
	'https://github.com/rackerlabs/docs-cloud-backup/v1', 
	'https://github.com/rackerlabs/docs-cloud-backup/v2', 
	'https://github.com/rackerlabs/docs-cloud-orchestration', 
	'https://github.com/rackerlabs/heat-resource-ref', 
	'https://github.com/rackerlabs/docs-cloud-rackconnect', 
	'https://github.com/rackerlabs/docs-cloud-queues', 
	'https://github.com/rackerlabs/docs-cloud-networks', 
	'https://github.com/rackerlabs/docs-cloud-big-data/v2', 
	'https://github.com/rackerlabs/otter', 
	'https://github.com/rackerlabs/docs-cloud-servers', 
	'https://github.com/rackerlabs/docs-cloud-files', 
	'https://github.com/rackerlabs/docs-cloud-metrics', 
	'https://github.com/rackerlabs/docs-cloud-identity', 
	'https://github.com/rackerlabs/docs-cloud-monitoring', 
	'https://github.com/rackerlabs/docs-barbican', 
	'https://github.com/rackerlabs/docs-dedicated-networking', 
	'https://github.com/rackerlabs/docs-common', 
	'https://github.com/rackerlabs/docs-rpc/v11', 
	'https://github.com/rackerlabs/docs-rpc/v10', 
	'https://github.com/rackerlabs/docs-dedicated-vcloud', 
	'https://github.com/rackerlabs/docs-redhat-osp',
	'https://github.com/rackerlabs/docs-container-service',
	'https://github.com/rackerlabs/rackspace-how-to'
    ]

    return [quote(item, safe='') for item in allContentIds]

if __name__ == '__main__':
    cli()