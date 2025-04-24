[![build-test](https://github.com/darkwizard242/ansible-role-crictl/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-crictl/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-crictl/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-crictl/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/crictl) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-crictl&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-crictl) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-crictl&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-crictl) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-crictl&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-crictl) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-crictl?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-crictl?color=orange&style=flat-square)

# Ansible Role: crictl

Role to install (_by default_) [crictl](https://github.com/kubernetes-sigs/cri-tools) on **Debian/Ubuntu** and **EL** systems. **crictl** is CLI tool for Kubernetes Container Runtime Interface.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
crictl_app: crictl
crictl_version: 1.33.0
crictl_os: "{{ ansible_system | lower }}"
crictl_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
crictl_dl_url: https://github.com/kubernetes-sigs/cri-tools/releases/download/v{{ crictl_version }}/{{ crictl_app }}-v{{ crictl_version }}-{{ crictl_os }}-{{ crictl_architecture_map[ansible_architecture] }}.tar.gz
crictl_bin_path: /usr/local/bin
crictl_file_owner: root
crictl_file_group: root
```

### Variables table:

Variable                | Description
----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------
crictl_app              | Defines the app to install i.e. **crictl**
crictl_version          | Defined to dynamically fetch the desired version to install. Defaults to: **1.33.0**
crictl_os               | Defines os type.
crictl_architecture_map | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture.
crictl_dl_url           | Defines URL to download the crictl binary from.
crictl_bin_path         | Defined to dynamically set the appropriate path to store crictl binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
crictl_file_owner       | Owner for the binary file of crictl.
crictl_file_group       | Group for the binary file of crictl.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **crictl**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.crictl
```

For customizing behavior of role (i.e. specifying the desired **crictl** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.crictl
  vars:
    crictl_version: 1.21.0
```

For customizing behavior of role (i.e. placing binary of **crictl** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.crictl
  vars:
    crictl_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-crictl/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
