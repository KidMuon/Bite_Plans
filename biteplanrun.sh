#!/bin/bash

SURREAL_DATABASENAME=$(jq -r '.name' config/surrealdb.json)
SURREAL_PORT=$(jq -r ".port" config/surrealdb.json)
SURREAL_USERNAME=$(jq -r ".username" config/surrealdb.json)
SURREAL_PASSWORD=$(jq -r ".password" config/surrealdb.json)
SURREAL_NAMESPACE=$(jq -r ".namespace" config/surrealdb.json)
SURREAL_FILENAME=$(jq -r ".filename" config/surrealdb.json)

surreal import --conn http://localhost:8000 \
    --user $SURREAL_USERNAME \
    --pass $SURREAL_PASSWORD\
    --ns $SURREAL_NAMESPACE --db $SURREAL_DATABASENAME \
    $SURREAL_FILENAME

python src/surreal_test.py

surreal export --conn http://localhost:8000 \
    --user $SURREAL_USERNAME --pass $SURREAL_PASSWORD \
    --namespace $SURREAL_NAMESPACE --database $SURREAL_DATABASENAME \
    $SURREAL_FILENAME