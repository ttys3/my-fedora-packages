#!/usr/bin/env bash

set -eou pipefail

fedpkg --name  115pc --release f$(rpm -E '%fedora') mockbuild --enable-network

