# SQLite Music

## Questions

2.1. With respects to lecture.db, artist id is a foreign key because artist id is the primary key of another table (artist table), which uniquely identifies each row in artist table.

2.2. This is because 1 artist can have many albums (1 to M relationship), hence, artist table cannot have an album id column where only 1 album id can be stored per artist record.

2.3. First, its likely that email address will be changed in the future. If email address is used as primary key and also foreign keys in other tables, the foreign keys will also have to be changed. This is unecessary complexity.
Second, number type data are processed quicker than character type data. Lastly, referencing a record by unique integers are easier and less error-prone than strings of characters in sql queries.

2.4. SELECT "Total" FROM "Invoice" WHERE "InvoiceDate" BETWEEN '2010-01-01'AND '2011-01-01' OR "InvoiceDate" = '2010-01-01'

2.5.
SELECT Track.Name
FROM
    ((SELECT
    InvoiceLine.TrackId, Invoice.CustomerId
    FROM InvoiceLine LEFT JOIN Invoice
    ON InvoiceLine.InvoiceId = Invoice.InvoiceId
    WHERE Invoice.CustomerId = '50') a)
LEFT JOIN Track
On a.TrackId = Track.TrackId

2.6. Similar in spirit to existing Artist table, create a new Composer table consisting of ComposerId and Composer Name. Thereafter, Composer field in Track can simply record the foreign key of Composer Id.

## Debrief

a. Nil

b. 20 minutes
