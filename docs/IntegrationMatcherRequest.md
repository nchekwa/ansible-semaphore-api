# IntegrationMatcherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**body_data_type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.integration_matcher_request import IntegrationMatcherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationMatcherRequest from a JSON string
integration_matcher_request_instance = IntegrationMatcherRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrationMatcherRequest.to_json())

# convert the object into a dict
integration_matcher_request_dict = integration_matcher_request_instance.to_dict()
# create an instance of IntegrationMatcherRequest from a dict
integration_matcher_request_from_dict = IntegrationMatcherRequest.from_dict(integration_matcher_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


