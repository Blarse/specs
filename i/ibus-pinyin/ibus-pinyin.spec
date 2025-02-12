Name:    ibus-pinyin
Version: 1.5.1
Release: alt1
Summary: The Chinese Pinyin and Bopomofo engines for IBus input platform

License: GPL-2.0+
Group: System/Libraries
URL: https://github.com/ibus/ibus-pinyin
Source0: %name-%version.tar

Packager:   Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: glib2-devel sqlite3 gcc-c++ python-devel
BuildRequires: gnome-common
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: libsqlite3-devel
BuildRequires: libuuid-devel
BuildRequires: libibus-devel >= 1.5.4
#BuildRequires: lua-devel >= 5.1
BuildRequires: opencc-devel
BuildRequires: pyzy-devel

%add_python3_path %_datadir/%name

%description
The Chinese Pinyin and Bopomofo input methods for IBus platform.

%prep
%setup -q
# Replace doublequotes to singlequotes for sqlite3
subst "s|\\\\\"|\\\\'|g" data/db/english/english.awk

%build
#./autogen.sh
%autoreconf
%configure --disable-static \
           --enable-db-open-phrase \
           --enable-opencc \
           --disable-boost \
           --disable-lua-extension

# make -C po update-gmo
%make_build

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%_libexecdir/ibus-engine-pinyin
%_libexecdir/ibus-setup-pinyin
%_datadir/ibus-pinyin
%_datadir/ibus/component/*
%_desktopdir/*.desktop

%changelog
* Sat Apr 13 2024 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- New version from https://github.com/ibus/ibus-pinyin

* Sun Apr 09 2023 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt7
- FTBFS: replaced doublequotes to singlequotes for sqlite3.

* Mon Aug 29 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt6
- FTBFS: disabled lua extension.

* Tue Jan 14 2020 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt5
- use python3 interpreter

* Wed Aug 21 2019 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt4
- rebuild with python3

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3.1
- rebuild with new lua 5.3

* Thu Jul 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt3
- Rebuild with new version of gcc
- Fix packager name

* Mon May 19 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt2
- Move from autoimport to Sisyphus (ALT #29978)

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_4
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- update to new release by fcimport

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- initial fc import

