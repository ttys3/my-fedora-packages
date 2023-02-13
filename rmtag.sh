#!/usr/bin/env bash

set -eou pipefail

tag=$1

git tag -d "$tag"

git push origin --delete "$tag"
