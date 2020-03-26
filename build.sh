#!/usr/bin/env bash

# Source variables from the versionfile
. ./version; export $(cut -d= -f1 version)

# Build image from the local directory
docker build . -t keywords:${RELEASE}.${MAJOR}.${MINOR}.${HOTFIX} --no-cache

