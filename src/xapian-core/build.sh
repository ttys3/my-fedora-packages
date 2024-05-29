#!/usr/bin/env bash

set -eou pipefail

fedpkg --name xapian-core --release f$(rpm -E '%fedora') mockbuild --enable-network


