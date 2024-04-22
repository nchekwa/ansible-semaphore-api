# IntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**template_id** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.integration_request import IntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationRequest from a JSON string
integration_request_instance = IntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrationRequest.to_json())

# convert the object into a dict
integration_request_dict = integration_request_instance.to_dict()
# create an instance of IntegrationRequest from a dict
integration_request_from_dict = IntegrationRequest.from_dict(integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


