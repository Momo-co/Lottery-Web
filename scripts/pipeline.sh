#!/bin/bash

set -e

# Install dependencies
bash scripts/setup.sh

# Run unit tests
bash scripts/test.sh

# Build and push Docker images
bash scripts/build.sh

# Configure hosts for deployment
bash scripts/config.sh

# Deploy stack to manager
bash scripts/deploy.sh
