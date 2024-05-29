#!/usr/bin/env bash

set -eou pipefail

fedpkg --name nosqlbooster4mongo --release f$(rpm -E '%fedora') mockbuild --enable-network


