# semaphore_api.IntegrationApi

All URIs are relative to *http://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**project_project_id_integrations_integration_id_matchers_get**](IntegrationApi.md#project_project_id_integrations_integration_id_matchers_get) | **GET** /project/{project_id}/integrations/{integration_id}/matchers | Get Integration Matcher linked to integration extractor
[**project_project_id_integrations_integration_id_matchers_matcher_id_delete**](IntegrationApi.md#project_project_id_integrations_integration_id_matchers_matcher_id_delete) | **DELETE** /project/{project_id}/integrations/{integration_id}/matchers/{matcher_id} | Removes integration matcher
[**project_project_id_integrations_integration_id_matchers_matcher_id_put**](IntegrationApi.md#project_project_id_integrations_integration_id_matchers_matcher_id_put) | **PUT** /project/{project_id}/integrations/{integration_id}/matchers/{matcher_id} | Updates Integration Matcher
[**project_project_id_integrations_integration_id_values_extractvalue_id_delete**](IntegrationApi.md#project_project_id_integrations_integration_id_values_extractvalue_id_delete) | **DELETE** /project/{project_id}/integrations/{integration_id}/values/{extractvalue_id} | Removes integration extract value
[**project_project_id_integrations_integration_id_values_extractvalue_id_put**](IntegrationApi.md#project_project_id_integrations_integration_id_values_extractvalue_id_put) | **PUT** /project/{project_id}/integrations/{integration_id}/values/{extractvalue_id} | Updates Integration ExtractValue
[**project_project_id_integrations_integration_id_values_get**](IntegrationApi.md#project_project_id_integrations_integration_id_values_get) | **GET** /project/{project_id}/integrations/{integration_id}/values | Get Integration Extracted Values linked to integration extractor


# **project_project_id_integrations_integration_id_matchers_get**
> List[IntegrationMatcher] project_project_id_integrations_integration_id_matchers_get(project_id, integration_id)

Get Integration Matcher linked to integration extractor

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.integration_matcher import IntegrationMatcher
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
    api_instance = semaphore_api.IntegrationApi(api_client)
    project_id = 1 # int | Project ID
    integration_id = 11 # int | integration ID

    try:
        # Get Integration Matcher linked to integration extractor
        api_response = api_instance.project_project_id_integrations_integration_id_matchers_get(project_id, integration_id)
        print("The response of IntegrationApi->project_project_id_integrations_integration_id_matchers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->project_project_id_integrations_integration_id_matchers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **integration_id** | **int**| integration ID | 

### Return type

[**List[IntegrationMatcher]**](IntegrationMatcher.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration Matcher |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_integrations_integration_id_matchers_matcher_id_delete**
> project_project_id_integrations_integration_id_matchers_matcher_id_delete(project_id, integration_id, matcher_id)

Removes integration matcher

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
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
    api_instance = semaphore_api.IntegrationApi(api_client)
    project_id = 1 # int | Project ID
    integration_id = 11 # int | integration ID
    matcher_id = 13 # int | matcher ID

    try:
        # Removes integration matcher
        api_instance.project_project_id_integrations_integration_id_matchers_matcher_id_delete(project_id, integration_id, matcher_id)
    except Exception as e:
        print("Exception when calling IntegrationApi->project_project_id_integrations_integration_id_matchers_matcher_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **integration_id** | **int**| integration ID | 
 **matcher_id** | **int**| matcher ID | 

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
**204** | integration matcher removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_integrations_integration_id_matchers_matcher_id_put**
> project_project_id_integrations_integration_id_matchers_matcher_id_put(project_id, integration_id, matcher_id, integration_matcher)

Updates Integration Matcher

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.integration_matcher_request import IntegrationMatcherRequest
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
    api_instance = semaphore_api.IntegrationApi(api_client)
    project_id = 1 # int | Project ID
    integration_id = 11 # int | integration ID
    matcher_id = 13 # int | matcher ID
    integration_matcher = semaphore_api.IntegrationMatcherRequest() # IntegrationMatcherRequest | 

    try:
        # Updates Integration Matcher
        api_instance.project_project_id_integrations_integration_id_matchers_matcher_id_put(project_id, integration_id, matcher_id, integration_matcher)
    except Exception as e:
        print("Exception when calling IntegrationApi->project_project_id_integrations_integration_id_matchers_matcher_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **integration_id** | **int**| integration ID | 
 **matcher_id** | **int**| matcher ID | 
 **integration_matcher** | [**IntegrationMatcherRequest**](IntegrationMatcherRequest.md)|  | 

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
**204** | Integration Matcher updated |  -  |
**400** | Bad integration matcher parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_integrations_integration_id_values_extractvalue_id_delete**
> project_project_id_integrations_integration_id_values_extractvalue_id_delete(project_id, integration_id, extractvalue_id)

Removes integration extract value

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
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
    api_instance = semaphore_api.IntegrationApi(api_client)
    project_id = 1 # int | Project ID
    integration_id = 11 # int | integration ID
    extractvalue_id = 12 # int | extractValue ID

    try:
        # Removes integration extract value
        api_instance.project_project_id_integrations_integration_id_values_extractvalue_id_delete(project_id, integration_id, extractvalue_id)
    except Exception as e:
        print("Exception when calling IntegrationApi->project_project_id_integrations_integration_id_values_extractvalue_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **integration_id** | **int**| integration ID | 
 **extractvalue_id** | **int**| extractValue ID | 

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
**204** | integration extract value removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_integrations_integration_id_values_extractvalue_id_put**
> project_project_id_integrations_integration_id_values_extractvalue_id_put(project_id, integration_id, extractvalue_id, integration_extract_value)

Updates Integration ExtractValue

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.integration_extract_value_request import IntegrationExtractValueRequest
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
    api_instance = semaphore_api.IntegrationApi(api_client)
    project_id = 1 # int | Project ID
    integration_id = 11 # int | integration ID
    extractvalue_id = 12 # int | extractValue ID
    integration_extract_value = semaphore_api.IntegrationExtractValueRequest() # IntegrationExtractValueRequest | 

    try:
        # Updates Integration ExtractValue
        api_instance.project_project_id_integrations_integration_id_values_extractvalue_id_put(project_id, integration_id, extractvalue_id, integration_extract_value)
    except Exception as e:
        print("Exception when calling IntegrationApi->project_project_id_integrations_integration_id_values_extractvalue_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **integration_id** | **int**| integration ID | 
 **extractvalue_id** | **int**| extractValue ID | 
 **integration_extract_value** | [**IntegrationExtractValueRequest**](IntegrationExtractValueRequest.md)|  | 

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
**204** | Integration Extract Value updated |  -  |
**400** | Bad integration extract value parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_project_id_integrations_integration_id_values_get**
> List[IntegrationExtractValue] project_project_id_integrations_integration_id_values_get(project_id, integration_id)

Get Integration Extracted Values linked to integration extractor

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.integration_extract_value import IntegrationExtractValue
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
    api_instance = semaphore_api.IntegrationApi(api_client)
    project_id = 1 # int | Project ID
    integration_id = 11 # int | integration ID

    try:
        # Get Integration Extracted Values linked to integration extractor
        api_response = api_instance.project_project_id_integrations_integration_id_values_get(project_id, integration_id)
        print("The response of IntegrationApi->project_project_id_integrations_integration_id_values_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationApi->project_project_id_integrations_integration_id_values_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID | 
 **integration_id** | **int**| integration ID | 

### Return type

[**List[IntegrationExtractValue]**](IntegrationExtractValue.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Integration Extracted Value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

