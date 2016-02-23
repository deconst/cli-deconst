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
import json

def get_doc_repos():
    """
    List all repos in the rackerlabs org that contain docs-
    
    GET /orgs/:org/repos
    """
    # Get list of repos in the rackerlabs org GET /orgs/:org/repos
    r = requests.get('https://api.github.com/orgs/rackerlabs/repos')

    if (r.ok):
       fullRepoList = json.loads(r.content)
       print json.dumps(fullRepoList, sort_keys=True, indent=4)
       
       allReposList = fullRepoList['name']
       print (allReposList)
       docReposList = 
       
def get_content_ids():
    """List all content IDs on the site.
    
    GET /content/:id
    Access previously stored content by its URL-encoded content ID.

    Takes the JSON response and gets the first heading from the HTML.
    {
      "assets": {},
      "envelope": {}
    }
    """
    content_id = quote('https://github.com/rackerlabs/docs-container-service', safe='')
    print (content_id)    
    
    r = requests.get('https://developer.rackspace.com:9000/content')
    print (r.status_code)
    categories = []
    if (r.ok):
       content = json.loads(r.content)
       print (content['envelope'])
    
def list_content_ids(self):
    pass
    
    
def list_by_search_term():
    """List content URLs with a certain tag.
    
    GET /search?q=:term&pageNumber=:num&perPage=:size&categories=deconst.horse

    Perform a full-text search against all indexed documents.

    q is a required parameter. pageNumber defaults to 1 if unspecified, and perPage
    defaults to 10. categories may be specified multiple times (or as categories[]),
    and if present at least once, will constrain search results to only those envelopes
    that contain at least one matching category.

    """
    pass

def main():

    get_doc_repos()
    get_content_ids()
