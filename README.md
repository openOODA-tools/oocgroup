# oocgroup: Sovereign CGROUP MANAGER

<div align="center">

```
================================================================================
                                oocgroup
               Sovereign openOODA CGROUP MANAGER
================================================================================
```

**Sovereign CGROUP MANAGER**  
*Creates and configures cgroup v2 resource limits for memory, cpu, and io controllers.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocgroup/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocgroup-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocgroup/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocgroup/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocgroup-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocgroup/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocgroup [options] [PATH]

Creates and configures cgroup v2 resource limits for memory, cpu, and io controllers.

Options:
  -p, --path <PATH>    inspect target cgroup v2 path (default: current cgroup)
  -i, --info           display comprehensive controller and subtree inspection
  -a, --audit          audit security delegation, unconstrained limits, and OOM risk
  -s, --systemd        generate systemd service drop-in configuration
  -m, --memory <SPEC>  specify memory limit (e.g. 512M, 2G, max)
  -c, --cpu <SPEC>     specify CPU quota percentage (e.g. 50%, 200%, max)
      --pids <MAX>     specify maximum task/pid count (e.g. 1000)
  -u, --unit <NAME>    systemd unit name for drop-in generation (default: app)
  -t, --tree           display cgroup hierarchy tree
      --demo           run against synthetic demo cgroup
      --json           output formatted as JSON Lines
  -h, --help           display this help and exit
  -v, --version        output version information and exit
      --mcp            run as Model Context Protocol stdio server
```

---

## 3. Theming Integration (`oote`)

`oocgroup` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocgroup` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oocgroup --mcp
```

### Available Tools

* **`cgroup_inspect`**: Inspect cgroup hierarchy, active controllers, limits, and usage.
  * Parameters: `path` (string, optional)
* **`cgroup_limits`**: Calculate and parse memory, CPU quota, and PID limits.
  * Parameters: `memory` (string), `cpu` (string), `pids` (string)
* **`cgroup_systemd`**: Synthesize a systemd service drop-in unit snippet (`50-cgroup-limits.conf`).
  * Parameters: `unit` (string), `memory` (string), `cpu` (string), `pids` (string)
* **`cgroup_audit`**: Audit cgroup security delegation, unconstrained limits, and OOM risks.
  * Parameters: `path` (string, optional)
* **`cgroup_tree`**: Display visual cgroup hierarchy subtree.
  * Parameters: `path` (string, optional)

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&ProcCap, &SysInfoCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
