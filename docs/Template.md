# Template


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**inventory_id** | **int** |  | [optional] 
**repository_id** | **int** |  | [optional] 
**environment_id** | **int** |  | [optional] 
**view_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**playbook** | **str** |  | [optional] 
**arguments** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**allow_override_args_in_task** | **bool** |  | [optional] 
**suppress_success_alerts** | **bool** |  | [optional] 
**app** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


