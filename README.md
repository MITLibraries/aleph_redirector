# Aleph to Alma redirector

## Purpose

This application is intended to help with the transition from our Aleph ILS to
our Alma / Primo implementation.

Most URLs we want to redirect to a page that clarifies the system changes.

Specific patterns of URLs, namely the Aleph Permalink pattern, we want to
assist users to find the same record in Primo.

## Development

Clone the repo and install the dependencies using Pipenv:

```shell
git clone git@github.com:MITLibraries/aleph_redirector.git

cd aleph_redirector

pipenv shell

pipenv install --dev

flask run
```

## Running tests locally

Follow above development installation instructions.

`pytest`

## Generating (or regenerating) cassettes

To (re)generate cassettes (cached responses)

`pytest --record-mode=rewrite`

## Environment variables

  `ALMA_SRU`: SRU endpoint for Alma
  `PRIMO_URL`: base URL to use to construct link to Primo UI
  `SENTRY_DSN`: set to a valid Sentry DSN to enable exception monitoring
  `TARGET_URL`: default URL to redirect to if no other match happens
