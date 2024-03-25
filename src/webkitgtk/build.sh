#!/usr/bin/env bash

set -eou pipefail

fedpkg --name webkitgtk --release f40 mockbuild --enable-network


