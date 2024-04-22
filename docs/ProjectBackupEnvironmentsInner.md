# ProjectBackupEnvironmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**var_json** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup_environments_inner import ProjectBackupEnvironmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackupEnvironmentsInner from a JSON string
project_backup_environments_inner_instance = ProjectBackupEnvironmentsInner.from_json(json)
# print the JSON string representation of the object
print(ProjectBackupEnvironmentsInner.to_json())

# convert the object into a dict
project_backup_environments_inner_dict = project_backup_environments_inner_instance.to_dict()
# create an instance of ProjectBackupEnvironmentsInner from a dict
project_backup_environments_inner_from_dict = ProjectBackupEnvironmentsInner.from_dict(project_backup_environments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


