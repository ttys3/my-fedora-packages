#!/usr/bin/env bash

set -eou pipefail

fedpkg --name xapian-core --release f40 mockbuild --enable-network


