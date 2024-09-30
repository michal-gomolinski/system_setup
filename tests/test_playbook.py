import pytest
import logging
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def run_in_container(container: DockerContainer, command: str, workdir=None):
    if container._container:
        result = ""
        for r in container._container.exec_run(
            command, stream=True, workdir=workdir
        ).output:
            _logger.debug(r.decode("utf-8"))
            result += r.decode("utf-8")
        return result

    raise Exception("Container is not running")


@pytest.mark.slow
def test_init_env(plain_container: DockerContainer):
    result = run_in_container(
        container=plain_container,
        command="init.sh",
        workdir="/home/ansible/ansible",
    )

    # _logger.info(container.get_logs())
    installed_python_pakages = run_in_container(
        container=plain_container, command="pip list"
    )

    assert "ansible" in installed_python_pakages
    assert "pip" in installed_python_pakages


@pytest.mark.slow
def test_run_playbook(ansible_container: DockerContainer):
    result = run_in_container(
        container=ansible_container,
        command="ansible-playbook --connection=local -i inventory.ini setup_playbook.yml",
        workdir="/home/ansible/ansible",
    )

    assert "localhost" in result
    assert "failed=0" in result
    assert "unreachable=0" in result
    # assert "changed=0" in result
    assert "ignored=0" in result
    assert "skipped=0" in result

    result = run_in_container(
        container=ansible_container,
        command="apt list --installed",
    )

    _logger.info(result)

    assert "python3-venv" in result
    assert "docker-ce" in result
    assert "docker-ce-cli" in result
    assert "containerd.io" in result
    assert "docker-compose-plugin" in result
    assert "docker-buildx-plugin" in result
    assert "zsh" in result

    result = run_in_container(
        container=ansible_container,
        command='/bin/bash -c "source $HOME/.nvm/nvm.sh && nvm --version && node --version"',
    )
    assert "0.40.1" in result
    assert "v20.17.0" in result
