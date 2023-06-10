

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
