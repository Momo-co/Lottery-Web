#!/bin/bash

scp docker-compose.yaml swarm-manager:
ssh swarm-manager << EOF
    export DATABASE_URI=$DATABASE_URI SECRET_KEY=$SECRET_KEY
    docker stack deploy --compose-file docker-compose.yaml lottery
EOF