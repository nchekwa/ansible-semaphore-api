# LoginMetadataOidcProvidersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the provider, used in the login URL | [optional] 
**name** | **str** | Text to show on the login button | [optional] 

## Example

```python
from semaphore_api.models.login_metadata_oidc_providers_inner import LoginMetadataOidcProvidersInner

# TODO update the JSON string below
json = "{}"
# create an instance of LoginMetadataOidcProvidersInner from a JSON string
login_metadata_oidc_providers_inner_instance = LoginMetadataOidcProvidersInner.from_json(json)
# print the JSON string representation of the object
print LoginMetadataOidcProvidersInner.to_json()

# convert the object into a dict
login_metadata_oidc_providers_inner_dict = login_metadata_oidc_providers_inner_instance.to_dict()
# create an instance of LoginMetadataOidcProvidersInner from a dict
login_metadata_oidc_providers_inner_form_dict = login_metadata_oidc_providers_inner.from_dict(login_metadata_oidc_providers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


