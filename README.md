# generic_program_install

Base rol to install programs

## Requirements

None

## Role Variables

config:
  directory:
  git_repo:
  packages:

* `install`    : Dictionary with the information of the program to install
  * `packages` : List of packages to install with the package manager
  * `pip_packages` : List of pip packages to install
  * `pip3_packages` : List of pip3 packages to install

* `config`: Dictionary with the information of the configuration
  * `directory`: Base directory to perform the clone of the configuration
    directory, for example: `~/.rcfiles`.
  * `git_repo`: Url to the git group of repositories of your dotfiles, for
    example: `https://git.myrepo.com/rcfiles`.
  * `packages`: List of packages to configure

Imagine that we've set

```yaml
config:
  directory: ~/.rcfiles
  git_repo: https://git.myrepo.com/rcfiles
  packages:
    - package_1
    - package_2

```

The configuration part will clone https://git.myrepo.com/rcfiles/package_1 and
https://git.myrepo.com/rcfiles/package_2 into `~/.rcfiles/package_1` and
`~/.rcfiles/package_2`.

It assumes that in each of those repositories you have the same structure that
you'd have on your home directory, so for example

```bash
$ tree -a ~/.rcfiles/package_1
├── .local
│   └── share
│       └── package_1_dir
└── .package1_rc
```

## Example playbook

```yaml
- hosts: all
  roles:
    - generic_program_install
```

## Testing

To test the role you need [molecule](http://molecule.readthedocs.io/en/latest/).

```bash
molecule test
```

## Todo

* Refactor to avoid duplicated code, keeping in mind the `~/.config` and
  `/.local/share` cases

## License

GPLv2

## Author Information
Lyz (lyz@riseup.net)
