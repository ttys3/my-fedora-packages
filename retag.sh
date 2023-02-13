#!/usr/bin/env bash

set -eou pipefail

tag=$1

git tag -d "$tag"

git push origin --delete "$tag"

tito tag --keep-version

git push --follow-tags origin -f
