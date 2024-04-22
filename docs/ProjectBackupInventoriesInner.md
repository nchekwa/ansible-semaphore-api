# ProjectBackupInventoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**inventory** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup_inventories_inner import ProjectBackupInventoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackupInventoriesInner from a JSON string
project_backup_inventories_inner_instance = ProjectBackupInventoriesInner.from_json(json)
# print the JSON string representation of the object
print(ProjectBackupInventoriesInner.to_json())

# convert the object into a dict
project_backup_inventories_inner_dict = project_backup_inventories_inner_instance.to_dict()
# create an instance of ProjectBackupInventoriesInner from a dict
project_backup_inventories_inner_from_dict = ProjectBackupInventoriesInner.from_dict(project_backup_inventories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


