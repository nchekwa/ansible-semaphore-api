# ProjectBackupKeysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup_keys_inner import ProjectBackupKeysInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackupKeysInner from a JSON string
project_backup_keys_inner_instance = ProjectBackupKeysInner.from_json(json)
# print the JSON string representation of the object
print(ProjectBackupKeysInner.to_json())

# convert the object into a dict
project_backup_keys_inner_dict = project_backup_keys_inner_instance.to_dict()
# create an instance of ProjectBackupKeysInner from a dict
project_backup_keys_inner_from_dict = ProjectBackupKeysInner.from_dict(project_backup_keys_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


