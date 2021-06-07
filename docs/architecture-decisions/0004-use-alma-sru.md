# 4. Use Alma SRU

Date: 2021-06-03

## Status

Accepted

## Context

We need a way to translate a supplied Aleph ID into an Alma ID suitable for use
in linking to a full record view in Primo UI.

Options include:

- [Alma Bibliographic Records and Inventory API](https://developers.exlibrisgroup.com/alma/apis/bibs/)
- [Alma SRU](https://developers.exlibrisgroup.com/alma/integrations/sru/)
- [TIMDEX](https://timdex.mit.edu)

Alma SRU is openly available with no API key or IP restrictions.

TIMDEX does not yet have this data loaded.

## Decision

Alma SRU works well for this use case, is openly available, and is ready for
this use case immediately.

We will use Alma SRU.

## Consequences

As we learn more about Alma SRU and Alma Bib API, we may find that this use case
fits better with the Alma Bib API.

Additionally, when TIMDEX is updated to have the necessary Alma records, we may
want to centralize on our internal discovery API.

Changing to use either of those other options is relatively minimal effort and
we should do so if they become preferred for this use case in the future.
