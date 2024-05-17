#!/bin/bash
GITHUB_URL="https://github.com/BlinerZ/Projet_Info0803.git"

# Download the SQL dump file
wget $GITHUB_URL -O contacts_dump.sql

# Initialize the SQLite database
sqlite3 contacts.db < contacts_dump.sql

# Keep the container running
tail -f /dev/null