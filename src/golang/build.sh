#!/usr/bin/env bash

set -eou pipefail

fedpkg --name golang --release f$(rpm -E '%fedora') mockbuild --enable-network


