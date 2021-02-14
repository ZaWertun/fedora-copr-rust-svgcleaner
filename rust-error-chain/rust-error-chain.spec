# Generated by rust2rpm 16
%bcond_with check

%global crate error-chain

Name:           rust-%{crate}
Version:        0.11.0
Release:        1%{?dist}
Summary:        Yet another error boilerplate library

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/error-chain
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Yet another error boilerplate library.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/has_backtrace
%endif

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
%cargo_build -- --no-default-features

%install
%cargo_install -- --no-default-features

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sun Feb 14 00:29:01 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 0.11.0-1
- Initial package
