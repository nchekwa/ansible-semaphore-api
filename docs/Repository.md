# Repository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**git_url** | **str** |  | [optional] 
**git_branch** | **str** |  | [optional] 
**ssh_key_id** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print Repository.to_json()

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_form_dict = repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


