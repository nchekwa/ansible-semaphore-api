# APIToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**expired** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from semaphore_api.models.api_token import APIToken

# TODO update the JSON string below
json = "{}"
# create an instance of APIToken from a JSON string
api_token_instance = APIToken.from_json(json)
# print the JSON string representation of the object
print(APIToken.to_json())

# convert the object into a dict
api_token_dict = api_token_instance.to_dict()
# create an instance of APIToken from a dict
api_token_from_dict = APIToken.from_dict(api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


