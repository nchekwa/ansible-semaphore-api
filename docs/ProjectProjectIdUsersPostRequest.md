# ProjectProjectIdUsersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_project_id_users_post_request import ProjectProjectIdUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectProjectIdUsersPostRequest from a JSON string
project_project_id_users_post_request_instance = ProjectProjectIdUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectProjectIdUsersPostRequest.to_json())

# convert the object into a dict
project_project_id_users_post_request_dict = project_project_id_users_post_request_instance.to_dict()
# create an instance of ProjectProjectIdUsersPostRequest from a dict
project_project_id_users_post_request_from_dict = ProjectProjectIdUsersPostRequest.from_dict(project_project_id_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


