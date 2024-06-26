# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.template_survey_var import TemplateSurveyVar

class TestTemplateSurveyVar(unittest.TestCase):
    """TemplateSurveyVar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplateSurveyVar:
        """Test TemplateSurveyVar
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplateSurveyVar`
        """
        model = TemplateSurveyVar()
        if include_optional:
            return TemplateSurveyVar(
                name = '',
                title = '',
                description = '',
                type = 'String => "", Integer => "int"',
                required = True
            )
        else:
            return TemplateSurveyVar(
        )
        """

    def testTemplateSurveyVar(self):
        """Test TemplateSurveyVar"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
