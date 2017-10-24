import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_parent_non_hidden_file(host):
    f = host.file('/root/README.md')
    assert f.exists
    assert f.is_symlink
    assert f.contains('This repository is for')


def test_parent_hidden_file(host):
    f = host.file('/root/.test_programrc')
    assert f.exists
    assert f.is_symlink
    assert f.contains('Making Gentooza life easy')


def test_config_file(host):
    f = host.file('/root/.config/test_program/file_1')
    assert f.exists
    assert f.contains('Making Gentooza life easy')


def test_local_share_file(host):
    f = host.file('/root/.local/share/test_program/file_1')
    assert f.exists
    assert f.contains('Making Gentooza life easy')


def test_vim_is_installed(host):
    vim = host.package("vim")
    assert vim.is_installed


def test_pip_package_installed(host):
    packages = host.pip_package.get_packages()
    assert 'pytest' in packages
