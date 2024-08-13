#!/usr/bin/env bash

set -eou pipefail

fedpkg --name quickjs --release f$(rpm -E '%fedora') mockbuild --enable-network


