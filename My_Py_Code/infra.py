import requests


def test_nginx_status(TestinfraBackend):
    host = 'https://jupyter.pp.ua'
    response = requests.get(host)
    assert response.status_code == 200

def test_nginx_is_installed(Package):
    nginx = Package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.10.3")
    
def test_nginx_running_and_enabled(Service):
    nginx = Service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled
  

def test_ntopng_stopped_and_disabled(Service):
    ntopng = Service("ntopng")
    assert ntopng.is_running == False
    assert ntopng.is_enabled == False

def test_redis_is_installed(Package):
    redis = Package("redis-server")
    assert redis.is_installed


def test_config_file(File):
    config_file = File('/etc/redis/redis.conf')
    assert config_file.contains('bind 127.0.0.1')
    assert config_file.is_file


def test_service_running(Service):
    service = Service('redis-server')
    assert service.is_running


def test_socket_listening(Socket):
    socket = Socket('tcp://127.0.0.1:6379')
    assert socket.is_listening


def test_command_output(Command):
    command = Command('redis-cli ping')
    assert command.stdout.rstrip() == 'PONG'
    assert command.rc == 0
