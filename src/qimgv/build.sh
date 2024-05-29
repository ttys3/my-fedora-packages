#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qimgv --release f$(rpm -E '%fedora') mockbuild --enable-network


