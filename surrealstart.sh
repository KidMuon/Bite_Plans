#!/bin/bash

SURREAL_PORT=$(jq -r ".port" config/surrealdb.json)
SURREAL_USERNAME=$(jq -r ".username" config/surrealdb.json)
SURREAL_PASSWORD=$(jq -r ".password" config/surrealdb.json)

surreal start \
    -A --auth --username $SURREAL_USERNAME \
    --password $SURREAL_PASSWORD \
    --bind 0.0.0.0:$SURREAL_PORT

