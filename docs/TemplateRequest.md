# TemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**inventory_id** | **int** |  | [optional] 
**repository_id** | **int** |  | [optional] 
**environment_id** | **int** |  | [optional] 
**view_id** | **int** |  | [optional] 
**vault_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**playbook** | **str** |  | [optional] 
**arguments** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**allow_override_args_in_task** | **bool** |  | [optional] 
**limit** | **str** |  | [optional] 
**suppress_success_alerts** | **bool** |  | [optional] 
**survey_vars** | [**List[TemplateSurveyVar]**](TemplateSurveyVar.md) |  | [optional] 

## Example

```python
from semaphore_api.models.template_request import TemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRequest from a JSON string
template_request_instance = TemplateRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateRequest.to_json())

# convert the object into a dict
template_request_dict = template_request_instance.to_dict()
# create an instance of TemplateRequest from a dict
template_request_from_dict = TemplateRequest.from_dict(template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


