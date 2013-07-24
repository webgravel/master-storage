gravel-master-storage
-----------

`gravel-storage` keeps portions of data in units called *boxes*.
Box can be of many types - it can be directory in filesystem, PostgreSQL database
or anything else plugin supports.

Box resides on any number of nodes - at most one node is active, rest are backups.
Only data stored in active node can be modified.

For example, in case of database active node would store data in live database, backup nodes would only keep SQL dump.

Limitations
-----------

Deleting and then creating resource with same identifier, but different type leads to undefined behaviour.
