# AccessKeyRequestLoginPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**login** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.access_key_request_login_password import AccessKeyRequestLoginPassword

# TODO update the JSON string below
json = "{}"
# create an instance of AccessKeyRequestLoginPassword from a JSON string
access_key_request_login_password_instance = AccessKeyRequestLoginPassword.from_json(json)
# print the JSON string representation of the object
print(AccessKeyRequestLoginPassword.to_json())

# convert the object into a dict
access_key_request_login_password_dict = access_key_request_login_password_instance.to_dict()
# create an instance of AccessKeyRequestLoginPassword from a dict
access_key_request_login_password_from_dict = AccessKeyRequestLoginPassword.from_dict(access_key_request_login_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


