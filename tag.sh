#!/usr/bin/env bash

# warning: you need cd to spec dir to run this scripts

set -eou pipefail

#tito tag --keep-version --no-auto-changelog
tito tag --keep-version

git push --follow-tags origin -f
