#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qbittorrent new-sources --offline qbittorrent-*.tar.xz*


