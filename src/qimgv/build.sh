#!/usr/bin/env bash

set -eou pipefail

fedpkg --name qimgv --release $(rpm -E '%fedora') mockbuild --enable-network


