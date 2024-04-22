# LoginMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc_providers** | [**List[LoginMetadataOidcProvidersInner]**](LoginMetadataOidcProvidersInner.md) | List of OIDC providers | [optional] 

## Example

```python
from semaphore_api.models.login_metadata import LoginMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LoginMetadata from a JSON string
login_metadata_instance = LoginMetadata.from_json(json)
# print the JSON string representation of the object
print(LoginMetadata.to_json())

# convert the object into a dict
login_metadata_dict = login_metadata_instance.to_dict()
# create an instance of LoginMetadata from a dict
login_metadata_from_dict = LoginMetadata.from_dict(login_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


