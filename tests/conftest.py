import pytest
import logging
from pathlib import Path
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

_TESTS_DIR = Path(__file__).parent

_logger = logging.getLogger(__name__)


@pytest.fixture
def ssh_container():
    image = DockerContainer(
        image="ssh_test",
    )
    image.volumes = {_TESTS_DIR.parent: {"bind": "/home/sshuser/ansible", "mode": "rw"}}
    image.start()
    _logger.info("Starting container")
    wait_for_logs(image, "...done.")
    _logger.info("Container started")
    yield image
    image.stop()


@pytest.fixture
def ansible_container():
    image = DockerContainer(
        image="ansible_test",
    )
    # ~/.ssh:/root/.ssh:ro
    image.volumes = {
        _TESTS_DIR.parent: {"bind": "/home/ansible/ansible", "mode": "rw"},
    }
    image.start()
    _logger.info("Container started")
    yield image
    image.stop()


@pytest.fixture
def plain_container():
    image = DockerContainer(
        image="plain_test",
    )
    image.volumes = {_TESTS_DIR.parent: {"bind": "/home/ansible/ansible", "mode": "rw"}}
    image.start()
    _logger.info("Container started")
    yield image
    image.stop()
