#!/bin/bash

# Initialisation database
sqlite3 contacts.db < contacts_dump.sql

# Maintenir le conteneur en vie
tail -f /dev/null
