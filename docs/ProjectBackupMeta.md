# ProjectBackupMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**alert** | **bool** |  | [optional] 
**max_parallel_tasks** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup_meta import ProjectBackupMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackupMeta from a JSON string
project_backup_meta_instance = ProjectBackupMeta.from_json(json)
# print the JSON string representation of the object
print(ProjectBackupMeta.to_json())

# convert the object into a dict
project_backup_meta_dict = project_backup_meta_instance.to_dict()
# create an instance of ProjectBackupMeta from a dict
project_backup_meta_from_dict = ProjectBackupMeta.from_dict(project_backup_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


