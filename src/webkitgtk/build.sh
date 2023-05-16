#!/usr/bin/env bash

set -eou pipefail

fedpkg --name webkitgtk --release f38 mockbuild --enable-network


