# python-deconst

A python-deconst client offers access to the Deconst Content API to make content and
search commands simpler.

# Development

Currently the `search.py` file contains the work so far. The `cli.py` file will contain
the [Python click library](http://click.pocoo.org/5/) code to make the CLI run.

# Use cases

I want to list of all content IDs on the site.

I want to list of content URLs with a certain tag.

I want to run a report of recently updated files.

I want to create navigation ideas by listing collections of categories or keywords or tags.

I want to list content based on the info in the metadata envelope.

I want to tweet a link to content based on a particular tag or updated date.


API: https://github.com/deconst/content-service#api

GET /content/:id

Access previously stored content by its URL-encoded content ID.

Response: Successful

{
  "assets": {},
  "envelope": {}
}
"envelope" will be the exact JSON document provided to PUT /content. "assets" will contain a set of site-wide layout asset variables.

To get a list, iterate through each content ID and retrieve the first heading?

GET /search?q=:term&pageNumber=:num&perPage=:size&categories=deconst.horse

Perform a full-text search against all indexed documents.

q is a required parameter. pageNumber defaults to 1 if unspecified, and perPage defaults to 10. categories may be specified multiple times (or as categories[]), and if present at least once, will constrain search results to only those envelopes that contain at least one matching category.

Response: Successful

{
  "total": 100,
  "results": [
    {
      "contentID": "https://github.com/deconst/deconst-docs/one",
      "title": "First result title",
      "excerpt": "body excerpt with matching text <em>highlighted</em>"
    },
    {
      "contentID": "https://github.com/deconst/deconst-docs/two",
      "title": "Second result title",
      "excerpt": "first bit of the body if no body content matched"
    }
  ]
}

Metadata envelope schema: https://deconst.horse/developing/envelope/
author, publish_date
tags, categories, keywords
