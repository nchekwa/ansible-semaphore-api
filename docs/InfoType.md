# InfoType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**update_body** | **str** |  | [optional] 
**update** | [**InfoTypeUpdate**](InfoTypeUpdate.md) |  | [optional] 

## Example

```python
from semaphore_api.models.info_type import InfoType

# TODO update the JSON string below
json = "{}"
# create an instance of InfoType from a JSON string
info_type_instance = InfoType.from_json(json)
# print the JSON string representation of the object
print(InfoType.to_json())

# convert the object into a dict
info_type_dict = info_type_instance.to_dict()
# create an instance of InfoType from a dict
info_type_from_dict = InfoType.from_dict(info_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


