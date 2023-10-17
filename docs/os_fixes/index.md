I use a Lenovo IdeaPad 3 with Garuda Linux installed on it. I have a dual boot setup with Windows 10 and Garuda Linux. I use Windows 10 for college assignments and Garuda Linux for everything else.

My system info is as follows:

```bash title="cat /etc/os-release"
NAME="Garuda Linux"
PRETTY_NAME="Garuda Linux"
ID=garuda
ID_LIKE=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://garudalinux.org/"
DOCUMENTATION_URL="https://wiki.garudalinux.org/"
SUPPORT_URL="https://forum.garudalinux.org/"
BUG_REPORT_URL="https://gitlab.com/groups/garuda-linux/"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
```

```bash title="uname -r"
6.1.55-1-lts
```

```bash title="inxi -Fxxxza --no-host"
System:
  Kernel: 6.1.55-1-lts arch: x86_64 bits: 64 compiler: gcc v: 13.2.1
    clocksource: hpet available: acpi_pm
    parameters: BOOT_IMAGE=/@/boot/vmlinuz-linux-lts
    root=UUID=62356c5b-fc37-4a8c-9498-2dc26dd64f68 rw rootflags=subvol=@
    quiet rd.udev.log_priority=3 vt.global_cursor_default=0
    systemd.unified_cgroup_hierarchy=1 loglevel=3 ibt=off
  Desktop: KDE Plasma v: 5.27.8 tk: Qt v: 5.15.10 info: polybar wm: kwin_x11
    vt: 2 dm: SDDM Distro: Garuda Linux base: Arch Linux
Machine:
  Type: Laptop System: LENOVO product: 82KT v: IdeaPad 3 14ALC6
    serial: <superuser required> Chassis: type: 10 v: IdeaPad 3 14ALC6
```
