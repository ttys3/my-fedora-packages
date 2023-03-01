#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qbittorrent --release f37 mockbuild --enable-network


