# UserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**alert** | **bool** |  | [optional] 
**admin** | **bool** |  | [optional] 

## Example

```python
from semaphore_api.models.user_request import UserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequest from a JSON string
user_request_instance = UserRequest.from_json(json)
# print the JSON string representation of the object
print UserRequest.to_json()

# convert the object into a dict
user_request_dict = user_request_instance.to_dict()
# create an instance of UserRequest from a dict
user_request_form_dict = user_request.from_dict(user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


