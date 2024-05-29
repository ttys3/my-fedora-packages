#!/usr/bin/env bash

set -eou pipefail

fedpkg --name pack --release f$(rpm -E '%fedora') mockbuild --enable-network


