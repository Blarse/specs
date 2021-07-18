%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-firefox
Version: 2.12
Release: alt1

Summary: Firefox-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/mozilla/policy-templates
BuildArch: noarch

BuildRequires: admx-lint

Source0: policy-templates.tar

%description
Firefox-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy-templates

%install
mkdir -p %buildroot%_datadir
cp -a windows/ %buildroot%_destdir
for file in %buildroot%_destdir/*.admx %buildroot%_destdir/*-*/*.adml; do
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsd=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsd="http:\/\/www.w3.org\/2001\/XMLSchema"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsi=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsi="http:\/\/www.w3.org\/2001\/XMLSchema-instance"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns="http:\/\/schemas.microsoft.com\/GroupPolicy\/2006\/07\/PolicyDefinitions"/' "$file"
done

%check
for file in %buildroot%_destdir/*.admx %buildroot%_destdir/*-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%dir %_destdir
%dir %_destdir/*-*/
%_destdir/*.admx
%_destdir/*/*.adml

%changelog
* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.12-alt1
- Update to new release
- Add admx-lint check with special workaround:
  https://github.com/altlinux/admx-lint/issues/1

* Fri May 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.10-alt1
- Update to new release with russian translation
- Set right URL of upstream project

* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 2.9-alt1
- Initial release 

