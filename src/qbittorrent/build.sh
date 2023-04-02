#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qbittorrent --release f38 mockbuild --enable-network


