import click

@click.group()
@click.version_option()

def cli():
    """Deconst, docs deconstructed.
    
    This is the command-line script for using the content API for
    developer.rackspace.com.
    """

@cli.group()
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
    deconst()