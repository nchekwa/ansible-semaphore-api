# ProjectBackupRepositoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**git_url** | **str** |  | [optional] 
**git_branch** | **str** |  | [optional] 
**ssh_key** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_backup_repositories_inner import ProjectBackupRepositoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBackupRepositoriesInner from a JSON string
project_backup_repositories_inner_instance = ProjectBackupRepositoriesInner.from_json(json)
# print the JSON string representation of the object
print(ProjectBackupRepositoriesInner.to_json())

# convert the object into a dict
project_backup_repositories_inner_dict = project_backup_repositories_inner_instance.to_dict()
# create an instance of ProjectBackupRepositoriesInner from a dict
project_backup_repositories_inner_from_dict = ProjectBackupRepositoriesInner.from_dict(project_backup_repositories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


