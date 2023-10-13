#!/usr/bin/env bash

set -eou pipefail

fedpkg --name nosqlbooster4mongo --release f39 mockbuild --enable-network


