# TaskOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **int** |  | [optional] 
**task** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**output** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.task_output import TaskOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TaskOutput from a JSON string
task_output_instance = TaskOutput.from_json(json)
# print the JSON string representation of the object
print TaskOutput.to_json()

# convert the object into a dict
task_output_dict = task_output_instance.to_dict()
# create an instance of TaskOutput from a dict
task_output_form_dict = task_output.from_dict(task_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


