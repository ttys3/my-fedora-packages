#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qbittorrent --release f40 mockbuild --enable-network


