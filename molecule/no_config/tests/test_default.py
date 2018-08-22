import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("package", [
    ("git"),
    ("python-pip"),
    ("python3-pip"),
])
def test_dependencies_are_installed(host, package):
    git = host.package("git")
    assert git.is_installed


def test_vim_is_installed(host):
    vim = host.package("vim")
    assert vim.is_installed
