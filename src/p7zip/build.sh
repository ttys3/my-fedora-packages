#!/usr/bin/env bash

set -eou pipefail

fedpkg --release f40 --name p7zip mockbuild --enable-network

