# semaphore_api.UserApi

All URIs are relative to *http://localhost:3000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get**](UserApi.md#user_get) | **GET** /user/ | Fetch logged in user
[**user_tokens_api_token_id_delete**](UserApi.md#user_tokens_api_token_id_delete) | **DELETE** /user/tokens/{api_token_id} | Expires API token
[**user_tokens_get**](UserApi.md#user_tokens_get) | **GET** /user/tokens | Fetch API tokens for user
[**user_tokens_post**](UserApi.md#user_tokens_post) | **POST** /user/tokens | Create an API token
[**users_get**](UserApi.md#users_get) | **GET** /users | Fetches all users
[**users_post**](UserApi.md#users_post) | **POST** /users | Creates a user
[**users_user_id_delete**](UserApi.md#users_user_id_delete) | **DELETE** /users/{user_id}/ | Deletes user
[**users_user_id_get**](UserApi.md#users_user_id_get) | **GET** /users/{user_id}/ | Fetches a user profile
[**users_user_id_password_post**](UserApi.md#users_user_id_password_post) | **POST** /users/{user_id}/password | Updates user password
[**users_user_id_put**](UserApi.md#users_user_id_put) | **PUT** /users/{user_id}/ | Updates user details


# **user_get**
> User user_get()

Fetch logged in user

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.user import User
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
    api_instance = semaphore_api.UserApi(api_client)

    try:
        # Fetch logged in user
        api_response = api_instance.user_get()
        print("The response of UserApi->user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |

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
    api_instance = semaphore_api.UserApi(api_client)
    api_token_id = 'kwofd61g93-yuqvex8efmhjkgnbxlo8mp1tin6spyhu=' # str | 

    try:
        # Expires API token
        api_instance.user_tokens_api_token_id_delete(api_token_id)
    except Exception as e:
        print("Exception when calling UserApi->user_tokens_api_token_id_delete: %s\n" % e)
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
    api_instance = semaphore_api.UserApi(api_client)

    try:
        # Fetch API tokens for user
        api_response = api_instance.user_tokens_get()
        print("The response of UserApi->user_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_tokens_get: %s\n" % e)
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
    api_instance = semaphore_api.UserApi(api_client)

    try:
        # Create an API token
        api_response = api_instance.user_tokens_post()
        print("The response of UserApi->user_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_tokens_post: %s\n" % e)
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

# **users_get**
> List[User] users_get()

Fetches all users

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.user import User
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
    api_instance = semaphore_api.UserApi(api_client)

    try:
        # Fetches all users
        api_response = api_instance.users_get()
        print("The response of UserApi->users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

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

# **users_post**
> User users_post(user)

Creates a user

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.user import User
from semaphore_api.models.user_request import UserRequest
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
    api_instance = semaphore_api.UserApi(api_client)
    user = semaphore_api.UserRequest() # UserRequest | 

    try:
        # Creates a user
        api_response = api_instance.users_post(user)
        print("The response of UserApi->users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserRequest**](UserRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | User creation failed |  -  |
**201** | User created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Deletes user

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
    api_instance = semaphore_api.UserApi(api_client)
    user_id = 2 # int | User ID

    try:
        # Deletes user
        api_instance.users_user_id_delete(user_id)
    except Exception as e:
        print("Exception when calling UserApi->users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | User deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Fetches a user profile

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.user import User
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
    api_instance = semaphore_api.UserApi(api_client)
    user_id = 2 # int | User ID

    try:
        # Fetches a user profile
        api_response = api_instance.users_user_id_get(user_id)
        print("The response of UserApi->users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID | 

### Return type

[**User**](User.md)

### Authorization

[cookie](../README.md#cookie), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_post**
> users_user_id_password_post(user_id, password)

Updates user password

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.users_user_id_password_post_request import UsersUserIdPasswordPostRequest
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
    api_instance = semaphore_api.UserApi(api_client)
    user_id = 2 # int | User ID
    password = semaphore_api.UsersUserIdPasswordPostRequest() # UsersUserIdPasswordPostRequest | 

    try:
        # Updates user password
        api_instance.users_user_id_password_post(user_id, password)
    except Exception as e:
        print("Exception when calling UserApi->users_user_id_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID | 
 **password** | [**UsersUserIdPasswordPostRequest**](UsersUserIdPasswordPostRequest.md)|  | 

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
**204** | Password updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_put**
> users_user_id_put(user_id, user)

Updates user details

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (bearer):

```python
import semaphore_api
from semaphore_api.models.user_put_request import UserPutRequest
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
    api_instance = semaphore_api.UserApi(api_client)
    user_id = 2 # int | User ID
    user = semaphore_api.UserPutRequest() # UserPutRequest | 

    try:
        # Updates user details
        api_instance.users_user_id_put(user_id, user)
    except Exception as e:
        print("Exception when calling UserApi->users_user_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID | 
 **user** | [**UserPutRequest**](UserPutRequest.md)|  | 

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
**204** | User Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

