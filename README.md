`gravel-storage` keeps portions of data in units called *boxes*.
Box can by of many types - it can be directory in filesystem, PostgreSQL database
or anything else plugin supports.

Box resides on any number of nodes - at most one node is active, rest are backups.
Only data stored in active node can be modified.

For exampe, in case of database active node would store data in database, backup nodes would only keep
SQL dump.
