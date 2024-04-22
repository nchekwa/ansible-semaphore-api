# ViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.view_request import ViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ViewRequest from a JSON string
view_request_instance = ViewRequest.from_json(json)
# print the JSON string representation of the object
print(ViewRequest.to_json())

# convert the object into a dict
view_request_dict = view_request_instance.to_dict()
# create an instance of ViewRequest from a dict
view_request_from_dict = ViewRequest.from_dict(view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


