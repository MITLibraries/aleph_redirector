# 2. Permalinks should have transitions to new systems

Date: 2021-05-27

## Status

Accepted

## Context

We are migrating from Aleph to Alma / Primo. Aleph had a system for creating
persistent links to records that we advertised as permalinks.

Example:

```text
Permalink for this record: http://library.mit.edu/item/001264079
```

Those links have been included in websites and user bookmarks for a decade.

We can choose to redirect all traffic to library.mit.edu to a generic page that
explains that we have moved systems, or we can try to use our knowledge of both
Aleph and Primo to both tell the user the old system has been retired while
providing them with an equivalent new _persistent_ link in Primo -- a link
which we should use care in refering to as _persistent_ and not _permanent_ if
unless we intend to support it across system transitions.

## Decision

As we advertised permalinks, we should make an effort to not only tell people a
system was shut down they were using, but provide them with a likely link to the
same record in the new system.

We will not maintain this linkage forever, but will use care in our status
codes to inform search engines to remove the old link while informing users
that the automatic redirecting will only remain for a specified period of time.

## Consequences

Our users and websites that are using Aleph permalinks will continue to have
access to the same information in Alma.

We will need to create a smarter redirect rather than relying on 404ing
everything to a single page that explains the system migration.

We need to convey to users that this is a temporary solution and will be
retired on a specific date so they should update bookmarks and webpages.
