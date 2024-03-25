#!/usr/bin/env bash

set -eou pipefail

fedpkg --name golang --release f40 mockbuild --enable-network


