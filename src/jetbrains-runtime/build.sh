#!/usr/bin/env bash

set -eou pipefail

fedpkg --name jetbrains-runtime --release f39 mockbuild --enable-network


