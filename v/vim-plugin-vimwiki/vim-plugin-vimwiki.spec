%define oname vimwiki

Name: vim-plugin-vimwiki
Version: 2023.04.04_1
Release: alt1

Summary: A personal wiki for Vim

License: MIT
Group: Editors
Url: https://vimwiki.github.io/

VCS: git://git.altlinux.org/gears/v/%name.git
Source: %name-%version.tar
Source1: %name.watch

Provides: %oname = %version

BuildRequires: rpm-build-vim
BuildArch: noarch

%description
VimWiki is a personal wiki for Vim -- a number of linked text files that have
their own syntax highlighting.

With VimWiki, you can:

- Organize notes and ideas
- Manage to-do lists
- Write documentation
- Maintain a diary
- Export everything to HTML

To do a quick start, press `<Leader>ww` (default is `\ww`) to go to your index
wiki file. By default, it is located in `~/vimwiki/index.wiki`. See `:h vimwiki_list`
for registering a different path/wiki.

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
find . -mindepth 1 -maxdepth 1 -type d \
	-not -name '.*' -and \
	-not -name doc -and \
	-not -name test \
	-exec cp -a -t %buildroot%vim_runtime_dir '{}' ';'
mkdir -p %buildroot%vim_runtime_dir/doc
cp -a doc/*.txt %buildroot%vim_runtime_dir/doc

%files
%doc CONTRIBUTING.md doc/design_notes.md LICENSE.md
%vim_runtime_dir/*/*

%changelog
* Sat Apr 08 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 2023.04.04_1-alt1
- Updated to v2023.04.04_1.

* Sun Dec 18 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2022.12.02-alt1
- Updated to v2022.12.02.

* Thu Apr 21 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.5.0.1.git63af6e7-alt1
- Initial build for ALT Sisyphus.
