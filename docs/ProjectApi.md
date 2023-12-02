# semaphore_api.ProjectApi

All URIs are relative to *http://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_project_id_delete**](ProjectApi.md#project_project_id_delete) | **DELETE** /project/{project_id}/ | Delete project
[**project_project_id_environment_environment_id_delete**](ProjectApi.md#project_project_id_environment_environment_id_delete) | **DELETE** /project/{project_id}/environment/{environment_id} | Removes environment
[**project_project_id_environment_environment_id_put**](ProjectApi.md#project_project_id_environment_environment_id_put) | **PUT** /project/{project_id}/environment/{environment_id} | Update environment
[**project_project_id_environment_get**](ProjectApi.md#project_project_id_environment_get) | **GET** /project/{project_id}/environment | Get environment
[**project_project_id_environment_post**](ProjectApi.md#project_project_id_environment_post) | **POST** /project/{project_id}/environment | Add environment
[**project_project_id_events_get**](ProjectApi.md#project_project_id_events_get) | **GET** /project/{project_id}/events | Get Events related to this project
[**project_project_id_get**](ProjectApi.md#project_project_id_get) | **GET** /project/{project_id}/ | Fetch project
[**project_project_id_inventory_get**](ProjectApi.md#project_project_id_inventory_get) | **GET** /project/{project_id}/inventory | Get inventory
[**project_project_id_inventory_inventory_id_delete**](ProjectApi.md#project_project_id_inventory_inventory_id_delete) | **DELETE** /project/{project_id}/inventory/{inventory_id} | Removes inventory
[**project_project_id_inventory_inventory_id_put**](ProjectApi.md#project_project_id_inventory_inventory_id_put) | **PUT** /project/{project_id}/inventory/{inventory_id} | Updates inventory
[**project_project_id_inventory_post**](ProjectApi.md#project_project_id_inventory_post) | **POST** /project/{project_id}/inventory | create inventory
[**project_project_id_keys_get**](ProjectApi.md#project_project_id_keys_get) | **GET** /project/{project_id}/keys | Get access keys linked to project
[**project_project_id_keys_key_id_delete**](ProjectApi.md#project_project_id_keys_key_id_delete) | **DELETE** /project/{project_id}/keys/{key_id} | Removes access key
[**project_project_id_keys_key_id_put**](ProjectApi.md#project_project_id_keys_key_id_put) | **PUT** /project/{project_id}/keys/{key_id} | Updates access key
[**project_project_id_keys_post**](ProjectApi.md#project_project_id_keys_post) | **POST** /project/{project_id}/keys | Add access key
[**project_project_id_put**](ProjectApi.md#project_project_id_put) | **PUT** /project/{project_id}/ | Update project
[**project_project_id_repositories_get**](ProjectApi.md#project_project_id_repositories_get) | **GET** /project/{project_id}/repositories | Get repositories
[**project_project_id_repositories_post**](ProjectApi.md#project_project_id_repositories_post) | **POST** /project/{project_id}/repositories | Add repository
[**project_project_id_repositories_repository_id_delete**](ProjectApi.md#project_project_id_repositories_repository_id_delete) | **DELETE** /project/{project_id}/repositories/{repository_id} | Removes repository
[**project_project_id_repositories_repository_id_put**](ProjectApi.md#project_project_id_repositories_repository_id_put) | **PUT** /project/{project_id}/repositories/{repository_id} | Updates repository
[**project_project_id_role_get**](ProjectApi.md#project_project_id_role_get) | **GET** /project/{project_id}/role | Fetch permissions of the current user for project
[**project_project_id_tasks_get**](ProjectApi.md#project_project_id_tasks_get) | **GET** /project/{project_id}/tasks | Get Tasks related to current project
[**project_project_id_tasks_last_get**](ProjectApi.md#project_project_id_tasks_last_get) | **GET** /project/{project_id}/tasks/last | Get last 200 Tasks related to current project
[**project_project_id_tasks_post**](ProjectApi.md#project_project_id_tasks_post) | **POST** /project/{project_id}/tasks | Starts a job
[**project_project_id_tasks_task_id_delete**](ProjectApi.md#project_project_id_tasks_task_id_delete) | **DELETE** /project/{project_id}/tasks/{task_id} | Deletes task (including output)
[**project_project_id_tasks_task_id_get**](ProjectApi.md#project_project_id_tasks_task_id_get) | **GET** /project/{project_id}/tasks/{task_id} | Get a single task
[**project_project_id_tasks_task_id_output_get**](ProjectApi.md#project_project_id_tasks_task_id_output_get) | **GET** /project/{project_id}/tasks/{task_id}/output | Get task output
[**project_project_id_tasks_task_id_stop_post**](ProjectApi.md#project_project_id_tasks_task_id_stop_post) | **POST** /project/{project_id}/tasks/{task_id}/stop | Stop a job
[**project_project_id_templates_get**](ProjectApi.md#project_project_id_templates_get) | **GET** /project/{project_id}/templates | Get template
[**project_project_id_templates_post**](ProjectApi.md#project_project_id_templates_post) | **POST** /project/{project_id}/templates | create template
[**project_project_id_templates_template_id_delete**](ProjectApi.md#project_project_id_templates_template_id_delete) | **DELETE** /project/{project_id}/templates/{template_id} | Removes template
[**project_project_id_templates_template_id_get**](ProjectApi.md#project_project_id_templates_template_id_get) | **GET** /project/{project_id}/templates/{template_id} | Get template
[**project_project_id_templates_template_id_put**](ProjectApi.md#project_project_id_templates_template_id_put) | **PUT** /project/{project_id}/templates/{template_id} | Updates template
[**project_project_id_users_get**](ProjectApi.md#project_project_id_users_get) | **GET** /project/{project_id}/users | Get users linked to project
[**project_project_id_users_post**](ProjectApi.md#project_project_id_users_post) | **POST** /project/{project_id}/users | Link user to project
[**project_project_id_users_user_id_delete**](ProjectApi.md#project_project_id_users_user_id_delete) | **DELETE** /project/{project_id}/users/{user_id} | Removes user from project
[**project_project_id_views_get**](ProjectApi.md#project_project_id_views_get) | **GET** /project/{project_id}/views | Get view
[**project_project_id_views_post**](ProjectApi.md#project_project_id_views_post) | **POST** /project/{project_id}/views | create view
[**project_project_id_views_view_id_delete**](ProjectApi.md#project_project_id_views_view_id_delete) | **DELETE** /project/{project_id}/views/{view_id} | Removes view
[**project_project_id_views_view_id_get**](ProjectApi.md#project_project_id_views_view_id_get) | **GET** /project/{project_id}/views/{view_id} | Get view
[**project_project_id_views_view_id_put**](ProjectApi.md#project_project_id_views_view_id_put) | **PUT** /project/{project_id}/views/{view_id} | Updates view


# **project_project_id_delete**
> project_project_id_delete(project_id)

Delete project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Delete project
        api_instance.project_project_id_delete(project_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Project deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_environment_environment_id_delete**
> project_project_id_environment_environment_id_delete(project_id, environment_id)

Removes environment

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    environment_id = 6 # int | environment ID

    try:
        # Removes environment
        api_instance.project_project_id_environment_environment_id_delete(project_id, environment_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_environment_environment_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **environment_id** | **int**| environment ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | environment removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_environment_environment_id_put**
> project_project_id_environment_environment_id_put(project_id, environment_id, environment)

Update environment

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.environment_request import EnvironmentRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    environment_id = 6 # int | environment ID
    environment = semaphore_api.EnvironmentRequest() # EnvironmentRequest | 

    try:
        # Update environment
        api_instance.project_project_id_environment_environment_id_put(project_id, environment_id, environment)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_environment_environment_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **environment_id** | **int**| environment ID | 
 **environment** | [**EnvironmentRequest**](EnvironmentRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Environment Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_environment_get**
> List[Environment] project_project_id_environment_get(project_id, sort, order)

Get environment

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.environment import Environment
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    sort = 'db-deploy' # str | sorting name
    order = 'desc' # str | ordering manner

    try:
        # Get environment
        api_response = api_instance.project_project_id_environment_get(project_id, sort, order)
        print("The response of ProjectApi->project_project_id_environment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_environment_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **sort** | **str**| sorting name | 
 **order** | **str**| ordering manner | 

### Return type

[**List[Environment]**](Environment.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | environment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_environment_post**
> project_project_id_environment_post(project_id, environment)

Add environment

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.environment_request import EnvironmentRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    environment = semaphore_api.EnvironmentRequest() # EnvironmentRequest | 

    try:
        # Add environment
        api_instance.project_project_id_environment_post(project_id, environment)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_environment_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **environment** | [**EnvironmentRequest**](EnvironmentRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Environment created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_events_get**
> List[Event] project_project_id_events_get(project_id)

Get Events related to this project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.event import Event
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Get Events related to this project
        api_response = api_instance.project_project_id_events_get(project_id)
        print("The response of ProjectApi->project_project_id_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_events_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

[**List[Event]**](Event.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of events in chronological order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_get**
> Project project_project_id_get(project_id)

Fetch project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project import Project
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Fetch project
        api_response = api_instance.project_project_id_get(project_id)
        print("The response of ProjectApi->project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

[**Project**](Project.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_inventory_get**
> List[Inventory] project_project_id_inventory_get(project_id, sort, order)

Get inventory

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.inventory import Inventory
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    sort = 'sort_example' # str | sorting name
    order = 'order_example' # str | ordering manner

    try:
        # Get inventory
        api_response = api_instance.project_project_id_inventory_get(project_id, sort, order)
        print("The response of ProjectApi->project_project_id_inventory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_inventory_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **sort** | **str**| sorting name | 
 **order** | **str**| ordering manner | 

### Return type

[**List[Inventory]**](Inventory.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inventory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_inventory_inventory_id_delete**
> project_project_id_inventory_inventory_id_delete(project_id, inventory_id)

Removes inventory

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    inventory_id = 5 # int | inventory ID

    try:
        # Removes inventory
        api_instance.project_project_id_inventory_inventory_id_delete(project_id, inventory_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_inventory_inventory_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **inventory_id** | **int**| inventory ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | inventory removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_inventory_inventory_id_put**
> project_project_id_inventory_inventory_id_put(project_id, inventory_id, inventory)

Updates inventory

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.inventory_request import InventoryRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    inventory_id = 5 # int | inventory ID
    inventory = semaphore_api.InventoryRequest() # InventoryRequest | 

    try:
        # Updates inventory
        api_instance.project_project_id_inventory_inventory_id_put(project_id, inventory_id, inventory)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_inventory_inventory_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **inventory_id** | **int**| inventory ID | 
 **inventory** | [**InventoryRequest**](InventoryRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Inventory updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_inventory_post**
> Inventory project_project_id_inventory_post(project_id, inventory)

create inventory

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.inventory import Inventory
from semaphore_api.models.inventory_request import InventoryRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    inventory = semaphore_api.InventoryRequest() # InventoryRequest | 

    try:
        # create inventory
        api_response = api_instance.project_project_id_inventory_post(project_id, inventory)
        print("The response of ProjectApi->project_project_id_inventory_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_inventory_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **inventory** | [**InventoryRequest**](InventoryRequest.md)|  | 

### Return type

[**Inventory**](Inventory.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | inventory created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_keys_get**
> List[AccessKey] project_project_id_keys_get(project_id, sort, order, key_type=key_type)

Get access keys linked to project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.access_key import AccessKey
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    sort = 'type' # str | sorting name
    order = 'asc' # str | ordering manner
    key_type = 'none' # str | Filter by key type (optional)

    try:
        # Get access keys linked to project
        api_response = api_instance.project_project_id_keys_get(project_id, sort, order, key_type=key_type)
        print("The response of ProjectApi->project_project_id_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_keys_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **sort** | **str**| sorting name | 
 **order** | **str**| ordering manner | 
 **key_type** | **str**| Filter by key type | [optional] 

### Return type

[**List[AccessKey]**](AccessKey.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access Keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_keys_key_id_delete**
> project_project_id_keys_key_id_delete(project_id, key_id)

Removes access key

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    key_id = 3 # int | key ID

    try:
        # Removes access key
        api_instance.project_project_id_keys_key_id_delete(project_id, key_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_keys_key_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **key_id** | **int**| key ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | access key removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_keys_key_id_put**
> project_project_id_keys_key_id_put(project_id, key_id, access_key)

Updates access key

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.access_key_request import AccessKeyRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    key_id = 3 # int | key ID
    access_key = semaphore_api.AccessKeyRequest() # AccessKeyRequest | 

    try:
        # Updates access key
        api_instance.project_project_id_keys_key_id_put(project_id, key_id, access_key)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_keys_key_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **key_id** | **int**| key ID | 
 **access_key** | [**AccessKeyRequest**](AccessKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Key updated |  -  |
**400** | Bad type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_keys_post**
> project_project_id_keys_post(project_id, access_key)

Add access key

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.access_key_request import AccessKeyRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    access_key = semaphore_api.AccessKeyRequest() # AccessKeyRequest | 

    try:
        # Add access key
        api_instance.project_project_id_keys_post(project_id, access_key)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_keys_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **access_key** | [**AccessKeyRequest**](AccessKeyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Access Key created |  -  |
**400** | Bad type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_put**
> project_project_id_put(project_id, project)

Update project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project_project_id_put_request import ProjectProjectIdPutRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    project = semaphore_api.ProjectProjectIdPutRequest() # ProjectProjectIdPutRequest | 

    try:
        # Update project
        api_instance.project_project_id_put(project_id, project)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **project** | [**ProjectProjectIdPutRequest**](ProjectProjectIdPutRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Project saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_repositories_get**
> List[Repository] project_project_id_repositories_get(project_id, sort, order)

Get repositories

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.repository import Repository
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    sort = 'sort_example' # str | sorting name
    order = 'order_example' # str | ordering manner

    try:
        # Get repositories
        api_response = api_instance.project_project_id_repositories_get(project_id, sort, order)
        print("The response of ProjectApi->project_project_id_repositories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_repositories_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **sort** | **str**| sorting name | 
 **order** | **str**| ordering manner | 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | repositories |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_repositories_post**
> project_project_id_repositories_post(project_id, repository)

Add repository

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.repository_request import RepositoryRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    repository = semaphore_api.RepositoryRequest() # RepositoryRequest | 

    try:
        # Add repository
        api_instance.project_project_id_repositories_post(project_id, repository)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_repositories_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **repository** | [**RepositoryRequest**](RepositoryRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Repository created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_repositories_repository_id_delete**
> project_project_id_repositories_repository_id_delete(project_id, repository_id)

Removes repository

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    repository_id = 4 # int | repository ID

    try:
        # Removes repository
        api_instance.project_project_id_repositories_repository_id_delete(project_id, repository_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_repositories_repository_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **repository_id** | **int**| repository ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | repository removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_repositories_repository_id_put**
> project_project_id_repositories_repository_id_put(project_id, repository_id, repository)

Updates repository

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.repository_request import RepositoryRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    repository_id = 4 # int | repository ID
    repository = semaphore_api.RepositoryRequest() # RepositoryRequest | 

    try:
        # Updates repository
        api_instance.project_project_id_repositories_repository_id_put(project_id, repository_id, repository)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_repositories_repository_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **repository_id** | **int**| repository ID | 
 **repository** | [**RepositoryRequest**](RepositoryRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Repository updated |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_role_get**
> ProjectProjectIdRoleGet200Response project_project_id_role_get(project_id)

Fetch permissions of the current user for project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project_project_id_role_get200_response import ProjectProjectIdRoleGet200Response
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Fetch permissions of the current user for project
        api_response = api_instance.project_project_id_role_get(project_id)
        print("The response of ProjectApi->project_project_id_role_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_role_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

[**ProjectProjectIdRoleGet200Response**](ProjectProjectIdRoleGet200Response.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_get**
> List[Task] project_project_id_tasks_get(project_id)

Get Tasks related to current project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.task import Task
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Get Tasks related to current project
        api_response = api_instance.project_project_id_tasks_get(project_id)
        print("The response of ProjectApi->project_project_id_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of tasks in chronological order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_last_get**
> List[Task] project_project_id_tasks_last_get(project_id)

Get last 200 Tasks related to current project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.task import Task
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Get last 200 Tasks related to current project
        api_response = api_instance.project_project_id_tasks_last_get(project_id)
        print("The response of ProjectApi->project_project_id_tasks_last_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_last_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of tasks in chronological order |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_post**
> Task project_project_id_tasks_post(project_id, task)

Starts a job

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project_project_id_tasks_post_request import ProjectProjectIdTasksPostRequest
from semaphore_api.models.task import Task
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    task = semaphore_api.ProjectProjectIdTasksPostRequest() # ProjectProjectIdTasksPostRequest | 

    try:
        # Starts a job
        api_response = api_instance.project_project_id_tasks_post(project_id, task)
        print("The response of ProjectApi->project_project_id_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **task** | [**ProjectProjectIdTasksPostRequest**](ProjectProjectIdTasksPostRequest.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task queued |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_task_id_delete**
> project_project_id_tasks_task_id_delete(project_id, task_id)

Deletes task (including output)

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    task_id = 8 # int | task ID

    try:
        # Deletes task (including output)
        api_instance.project_project_id_tasks_task_id_delete(project_id, task_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_task_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **task_id** | **int**| task ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | task deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_task_id_get**
> Task project_project_id_tasks_task_id_get(project_id, task_id)

Get a single task

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.task import Task
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    task_id = 8 # int | task ID

    try:
        # Get a single task
        api_response = api_instance.project_project_id_tasks_task_id_get(project_id, task_id)
        print("The response of ProjectApi->project_project_id_tasks_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_task_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **task_id** | **int**| task ID | 

### Return type

[**Task**](Task.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_task_id_output_get**
> List[TaskOutput] project_project_id_tasks_task_id_output_get(project_id, task_id)

Get task output

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.task_output import TaskOutput
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    task_id = 8 # int | task ID

    try:
        # Get task output
        api_response = api_instance.project_project_id_tasks_task_id_output_get(project_id, task_id)
        print("The response of ProjectApi->project_project_id_tasks_task_id_output_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_task_id_output_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **task_id** | **int**| task ID | 

### Return type

[**List[TaskOutput]**](TaskOutput.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | output |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_tasks_task_id_stop_post**
> project_project_id_tasks_task_id_stop_post(project_id, task_id)

Stop a job

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    task_id = 8 # int | task ID

    try:
        # Stop a job
        api_instance.project_project_id_tasks_task_id_stop_post(project_id, task_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_tasks_task_id_stop_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **task_id** | **int**| task ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Task queued |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_templates_get**
> List[Template] project_project_id_templates_get(project_id, sort, order)

Get template

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.template import Template
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    sort = 'sort_example' # str | sorting name
    order = 'order_example' # str | ordering manner

    try:
        # Get template
        api_response = api_instance.project_project_id_templates_get(project_id, sort, order)
        print("The response of ProjectApi->project_project_id_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_templates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **sort** | **str**| sorting name | 
 **order** | **str**| ordering manner | 

### Return type

[**List[Template]**](Template.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_templates_post**
> TemplateRequest project_project_id_templates_post(project_id, templateyes)

create template

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.template_request import TemplateRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    templateyes = semaphore_api.TemplateRequest() # TemplateRequest | 

    try:
        # create template
        api_response = api_instance.project_project_id_templates_post(project_id, templateyes)
        print("The response of ProjectApi->project_project_id_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_templates_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **templateyes** | [**TemplateRequest**](TemplateRequest.md)|  | 

### Return type

[**TemplateRequest**](TemplateRequest.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | template created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_templates_template_id_delete**
> project_project_id_templates_template_id_delete(project_id, template_id)

Removes template

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    template_id = 7 # int | template ID

    try:
        # Removes template
        api_instance.project_project_id_templates_template_id_delete(project_id, template_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_templates_template_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **template_id** | **int**| template ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | template removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_templates_template_id_get**
> Template project_project_id_templates_template_id_get(project_id, template_id)

Get template

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.template import Template
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    template_id = 7 # int | template ID

    try:
        # Get template
        api_response = api_instance.project_project_id_templates_template_id_get(project_id, template_id)
        print("The response of ProjectApi->project_project_id_templates_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_templates_template_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **template_id** | **int**| template ID | 

### Return type

[**Template**](Template.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | template object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_templates_template_id_put**
> project_project_id_templates_template_id_put(project_id, template_id, template)

Updates template

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.template_request import TemplateRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    template_id = 7 # int | template ID
    template = semaphore_api.TemplateRequest() # TemplateRequest | 

    try:
        # Updates template
        api_instance.project_project_id_templates_template_id_put(project_id, template_id, template)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_templates_template_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **template_id** | **int**| template ID | 
 **template** | [**TemplateRequest**](TemplateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | template updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_users_get**
> List[ProjectUser] project_project_id_users_get(project_id, sort, order)

Get users linked to project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project_user import ProjectUser
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    sort = 'email' # str | sorting name
    order = 'desc' # str | ordering manner

    try:
        # Get users linked to project
        api_response = api_instance.project_project_id_users_get(project_id, sort, order)
        print("The response of ProjectApi->project_project_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_users_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **sort** | **str**| sorting name | 
 **order** | **str**| ordering manner | 

### Return type

[**List[ProjectUser]**](ProjectUser.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_users_post**
> project_project_id_users_post(project_id, user)

Link user to project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project_project_id_users_post_request import ProjectProjectIdUsersPostRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    user = semaphore_api.ProjectProjectIdUsersPostRequest() # ProjectProjectIdUsersPostRequest | 

    try:
        # Link user to project
        api_instance.project_project_id_users_post(project_id, user)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_users_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **user** | [**ProjectProjectIdUsersPostRequest**](ProjectProjectIdUsersPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_users_user_id_delete**
> project_project_id_users_user_id_delete(project_id, user_id)

Removes user from project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    user_id = 2 # int | User ID

    try:
        # Removes user from project
        api_instance.project_project_id_users_user_id_delete(project_id, user_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_users_user_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **user_id** | **int**| User ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_views_get**
> List[View] project_project_id_views_get(project_id)

Get view

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.view import View
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID

    try:
        # Get view
        api_response = api_instance.project_project_id_views_get(project_id)
        print("The response of ProjectApi->project_project_id_views_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_views_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 

### Return type

[**List[View]**](View.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | view |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_views_post**
> View project_project_id_views_post(project_id, view)

create view

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.view import View
from semaphore_api.models.view_request import ViewRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    view = semaphore_api.ViewRequest() # ViewRequest | 

    try:
        # create view
        api_response = api_instance.project_project_id_views_post(project_id, view)
        print("The response of ProjectApi->project_project_id_views_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_views_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **view** | [**ViewRequest**](ViewRequest.md)|  | 

### Return type

[**View**](View.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | view created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_views_view_id_delete**
> project_project_id_views_view_id_delete(project_id, view_id)

Removes view

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    view_id = 10 # int | view ID

    try:
        # Removes view
        api_instance.project_project_id_views_view_id_delete(project_id, view_id)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_views_view_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **view_id** | **int**| view ID | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | view removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_views_view_id_get**
> View project_project_id_views_view_id_get(project_id, view_id)

Get view

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.view import View
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    view_id = 10 # int | view ID

    try:
        # Get view
        api_response = api_instance.project_project_id_views_view_id_get(project_id, view_id)
        print("The response of ProjectApi->project_project_id_views_view_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_views_view_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **view_id** | **int**| view ID | 

### Return type

[**View**](View.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | view object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_views_view_id_put**
> project_project_id_views_view_id_put(project_id, view_id, view)

Updates view

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.view_request import ViewRequest
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: bearer
configuration.api_key['bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.ProjectApi(api_client)
    project_id = 1 # int | Project ID
    view_id = 10 # int | view ID
    view = semaphore_api.ViewRequest() # ViewRequest | 

    try:
        # Updates view
        api_instance.project_project_id_views_view_id_put(project_id, view_id, view)
    except Exception as e:
        print("Exception when calling ProjectApi->project_project_id_views_view_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **view_id** | **int**| view ID | 
 **view** | [**ViewRequest**](ViewRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | view updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

