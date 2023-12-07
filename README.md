# ansible-semaphore-api
[![Semaphore Check Version](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/check-version.yml/badge.svg)](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/check-version.yml)
[![OpenAPI](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/openapi-generator.yml/badge.svg)](https://github.com/nchekwa/ansible-semaphore-api/actions/workflows/openapi-generator.yml)

[Ansible Semaphore](https://www.ansible-semaphore.com/) Python API Lib <br> 


<br>

![PyPi](https://pypi.org/static/images/logo-small.2a411bc6.svg) 
```bash
pip install semaphore-api
```

-or- manual installation:
```bash
SEMAPHORE_API_VERSION=$(curl -s https://api.github.com/repos/nchekwa/ansible-semaphore-api/releases/latest | jq -r '.name' | sed 's/^v//')
echo $SEMAPHORE_API_VERSION
curl -LJOs https://github.com/nchekwa/ansible-semaphore-api/raw/main/dist/semaphore_api-$SEMAPHORE_API_VERSION-py3-none-any.whl
pip install semaphore_api-$SEMAPHORE_API_VERSION-py3-none-any.whl
```


# Example:
## Generate token based on user credentials:

```python
from semaphore_api.configuration import Configuration
from semaphore_api.api.authentication_api import AuthenticationApi
from semaphore_api.api_client import ApiClient
from semaphore_api.api.projects_api import ProjectsApi
from semaphore_api.models.login import Login

from semaphore_api.models.api_token import APIToken
from semaphore_api.api_response import ApiResponse
from semaphore_api.api.user_api import UserApi


host = "127.0.0.1"
port="3000"
protocol="http"
username="admin"
password="admin"

configuration = Configuration(
    host = f"{protocol}://{host}:{port}/api",
)
api_client = ApiClient(configuration)
api_instance = AuthenticationApi(api_client)
login_body = Login(auth=username, password=password)

# Parse login-reponse
login:ApiResponse = api_instance.auth_login_post_with_http_info(login_body)
print(f"login -> {type(login)} -> {login}")

# Get Cookie from login-reponse
api_cookie = login.headers['Set-Cookie']
print(f"api_cookie -> {type(api_cookie)} -> {api_cookie}")

# Set Cookie to API Client
api_client.cookie = api_cookie

# Example 1: Get projects based on Cookie
projects_get       = ProjectsApi(api_client).projects_get()
print(f"projects_get -> {type(projects_get)} -> {projects_get}")

# Example 2: Create Token
user_tokens_post:APIToken = UserApi(api_client).user_tokens_post()
print(f"user_tokens_post -> {type(user_tokens_post)} -> {user_tokens_post}")

# Example 3: Delete Token
user_tokens_api_token_id_delete:APIToken = UserApi(api_client).user_tokens_api_token_id_delete(api_token_id=user_tokens_post.id)
print(f"user_tokens_api_token_id_delete -> {type(user_tokens_api_token_id_delete)} -> {user_tokens_api_token_id_delete}")

# Example 4: Get List of all tokens
user_tokens_get = AuthenticationApi(api_client).user_tokens_get()
print(f"user_tokens_get -> {type(user_tokens_get)} -> {user_tokens_get}")

```

Response:
```text
login -> <class 'semaphore_api.api_response.ApiResponse'> -> status_code=204 headers={'Content-Type': 'application/json', 'Set-Cookie': 'semaphore=MTcwMTkyNjcwN3xGRmtnNEVNRnJFUEg5cThLTGlnUVFkZEJnZHY4Y3BlQno0TGNmbzNhTEVXMGZHdi1aWkQ0TmgwRmZkNTlyV09TYkU3WlhmZV9CRXpCczBpc1pwZkd2dGc9fIe8S1uDxjr2z5DjtAY2TDGwTeS4M44usYYhH7iSRpj5; Path=/', 'Date': 'Thu, 07 Dec 2023 05:25:07 GMT'} data=None raw_data=b''

api_cookie -> <class 'str'> -> semaphore=MTcwMTkyNjcwN3xGRmtnNEVNRnJFUEg5cThLTGlnUVFkZEJnZHY4Y3BlQno0TGNmbzNhTEVXMGZHdi1aWkQ0TmgwRmZkNTlyV09TYkU3WlhmZV9CRXpCczBpc1pwZkd2dGc9fIe8S1uDxjr2z5DjtAY2TDGwTeS4M44usYYhH7iSRpj5; Path=/

projects_get -> <class 'list'> -> [Project(id=1, name='Junier', created='2023-11-27T22:36:46.900379365Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=2, name='Cisco', created='2023-11-27T22:36:53.049960469Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=8, name='New Project A', created='2023-12-07T04:54:57.198626268Z', alert=False, alert_chat=None, max_parallel_tasks=0)]

user_tokens_post -> <class 'semaphore_api.models.api_token.APIToken'> -> id='kffsrc7wunuiqswfheu1xhlvrkjhes6d4koyjtvjgt8=' created='0001-01-01T00:00:00Z' expired=False 
user_id=1

user_tokens_api_token_id_delete -> <class 'NoneType'> -> None

user_tokens_get -> <class 'list'> -> [APIToken(id='4tb0h2egdfxccppk5yiyikw38iglq86loe_t6ragmv4=', created='0001-01-01T00:00:00Z', expired=False, user_id=1), APIToken(id='7uxrljogdekxdretrdlhlcqvl3p_6d1rymrqokf5hau=', created='0001-01-01T00:00:00Z', expired=False, user_id=1), APIToken(id='kffsrc7wunuiqswfheu1xhlvrkjhes6d4koyjtvjgt8=', created='0001-01-01T00:00:00Z', expired=True, user_id=1), APIToken(id='ujg3e2irwq5_00gezbzo6qee9ldsqiwnekstfhbv5v4=', created='0001-01-01T00:00:00Z', expired=True, user_id=1), APIToken(id='zkaidtasbkv84q4_4a20wb0j3uhkspvm3tbfwtdm6f4=', created='0001-01-01T00:00:00Z', expired=True, user_id=1)]
```

Please note '<b>kffsrc7wunuiqswfheu1xhlvrkjhes6d4koyjtvjgt8</b>' - that token will not be removed. It will be marked as <b>expired=True</b>



## Connect based on API key (token):

```python
import semaphore_api
from semaphore_api.api.default_api import DefaultApi

from semaphore_api.models.project_request import ProjectRequest
from semaphore_api.models.project import Project
from semaphore_api.api.projects_api import ProjectsApi
from semaphore_api.api.project_api import ProjectApi

from pprint import pprint

def get_id_by_name(items_list, search_name):
    for item in items_list:
        if item.name == search_name:
            return item.id
    return None  # Return None if the name is not found in the list

api_key='7uxrljogdekxdretrdlhlcqvl3p_6d1rymrqokf5hau='
host = "127.0.0.1"
port="3000"
protocol="http"

configuration = semaphore_api.Configuration(
    host = f"{protocol}://{host}:{port}/api",
    api_key = {'bearer': api_key},
    api_key_prefix={'bearer': 'Bearer'}
)
api_client = semaphore_api.ApiClient(configuration)

# Example 1 - Ping
ping_get       = DefaultApi(api_client).ping_get()
print(f"ping_get -> {type(ping_get)} -> {ping_get}")

# Example 2 - Ansible Semaphore Info
info_get       = DefaultApi(api_client).info_get()
print(f"info_get -> {type(info_get)} -> {info_get.__dict__} -> {type(info_get.__dict__)}")

## Example 3 - Create new project
new_project = ProjectRequest(name="New Project A")
projects_post       = ProjectsApi(api_client).projects_post(new_project)
print(f"projects_post -> {type(projects_post)} -> {projects_post}")

# Example 4 - Get List of the project
projects_get       = ProjectsApi(api_client).projects_get()
print(f"projects_get -> {type(projects_get)} -> {projects_get}")

# Extract project ID from list (search by name)
new_project_id = get_id_by_name(ProjectsApi(api_client).projects_get(), new_project.name)
print(f"new_project_id -> {new_project_id}")

# Example 5
project_delete       = ProjectApi(api_client).project_project_id_delete(new_project_id)
print(f"project_delete -> {type(project_delete)} -> {project_delete}")

projects_get       = ProjectsApi(api_client).projects_get()
print(f"projects_get -> {type(projects_get)} -> {projects_get}")
```

Response:
```text
ping_get -> <class 'str'> -> pong

info_get -> <class 'semaphore_api.models.info_type.InfoType'> -> {'version': 'v2.9.37', 'update_body': None, 'update': None} -> <class 'dict'>

projects_post -> <class 'NoneType'> -> None

projects_get -> <class 'list'> -> [Project(id=1, name='Junier', created='2023-11-27T22:36:46.900379365Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=2, name='Cisco', created='2023-11-27T22:36:53.049960469Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=6, name='New Project A', created='2023-12-07T04:45:10.520367408Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=7, name='New Project A', created='2023-12-07T04:46:47.026084765Z', alert=False, alert_chat=None, max_parallel_tasks=0)]

new_project_id -> 6

project_delete -> <class 'NoneType'> -> None

projects_get -> <class 'list'> -> [Project(id=1, name='Junier', created='2023-11-27T22:36:46.900379365Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=2, name='Cisco', created='2023-11-27T22:36:53.049960469Z', alert=False, alert_chat=None, max_parallel_tasks=0), Project(id=7, name='New Project A', created='2023-12-07T04:46:47.026084765Z', alert=False, alert_chat=None, max_parallel_tasks=0)]
```



