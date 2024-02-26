%global _unpackaged_files_terminate_build 1

%global import_path github.com/project-zot/zot

Name: zot
Version: 2.0.1
Release: alt1

Summary: zot - A production-ready vendor-neutral OCI-native container image registry (purely based on OCI Distribution Specification)
License: Apache-2.0
Group: Other
Url: https://zotregistry.dev/
Vcs: https://github.com/project-zot/zot

Source: %name-%version.tar
Source1: zui.tar
Source2: zot.service
Source3: config.json

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: node >= 18

%description
zot: a production-ready vendor-neutral OCI image registry -
images stored in OCI image format,
distribution specification on-the-wire, that's it!

%prep
%setup
tar -xvf %SOURCE1
# don't need modcheck, it calls go mod tidy
sed -i 's/^binary: modcheck build-metadata$/binary: build-metadata/' Makefile
sed -i 's/^cli: modcheck build-metadata$/cli: build-metadata/' Makefile
sed -i 's/^bench: modcheck build-metadata$/bench: build-metadata/' Makefile
# don't strip debug information
sed -E -i 's/go build (.?*) -s -w/go build \1/' Makefile
# fixes: -buildmode=pie requires external (cgo) linking, but cgo is not enabled
sed -i 's/CGO_ENABLED=0/CGO_ENABLED=1/' Makefile

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
# build the web ui
pushd zui/
npm run build
popd

%make COMMIT=%release ZUI_BUILD_PATH="$BUILDDIR/src/%import_path/zui/build" binary cli bench

./bin/zot-linux-%go_hostarch completion bash > zot.bash
./bin/zot-linux-%go_hostarch completion zsh > zot.zsh
./bin/zot-linux-%go_hostarch completion fish > zot.fish

./bin/zli-linux-%go_hostarch completion bash > zli.bash
./bin/zli-linux-%go_hostarch completion zsh > zli.zsh
./bin/zli-linux-%go_hostarch completion fish > zli.fish

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

cd .build/src/%import_path

install -Dm 755 ./bin/zot-linux-%go_hostarch %buildroot%_bindir/%name
install -Dm 755 ./bin/zli-linux-%go_hostarch %buildroot%_bindir/zli
install -Dm 755 ./bin/zb-linux-%go_hostarch %buildroot%_bindir/zb

install -Dm 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 644 %SOURCE3 %buildroot%_sysconfdir/%name/config.json

install -Dm 755 zot.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 755 zot.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -Dm 755 zot.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

install -Dm 755 zli.bash %buildroot%_datadir/bash-completion/completions/zli
install -Dm 755 zli.zsh %buildroot%_datadir/zsh/site-functions/_zli
install -Dm 755 zli.fish %buildroot%_datadir/fish/vendor_completions.d/zli.fish

mkdir -p %buildroot%_localstatedir/%name

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -r -g _%name -M -d %_localstatedir/%name -s /dev/null -c "Zot registry user" \
    _%name > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%_bindir/%name
%_bindir/zli
%_bindir/zb
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.json
%_unitdir/%name.service
%attr(775, _%name, _%name) %dir %_localstatedir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/bash-completion/completions/zli
%_datadir/zsh/site-functions/_zli
%_datadir/fish/vendor_completions.d/zli.fish

%changelog
* Mon Feb 19 2024 Alexander Stepchenko <geochip@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
