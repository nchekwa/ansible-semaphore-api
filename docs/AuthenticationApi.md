# semaphore_api.AuthenticationApi

All URIs are relative to *http://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_get**](AuthenticationApi.md#auth_login_get) | **GET** /auth/login | Fetches login metadata
[**auth_login_post**](AuthenticationApi.md#auth_login_post) | **POST** /auth/login | Performs Login
[**auth_logout_post**](AuthenticationApi.md#auth_logout_post) | **POST** /auth/logout | Destroys current session
[**auth_oidc_provider_id_login_get**](AuthenticationApi.md#auth_oidc_provider_id_login_get) | **GET** /auth/oidc/{provider_id}/login | Begin OIDC authentication flow and redirect to OIDC provider
[**auth_oidc_provider_id_redirect_get**](AuthenticationApi.md#auth_oidc_provider_id_redirect_get) | **GET** /auth/oidc/{provider_id}/redirect | Finish OIDC authentication flow, upon succes you will be logged in
[**user_tokens_api_token_id_delete**](AuthenticationApi.md#user_tokens_api_token_id_delete) | **DELETE** /user/tokens/{api_token_id} | Expires API token
[**user_tokens_get**](AuthenticationApi.md#user_tokens_get) | **GET** /user/tokens | Fetch API tokens for user
[**user_tokens_post**](AuthenticationApi.md#user_tokens_post) | **POST** /user/tokens | Create an API token


# **auth_login_get**
> LoginMetadata auth_login_get()

Fetches login metadata

Fetches metadata for login, such as available OIDC providers

### Example


```python
import semaphore_api
from semaphore_api.models.login_metadata import LoginMetadata
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)


# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.AuthenticationApi(api_client)

    try:
        # Fetches login metadata
        api_response = api_instance.auth_login_get()
        print("The response of AuthenticationApi->auth_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_login_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginMetadata**](LoginMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_post**
> auth_login_post(login_body)

Performs Login

Upon success you will be logged in

### Example


```python
import semaphore_api
from semaphore_api.models.login import Login
from semaphore_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = semaphore_api.Configuration(
    host = "http://localhost:3000/api"
)


# Enter a context with an instance of the API client
with semaphore_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = semaphore_api.AuthenticationApi(api_client)
    login_body = semaphore_api.Login() # Login | 

    try:
        # Performs Login
        api_instance.auth_login_post(login_body)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_body** | [**Login**](Login.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | You are logged in |  -  |
**400** | something in body is missing / is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout_post**
> auth_logout_post()

Destroys current session

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
    api_instance = semaphore_api.AuthenticationApi(api_client)

    try:
        # Destroys current session
        api_instance.auth_logout_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Your session was successfully nuked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_oidc_provider_id_login_get**
> auth_oidc_provider_id_login_get(provider_id)

Begin OIDC authentication flow and redirect to OIDC provider

The user agent is redirected to this endpoint when chosing to sign in via OIDC

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
    api_instance = semaphore_api.AuthenticationApi(api_client)
    provider_id = 'mysso' # str | 

    try:
        # Begin OIDC authentication flow and redirect to OIDC provider
        api_instance.auth_oidc_provider_id_login_get(provider_id)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_oidc_provider_id_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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
**302** | Redirection to the OIDC provider on success, or to the login page on error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_oidc_provider_id_redirect_get**
> auth_oidc_provider_id_redirect_get(provider_id)

Finish OIDC authentication flow, upon succes you will be logged in

The user agent is redirected here by the OIDC provider to complete authentication

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
    api_instance = semaphore_api.AuthenticationApi(api_client)
    provider_id = 'mysso' # str | 

    try:
        # Finish OIDC authentication flow, upon succes you will be logged in
        api_instance.auth_oidc_provider_id_redirect_get(provider_id)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_oidc_provider_id_redirect_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

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
**302** | Redirection to the Semaphore root URL on success, or to the login page on error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tokens_api_token_id_delete**
> user_tokens_api_token_id_delete(api_token_id)

Expires API token

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
    api_instance = semaphore_api.AuthenticationApi(api_client)
    api_token_id = 'kwofd61g93-yuqvex8efmhjkgnbxlo8mp1tin6spyhu=' # str | 

    try:
        # Expires API token
        api_instance.user_tokens_api_token_id_delete(api_token_id)
    except Exception as e:
        print("Exception when calling AuthenticationApi->user_tokens_api_token_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_id** | **str**|  | 

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
**204** | Expired API Token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tokens_get**
> List[APIToken] user_tokens_get()

Fetch API tokens for user

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.api_token import APIToken
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
    api_instance = semaphore_api.AuthenticationApi(api_client)

    try:
        # Fetch API tokens for user
        api_response = api_instance.user_tokens_get()
        print("The response of AuthenticationApi->user_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->user_tokens_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIToken]**](APIToken.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API Tokens |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tokens_post**
> APIToken user_tokens_post()

Create an API token

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.api_token import APIToken
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
    api_instance = semaphore_api.AuthenticationApi(api_client)

    try:
        # Create an API token
        api_response = api_instance.user_tokens_post()
        print("The response of AuthenticationApi->user_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->user_tokens_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIToken**](APIToken.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | API Token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

