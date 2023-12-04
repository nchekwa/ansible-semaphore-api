# ansible-semaphore-api
[![OpenAPI](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/openapi-generator.yml/badge.svg)](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/openapi-generator.yml)
[![Python PyPi](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/python-pypi.yml/badge.svg)](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/python-pypi.yml)

[Ansible Semaphore](https://www.ansible-semaphore.com/) Python API Lib <br> 


<br>

![PyPi](https://pypi.org/static/images/logo-small.2a411bc6.svg) 
```bash
pip install semaphore-api
```

-or- manual installation:
```bash
pip install semaphore_api-2.x.x-py3-none-any.whl
```


# Example:
Connect based on API key:

```python
import semaphore_api
from semaphore_api.api.default_api import DefaultApi as SemaphoreDefaultApi
from semaphore_api.api.projects_api import ProjectsApi as SemaphoreProjectsApi

api_key='7uxrljogdekxdretrdlhlcqvl3p_6d1rymrqokf5hau='
host = "127.0.0.1"
port="3000"
protocol="http"

ansible_sempaphore_configuration = semaphore_api.Configuration(
    host = f"{protocol}://{host}:{port}/api",
    api_key = {'bearer': api_key},
    api_key_prefix={'bearer': 'Bearer'}
)
ansible_sempaphore_client = semaphore_api.ApiClient(ansible_sempaphore_configuration)

info_get       = SemaphoreDefaultApi(ansible_sempaphore_client).info_get()
print(info_get)
projects       = SemaphoreProjectsApi(ansible_sempaphore_client).projects_get()
print(projects)
```
