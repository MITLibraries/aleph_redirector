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
