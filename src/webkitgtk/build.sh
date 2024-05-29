#!/usr/bin/env bash

set -eou pipefail

fedpkg --name webkitgtk --release f$(rpm -E '%fedora') mockbuild --enable-network


