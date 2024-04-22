# ProjectBackupTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**view** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**playbook** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**allow_override_args_in_task** | **bool** |  | [optional] 
**suppress_success_alerts** | **bool** |  | [optional] 
**autorun** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup_templates_inner import ProjectBackupTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackupTemplatesInner from a JSON string
project_backup_templates_inner_instance = ProjectBackupTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(ProjectBackupTemplatesInner.to_json())

# convert the object into a dict
project_backup_templates_inner_dict = project_backup_templates_inner_instance.to_dict()
# create an instance of ProjectBackupTemplatesInner from a dict
project_backup_templates_inner_from_dict = ProjectBackupTemplatesInner.from_dict(project_backup_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


