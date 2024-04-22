# EnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**var_json** | **str** |  | [optional] 
**env** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.environment_request import EnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentRequest from a JSON string
environment_request_instance = EnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentRequest.to_json())

# convert the object into a dict
environment_request_dict = environment_request_instance.to_dict()
# create an instance of EnvironmentRequest from a dict
environment_request_from_dict = EnvironmentRequest.from_dict(environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


