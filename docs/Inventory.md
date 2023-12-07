# Inventory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**inventory** | **str** |  | [optional] 
**ssh_key_id** | **int** |  | [optional] 
**become_key_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from semaphore_api.models.inventory import Inventory

# TODO update the JSON string below
json = "{}"
# create an instance of Inventory from a JSON string
inventory_instance = Inventory.from_json(json)
# print the JSON string representation of the object
print Inventory.to_json()

# convert the object into a dict
inventory_dict = inventory_instance.to_dict()
# create an instance of Inventory from a dict
inventory_form_dict = inventory.from_dict(inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


