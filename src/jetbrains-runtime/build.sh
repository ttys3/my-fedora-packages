#!/usr/bin/env bash

set -eou pipefail

fedpkg --name jetbrains-runtime --release f40 mockbuild --enable-network


