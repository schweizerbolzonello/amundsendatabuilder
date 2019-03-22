import json
import unittest

from databuilder.models.user_elasticsearch_document import UserESDocument


class TestUserElasticsearchDocument(unittest.TestCase):

    def test_to_json(self):
        # type: () -> None
        """
        Test string generated from to_json method
        """
        test_obj = UserESDocument(elasticsearch_index='test_index',
                                  elasticsearch_type='test_type',
                                  email='test@email.com',
                                  first_name='test_firstname',
                                  last_name='test_lastname',
                                  name='full_name',
                                  team_name='team',
                                  employee_type='fte',
                                  manager_email='test_manager',
                                  slack_id='test_slack',
                                  total_read=2,
                                  total_own=3,
                                  total_follow=1)

        expected_index_dict = {"index": {"_type": "test_type", "_index": "test_index"}}
        expected_document_dict = {"first_name": "test_firstname",
                                  "last_name": "test_lastname",
                                  "name": "full_name",
                                  "team_name": "team",
                                  "total_follow": 1,
                                  "total_read": 2,
                                  "is_active": True,
                                  "total_own": 3,
                                  "slack_id": 'test_slack',
                                  "manager_email": "test_manager",
                                  'github_username': "",
                                  "employee_type": 'fte',
                                  "email": "test@email.com",
                                  }

        result = test_obj.to_json()
        results = result.split("\n")

        # verify two new line characters in result
        self.assertEqual(len(results), 3, "Result from to_json() function doesn't have 2 newlines!")

        self.assertDictEqual(json.loads(results[0]), expected_index_dict)
        print(results[1])
        self.assertDictEqual(json.loads(results[1]), expected_document_dict)
