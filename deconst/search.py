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

import requests
from requests.utils import quote
import json

def get_doc_repos():
    """
    List all repos in the rackerlabs org that contain docs-
    
    GET /orgs/:org/repos
    """
    # Get list of repos in the rackerlabs org GET /orgs/:org/repos
    pass

def get_content_by_id(content_id):
    """Get content based on ID.
    
    GET /content/:id
    Access previously stored content by its URL-encoded content ID.

    Takes the JSON response and gets the first heading from the HTML.
    {
      "assets": {},
      "envelope": {}
    }
    """
    # content_id = quote('https://github.com/rackerlabs/docs-container-service', safe='')
    # print (content_id)    
    
    r = requests.get('https://developer.rackspace.com:9000/content/' + content_id)
    # print (r.status_code)
    # print (r.headers)
    if (r.ok):
       content = json.loads(r.content)
    return r.json()
    
    
def list_content_ids():
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

    
def list_by_search_term(term):
    """List content URLs with a certain tag.
    
    GET /search?q=:term&pageNumber=:num&perPage=:size&categories=deconst.horse

    Perform a full-text search against all indexed documents.

    q is a required parameter. pageNumber defaults to 1 if unspecified, and perPage
    defaults to 10. categories may be specified multiple times (or as categories[]),
    and if present at least once, will constrain search results to only those envelopes
    that contain at least one matching category.

    """

    r = requests.get('https://developer.rackspace.com:9000/search?q=' + term)
    print (r.status_code)

    if (r.ok):
       return json.loads(r.content)

def main():

    for content_id in list_content_ids():
        envelope = get_content_by_id(content_id)
        print envelope['envelope']['title']    
        
    keywordSearch = list_by_search_term('container')
    print keywordSearch['total']
