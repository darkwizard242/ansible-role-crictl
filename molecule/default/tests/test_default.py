import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/crictl'


def test_crictl_binary_exists(host):
    """
    Tests if crictl binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_crictl_binary_file(host):
    """
    Tests if crictl binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_crictl_binary_which(host):
    """
    Tests the output to confirm crictl's binary location.
    """
    assert host.check_output('which crictl') == PACKAGE_BINARY
