# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate bitflags

Name:           rust-%{crate}
Version:        1.2.1
Release:        1%{?dist}
Summary:        Macro to generate structures which behave like bitflags

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bitflags
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Macro to generate structures which behave like bitflags.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+example_generated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+example_generated-devel %{_description}

This package contains library source intended for building other packages
which use "example_generated" feature of "%{crate}" crate.

%files       -n %{name}+example_generated-devel
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
* Sun Feb 14 00:29:43 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.2.1-1
- Initial package
