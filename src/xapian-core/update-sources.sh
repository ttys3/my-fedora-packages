#!/usr/bin/env bash

set -eou pipefail

fedpkg --name xapian-core new-sources --offline *.tar.xz*


