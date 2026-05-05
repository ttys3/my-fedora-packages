#!/usr/bin/env bash
# Local mockbuild without hitting Fedora dist-git lookaside cache.
# Usage: ./mockbuild.sh [extra mock args...]

set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"

SPEC="kitty.spec"
VENDOR_CONFIG="./go-vendor-tools.toml"

VERSION=$(rpmspec -q --qf '%{version}\n' --srpm "$SPEC")
FEDORA_REL=$(rpm -E '%fedora')
ARCH=$(rpm -E '%_arch')
UPSTREAM_TARBALL="kitty-${VERSION}.tar.xz"
VENDOR_TARBALL="kitty-vendor.tar.xz"

echo ">>> kitty ${VERSION} on fedora-${FEDORA_REL}-${ARCH}"

echo ">>> [1/4] fetching upstream sources into $(pwd)"
spectool -C . -g "$SPEC"

echo ">>> [2/4] generating go vendor archive"
go_vendor_archive create --config "$VENDOR_CONFIG" "./${UPSTREAM_TARBALL}" -O "${VENDOR_TARBALL}"

echo ">>> [3/4] building SRPM (no lookaside)"
rm -f ./*.src.rpm
fedpkg --release "f${FEDORA_REL}" srpm
SRPM=$(ls -1t ./*.src.rpm | head -n1)
echo "    SRPM: ${SRPM}"

echo ">>> [4/4] mock --rebuild"
mock -r "fedora-${FEDORA_REL}-${ARCH}" --enable-network --rebuild "${SRPM}" "$@"

echo ">>> done"
