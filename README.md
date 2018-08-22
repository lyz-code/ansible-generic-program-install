# generic_program_install

Base rol to install programs

## Requirements

None

## Role Variables
* `program`    : Dictionary with the information of the program
  * `name`     : Program name
  * `packages` : List of packages to install
  * `pip_packages` : List of pip packages to install
  * `pip3_packages` : List of pip3 packages to install

* `config`: Dictionary with the information of the configuration
  * `directory`: Base directory to perform the clone of the configuration
    directory
  * `git_repo`: Git repository of your dotfiles. It's assumed that the
    repository has the same structure as your home directory. For example, in
    the root of my vim configuration git repository I've got a directory called
    `.vim` and a `.vimrc` file.


## Example of use in a role

### Install and configure
```yaml
- name: Name of task
  include_role:
    name: generic_program_install
```

### Just install
```yaml
- name: Name of task
  include_role:
    name: generic_program_install
    tasks_from: install
```

### Just install

```yaml
- name: Name of task
  include_role:
    name: generic_program_install
    tasks_from: configure
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
