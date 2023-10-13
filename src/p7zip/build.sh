#!/usr/bin/env bash

set -eou pipefail

fedpkg --release f39 --name p7zip mockbuild --enable-network

