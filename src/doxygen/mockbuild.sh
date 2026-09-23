#!/usr/bin/env bash
# Local mockbuild of doxygen against the xapian 2.x packaged in ../xapian-core.
# Usage: ./mockbuild.sh [extra mock args...]
#
# The Fedora chroot only has xapian 1.4, so the RPMs from ../xapian-core/build.sh
# are handed to mock as a local repo. Set XAPIAN_REPO to use another repo instead
# (a URL or a file:// directory with repodata), e.g. the Copr repo once it has 2.x.

set -euo pipefail

cd "$(dirname "$(readlink -f "$0")")"

SPEC="doxygen.spec"
XAPIAN_SPEC="../xapian-core/xapian-core.spec"

VERSION=$(rpmspec -q --qf '%{version}\n' --srpm "$SPEC")
FEDORA_REL=$(rpm -E '%fedora')
ARCH=$(rpm -E '%_arch')
MOCK_ROOT="fedora-${FEDORA_REL}-${ARCH}"
RESULT_DIR="/var/lib/mock/${MOCK_ROOT}/result"

echo ">>> doxygen ${VERSION} on ${MOCK_ROOT}"

if [[ -z "${XAPIAN_REPO:-}" ]]; then
    XAPIAN_RESULTS="../xapian-core/results_xapian-core/$(rpmspec -q --qf '%{version}/%{release}\n' --srpm "$XAPIAN_SPEC")"
    if ! compgen -G "${XAPIAN_RESULTS}/xapian-core-devel-*.rpm" >/dev/null; then
        echo "no xapian-core-devel RPM in ${XAPIAN_RESULTS}, run ../xapian-core/build.sh first" >&2
        exit 1
    fi
    XAPIAN_REPO_DIR=$(mktemp -d)
    trap 'rm -rf "${XAPIAN_REPO_DIR}"' EXIT
    cp "${XAPIAN_RESULTS}"/*.rpm "${XAPIAN_REPO_DIR}/"
    rm -f "${XAPIAN_REPO_DIR}"/*.src.rpm
    createrepo_c --quiet "${XAPIAN_REPO_DIR}"
    XAPIAN_REPO="file://${XAPIAN_REPO_DIR}"
fi
echo "    xapian repo: ${XAPIAN_REPO}"

echo ">>> [1/3] fetching sources from the Fedora lookaside cache"
fedpkg --name doxygen --release "f${FEDORA_REL}" sources

echo ">>> [2/3] building SRPM"
rm -f ./*.src.rpm
fedpkg --name doxygen --release "f${FEDORA_REL}" srpm
SRPM=$(ls -1t ./*.src.rpm | head -n1)
echo "    SRPM: ${SRPM}"

echo ">>> [3/3] mock --rebuild"
mock -r "${MOCK_ROOT}" --addrepo="${XAPIAN_REPO}" --rebuild "${SRPM}" "$@"

echo ">>> done"
echo ">>> build artifacts in ${RESULT_DIR}"
ls -1 "${RESULT_DIR}"/*.rpm 2>/dev/null | grep -v '\.src\.rpm$' | sed 's/^/    /' || true
