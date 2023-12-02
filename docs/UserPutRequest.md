# UserPutRequest


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
from semaphore_api.models.user_put_request import UserPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserPutRequest from a JSON string
user_put_request_instance = UserPutRequest.from_json(json)
# print the JSON string representation of the object
print UserPutRequest.to_json()

# convert the object into a dict
user_put_request_dict = user_put_request_instance.to_dict()
# create an instance of UserPutRequest from a dict
user_put_request_form_dict = user_put_request.from_dict(user_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


