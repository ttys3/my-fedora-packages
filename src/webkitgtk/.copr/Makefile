
srpm:
	echo "cwd: $(shell pwd)"
	echo "outdir: $(outdir)"
	echo "spec: $(spec)"
	test -d $(outdir) || mkdir -p $(outdir)
	dnf -y install -y curl git tito
	curl -LZO 'https://webkitgtk.org/releases/webkitgtk-2.38.4.tar.xz'
	curl -LZO 'https://webkitgtk.org/releases/webkitgtk-2.38.4.tar.xz.asc'
	tito build --test --srpm --output=$(outdir)