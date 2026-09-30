GITHUB_LINK = 'https://github.com/FrillySnake/cs567-triangle-testing'

import requests
import unittest

USER_ID = 'FrillySnake' # NOTE: empty this string to use user input, or replace with a different user id of choice

def access_github(userId):
    repos = requests.get(f'https://api.github.com/users/{userId}/repos').json()
    output = []
    # print(repos)

    for r in repos:
        name = r['name']
        commits = requests.get(f'https://api.github.com/repos/{userId}/{name}/commits').json()
        output.append(f'Repo: {name} Number of commits: {len(commits)}')
    
    return output

def run_access_github(userId):
    output = access_github(userId)
    for i in output:
        print(i)

from unittest.mock import Mock, patch

def fake_get(url):
        if url == 'https://api.github.com/users/FrillySnake/repos':
            response = Mock()
            response.json.return_value = [{'name': 'CS562-ESQL'}, {'name': 'cs567-triangle-testing'}]
            return response

        if url == 'https://api.github.com/repos/FrillySnake/CS562-ESQL/commits':
                    response = Mock()
                    response.json.return_value = [{'id': 1}, {'id': 2}]
                    return response

        if url == 'https://api.github.com/repos/FrillySnake/cs567-triangle-testing/commits':
                            response = Mock()
                            response.json.return_value = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}, {'id': 7}]
                            return response

        if url == 'https://api.github.com/users/richkempinski/repos':
                    response = Mock()
                    response.json.return_value = [{'name': 'hellogitworld'}, {'name': 'Mocks'}, {'name': 'threads-of-life'}, {'name': 'try_nbdev'}]
                    return response
        
        if url == 'https://api.github.com/repos/richkempinski/hellogitworld/commits':
                    response = Mock()
                    response.json.return_value = [{'id': 1}, {'id': 2}, {'id': 3}]
                    return response

        if url == 'https://api.github.com/repos/richkempinski/Mocks/commits':
                            response = Mock()
                            response.json.return_value = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 6}, {'id': 7}, {'id': 8}, {'id': 9}]
                            return response

        if url == 'https://api.github.com/repos/richkempinski/threads-of-life/commits':
                            response = Mock()
                            response.json.return_value = [{'id': 1}]
                            return response
        
        if url == 'https://api.github.com/repos/richkempinski/try_nbdev/commits':
                            response = Mock()
                            response.json.return_value = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}]
                            return response

class TestGithub(unittest.TestCase):
    def testSet1(self):
        with patch('__main__.requests.get') as mock_get:
            mock_get.side_effect = fake_get

            self.assertListEqual(access_github('richkempinski'), ['Repo: hellogitworld Number of commits: 3', 'Repo: Mocks Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 5'], 'Confirm list output is equal')
            self.assertIn('Repo: CS562-ESQL Number of commits: 2', access_github('FrillySnake'), 'Confirm specific element in list output')

if __name__ == '__main__':
    userId = USER_ID if USER_ID else input('Enter a GitHub User ID: ')
    # run_access_github(userId)

    unittest.main(exit=True)