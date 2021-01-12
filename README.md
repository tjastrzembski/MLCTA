# MLCGB (Multi Language Call Graph Builder)
This Tool generates a calling graph for Zope application servers. It scans all Zope objects, filters all possible function calls of them and connect them to each other by using those filtered function calls. It uses ANTLR to provide multiple parsers to filter different meta-/interpretation types.

## Requirements

- Python
- ANTLR

Zope application server uses 
- ZODBsync
- PostgreSQL
