# semaphore_api.ProjectsApi

All URIs are relative to *http://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | Get projects
[**projects_post**](ProjectsApi.md#projects_post) | **POST** /projects | Create a new project


# **projects_get**
> List[Project] projects_get()

Get projects

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
    api_instance = semaphore_api.ProjectsApi(api_client)

    try:
        # Get projects
        api_response = api_instance.projects_get()
        print("The response of ProjectsApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> projects_post(project)

Create a new project

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):
```python
import time
import os
import semaphore_api
from semaphore_api.models.project_request import ProjectRequest
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
    api_instance = semaphore_api.ProjectsApi(api_client)
    project = semaphore_api.ProjectRequest() # ProjectRequest | 

    try:
        # Create a new project
        api_instance.projects_post(project)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectRequest**](ProjectRequest.md)|  | 

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
**201** | Created project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

