#!/usr/bin/env bash

set -eou pipefail

fedpkg --name webkitgtk --release f39 mockbuild --enable-network


