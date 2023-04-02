#!/usr/bin/env bash

set -eou pipefail

fedpkg --name jetbrains-runtime --release f38 mockbuild --enable-network


