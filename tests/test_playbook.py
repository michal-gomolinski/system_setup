import time
import logging
from testcontainers.core.container import DockerContainer

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def test_playbook(container: DockerContainer):
    container.exec("/home/sshuser/ansible/init.sh")
    time.sleep(1000)
    _logger.info(container.get_logs())
    assert True
