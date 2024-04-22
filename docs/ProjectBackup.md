# ProjectBackup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ProjectBackupMeta**](ProjectBackupMeta.md) |  | [optional] 
**templates** | [**List[ProjectBackupTemplatesInner]**](ProjectBackupTemplatesInner.md) |  | [optional] 
**repositories** | [**List[ProjectBackupRepositoriesInner]**](ProjectBackupRepositoriesInner.md) |  | [optional] 
**keys** | [**List[ProjectBackupKeysInner]**](ProjectBackupKeysInner.md) |  | [optional] 
**views** | [**List[ProjectBackupViewsInner]**](ProjectBackupViewsInner.md) |  | [optional] 
**inventories** | [**List[ProjectBackupInventoriesInner]**](ProjectBackupInventoriesInner.md) |  | [optional] 
**environments** | [**List[ProjectBackupEnvironmentsInner]**](ProjectBackupEnvironmentsInner.md) |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup import ProjectBackup

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackup from a JSON string
project_backup_instance = ProjectBackup.from_json(json)
# print the JSON string representation of the object
print(ProjectBackup.to_json())

# convert the object into a dict
project_backup_dict = project_backup_instance.to_dict()
# create an instance of ProjectBackup from a dict
project_backup_from_dict = ProjectBackup.from_dict(project_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


