#!/usr/bin/env bash

set -eou pipefail

fedpkg --name xapian-core --release f39 mockbuild --enable-network


