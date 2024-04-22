# RepositoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**git_url** | **str** |  | [optional] 
**git_branch** | **str** |  | [optional] 
**ssh_key_id** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.repository_request import RepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRequest from a JSON string
repository_request_instance = RepositoryRequest.from_json(json)
# print the JSON string representation of the object
print(RepositoryRequest.to_json())

# convert the object into a dict
repository_request_dict = repository_request_instance.to_dict()
# create an instance of RepositoryRequest from a dict
repository_request_from_dict = RepositoryRequest.from_dict(repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


