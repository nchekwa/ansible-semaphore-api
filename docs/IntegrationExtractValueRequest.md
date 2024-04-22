# IntegrationExtractValueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value_source** | **str** |  | [optional] 
**body_data_type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**variable** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.integration_extract_value_request import IntegrationExtractValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationExtractValueRequest from a JSON string
integration_extract_value_request_instance = IntegrationExtractValueRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrationExtractValueRequest.to_json())

# convert the object into a dict
integration_extract_value_request_dict = integration_extract_value_request_instance.to_dict()
# create an instance of IntegrationExtractValueRequest from a dict
integration_extract_value_request_from_dict = IntegrationExtractValueRequest.from_dict(integration_extract_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


