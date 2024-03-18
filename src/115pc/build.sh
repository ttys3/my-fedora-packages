#!/usr/bin/env bash

set -eou pipefail

fedpkg --name  115pc --release f39 mockbuild --enable-network

