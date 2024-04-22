# IntegrationMatcher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**integration_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**body_data_type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.integration_matcher import IntegrationMatcher

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationMatcher from a JSON string
integration_matcher_instance = IntegrationMatcher.from_json(json)
# print the JSON string representation of the object
print(IntegrationMatcher.to_json())

# convert the object into a dict
integration_matcher_dict = integration_matcher_instance.to_dict()
# create an instance of IntegrationMatcher from a dict
integration_matcher_from_dict = IntegrationMatcher.from_dict(integration_matcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


