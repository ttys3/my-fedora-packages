#!/usr/bin/env bash

set -eou pipefail

fedpkg --name golang --release f38 mockbuild --enable-network


