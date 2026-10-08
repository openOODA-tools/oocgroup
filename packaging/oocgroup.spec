Name:           oocgroup
Version:        0.2.0
Release:        1%{?dist}
Summary:        Creates and configures cgroup v2 resource limits for memory, cpu, and io controllers.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocgroup
Source0:        oocgroup-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocgroup is a sovereign, capability-bounded CGROUP MANAGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocgroup
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocgroup-uninstall

%files
/usr/bin/oocgroup
/usr/bin/oocgroup-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to pure native openOODA with dual CLI/MCP and tri-dist packaging
