# doxygen

Fedora's doxygen, rebuilt so that its search tools (`doxyindexer`,
`doxysearch.cgi`) link the xapian 2.x from `../xapian-core` (`libxapian.so.45`).

Fedora's own doxygen links xapian 1.4 (`libxapian.so.30`), so it cannot be
installed next to xapian 2.x: dnf resolves `dnf install doxygen` by downgrading
xapian-core, xapian-core-libs and xapian-core-devel to 1.4.

The packaging is imported unchanged from https://src.fedoraproject.org/rpms/doxygen;
the only local changes are `BuildRequires: xapian-core-devel >= 2.0` and the
Release bump.

## how to build

```shell
# build xapian-core first; mockbuild.sh hands its RPMs to mock as a local repo
(cd ../xapian-core && ./build.sh)
./mockbuild.sh
```
