# AccessKeyRequestSsh


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.access_key_request_ssh import AccessKeyRequestSsh

# TODO update the JSON string below
json = "{}"
# create an instance of AccessKeyRequestSsh from a JSON string
access_key_request_ssh_instance = AccessKeyRequestSsh.from_json(json)
# print the JSON string representation of the object
print AccessKeyRequestSsh.to_json()

# convert the object into a dict
access_key_request_ssh_dict = access_key_request_ssh_instance.to_dict()
# create an instance of AccessKeyRequestSsh from a dict
access_key_request_ssh_form_dict = access_key_request_ssh.from_dict(access_key_request_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


