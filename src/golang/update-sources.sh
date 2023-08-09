#!/usr/bin/env bash

set -eou pipefail

fedpkg --name golang new-sources --offline *.src.tar.gz


