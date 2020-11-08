# [Caleb Curry SQL-Server (RDBMS)](https://www.youtube.com/watch?v=WttoAlS__8k&list=PL_c9BZzLwBRKC2PJwLFxc2y6cyXYYQzj3)

## Terms
+ data  facts, information
+ database collection of data
+ DBMS - Data Base Management System
+ RDBMS (Relational Data Base System) - presentation the data in a beatifull way
+ intermediary table or junction table - essentially to record the associations between a relation many to many
+ data integrity - data is correct, up to data as possible, not conflicting, no duplicates and it is describing what we think it´s describing.
+ surrogate key - computer generated number for the sake of the data base only.
+ natural key - has a real world meaning (must be unique, not null and never changes)
+ composite key - a primary key that consists of a multiple columns
+ index custered

## ON DELETE
+ no action - parent is locked into existence until that child is no longer there.
+ cascade - delete the parent it´s automatically going to pass on all changes
+ set null - delete the parent and child is going to be replaced with null
+ set default - delete the parent and child is going to be replaced with a default value.

## Indexes
+ clustered - phone book how the table is laid out. (primary key as default). IT can be only one index.a
+ non-clustered - last page from a book.
