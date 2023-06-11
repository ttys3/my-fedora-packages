#!/usr/bin/env bash

set -eou pipefail

fedpkg --name xapian-core --release f38 mockbuild --enable-network


