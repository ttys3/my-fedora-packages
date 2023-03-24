#!/usr/bin/env bash

set -eou pipefail

fedpkg --release f38 --name p7zip mockbuild --enable-network

