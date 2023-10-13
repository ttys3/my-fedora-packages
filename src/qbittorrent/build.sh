#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qbittorrent --release f39 mockbuild --enable-network


