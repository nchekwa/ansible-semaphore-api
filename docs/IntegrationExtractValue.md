# IntegrationExtractValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**value_source** | **str** |  | [optional] 
**body_data_type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**variable** | **str** |  | [optional] 
**integration_id** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.integration_extract_value import IntegrationExtractValue

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationExtractValue from a JSON string
integration_extract_value_instance = IntegrationExtractValue.from_json(json)
# print the JSON string representation of the object
print(IntegrationExtractValue.to_json())

# convert the object into a dict
integration_extract_value_dict = integration_extract_value_instance.to_dict()
# create an instance of IntegrationExtractValue from a dict
integration_extract_value_from_dict = IntegrationExtractValue.from_dict(integration_extract_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


