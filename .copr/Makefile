
srpm:
	echo "cwd: $(shell pwd)"
	echo "outdir: $(outdir)"
	echo "spec: $(spec)"
	echo "spec dir: $(dir $(spec))"
	test -d $(outdir) || mkdir -p $(outdir)
	dnf -y install -y curl git rpm-build
	cd $(dir $(spec))
	curl -LZO 'https://webkitgtk.org/releases/webkitgtk-2.38.4.tar.xz'
	curl -LZO 'https://webkitgtk.org/releases/webkitgtk-2.38.4.tar.xz.asc'
	test -d SOURCES || mkdir SOURCES
	cp -v *.patch ./SOURCES/
	cp -v *.gpg ./SOURCES/
	cp -v *.tar* ./SOURCES/
	rpmbuild --define "_topdir `pwd`" -bs webkitgtk.spec
	mv ./SRPMS/*.src.rpm $(outdir)/