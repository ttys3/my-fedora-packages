#!/usr/bin/env bash

set -eou pipefail

fedpkg --name jetbrains-runtime --release f37 mockbuild --enable-network


