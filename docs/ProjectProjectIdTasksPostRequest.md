# ProjectProjectIdTasksPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** |  | [optional] 
**debug** | **bool** |  | [optional] 
**dry_run** | **bool** |  | [optional] 
**diff** | **bool** |  | [optional] 
**playbook** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**limit** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.project_project_id_tasks_post_request import ProjectProjectIdTasksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectProjectIdTasksPostRequest from a JSON string
project_project_id_tasks_post_request_instance = ProjectProjectIdTasksPostRequest.from_json(json)
# print the JSON string representation of the object
print ProjectProjectIdTasksPostRequest.to_json()

# convert the object into a dict
project_project_id_tasks_post_request_dict = project_project_id_tasks_post_request_instance.to_dict()
# create an instance of ProjectProjectIdTasksPostRequest from a dict
project_project_id_tasks_post_request_form_dict = project_project_id_tasks_post_request.from_dict(project_project_id_tasks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


