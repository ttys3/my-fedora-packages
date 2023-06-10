
## how to install

```shell
# for dev
sudo dnf --disablerepo='*' --enablerepo=copr:copr.fedorainfracloud.org:ttys3:my-fedora-packages reinstall xapian-core xapian-core-devel xapian-core-libs

# for debug
sudo dnf --disablerepo='*' --enablerepo=copr:copr.fedorainfracloud.org:ttys3:my-fedora-packages reinstall xapian-core-debuginfo xapian-core-debugsource xapian-core-libs-debuginfo
```

## compile troubleshoot

```
checking whether g++ is a working C++ compiler... yes
./configure: line 18129: syntax error near unexpected token `17'
./configure: line 18129: `AX_CXX_COMPILE_STDCXX(17)'
```

```shell
sudo dnf install -y autoconf-archive
autoreconf -ifv
```

how to manual build:

```shell
/usr/bin/make -O -j10 V=1 VERBOSE=1

/usr/bin/make install DESTDIR=$(pwd)/result INSTALL="/usr/bin/install -p"
```


## notice

xapian header file path

1.5 is
```
/usr/include/xapian-1.5/xapian.h
/usr/include/xapian-1.5/xapian/*.h
```

1.4.x is
```
/usr/include/xapian.h
/usr/include/xapian/*.h
```
