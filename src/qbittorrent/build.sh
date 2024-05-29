#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qbittorrent --release f$(rpm -E '%fedora') mockbuild --enable-network


