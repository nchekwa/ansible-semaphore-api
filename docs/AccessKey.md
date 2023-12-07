# AccessKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**login_password** | [**AccessKeyRequestLoginPassword**](AccessKeyRequestLoginPassword.md) |  | [optional] 
**ssh** | [**AccessKeyRequestSsh**](AccessKeyRequestSsh.md) |  | [optional] 

## Example

```python
from semaphore_api.models.access_key import AccessKey

# TODO update the JSON string below
json = "{}"
# create an instance of AccessKey from a JSON string
access_key_instance = AccessKey.from_json(json)
# print the JSON string representation of the object
print AccessKey.to_json()

# convert the object into a dict
access_key_dict = access_key_instance.to_dict()
# create an instance of AccessKey from a dict
access_key_form_dict = access_key.from_dict(access_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


