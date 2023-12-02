# Task


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**template_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**debug** | **bool** |  | [optional] 
**playbook** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**limit** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


