# ScheduleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**cron_format** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**template_id** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.schedule_request import ScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleRequest from a JSON string
schedule_request_instance = ScheduleRequest.from_json(json)
# print the JSON string representation of the object
print ScheduleRequest.to_json()

# convert the object into a dict
schedule_request_dict = schedule_request_instance.to_dict()
# create an instance of ScheduleRequest from a dict
schedule_request_form_dict = schedule_request.from_dict(schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


