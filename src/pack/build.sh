#!/usr/bin/env bash

set -eou pipefail

fedpkg --name pack --release f39 mockbuild --enable-network


