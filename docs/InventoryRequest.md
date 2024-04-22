# InventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**inventory** | **str** |  | [optional] 
**ssh_key_id** | **int** |  | [optional] 
**become_key_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.inventory_request import InventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryRequest from a JSON string
inventory_request_instance = InventoryRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryRequest.to_json())

# convert the object into a dict
inventory_request_dict = inventory_request_instance.to_dict()
# create an instance of InventoryRequest from a dict
inventory_request_from_dict = InventoryRequest.from_dict(inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


