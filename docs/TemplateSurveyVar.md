# TemplateSurveyVar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from semaphore_api.models.template_survey_var import TemplateSurveyVar

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSurveyVar from a JSON string
template_survey_var_instance = TemplateSurveyVar.from_json(json)
# print the JSON string representation of the object
print TemplateSurveyVar.to_json()

# convert the object into a dict
template_survey_var_dict = template_survey_var_instance.to_dict()
# create an instance of TemplateSurveyVar from a dict
template_survey_var_form_dict = template_survey_var.from_dict(template_survey_var_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


