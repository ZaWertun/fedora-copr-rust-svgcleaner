# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate phf_shared

Name:           rust-%{crate}
Version:        0.7.24
Release:        1%{?dist}
Summary:        Support code shared by PHF libraries

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/phf_shared
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(siphasher/default) >= 0.2.0 with crate(siphasher/default) < 0.3.0)
%endif

%global _description %{expand:
Support code shared by PHF libraries.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages
which use "core" feature of "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicase-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicase-devel %{_description}

This package contains library source intended for building other packages
which use "unicase" feature of "%{crate}" crate.

%files       -n %{name}+unicase-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sun Feb 14 00:50:39 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.7.24-1
- Initial package
