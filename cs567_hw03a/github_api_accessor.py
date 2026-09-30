GITHUB_LINK = 'https://github.com/FrillySnake/cs567-triangle-testing'

import requests
import unittest

USER_ID = 'FrillySnake' # fill with a GitHub user id to skip user input

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

class TestGithub(unittest.TestCase):
    def testSet1(self):
        self.assertListEqual(access_github('richkempinski'), ['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5'], 'Confirm list output is equal')
        self.assertIn('Repo: CS562-ESQL Number of commits: 27', access_github('FrillySnake'), 'Confirm specific element in list output')

if __name__ == '__main__':
    userId = USER_ID if USER_ID else input('Enter a GitHub User ID: ')
    run_access_github(userId)

    unittest.main(exit=True)