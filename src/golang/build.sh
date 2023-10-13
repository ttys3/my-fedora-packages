#!/usr/bin/env bash

set -eou pipefail

fedpkg --name golang --release f39 mockbuild --enable-network


