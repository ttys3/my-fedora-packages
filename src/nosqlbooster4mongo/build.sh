#!/usr/bin/env bash

set -eou pipefail

fedpkg --name nosqlbooster4mongo --release f38 mockbuild --enable-network


