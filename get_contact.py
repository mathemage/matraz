import base64
import json
import requests
import sys

def get_readme(owner, repo):
    repo_name = owner + '/' + repo
    url = 'https://api.github.com/repos/' + repo_name + '/readme'

    r = requests.get(url)
    j = json.loads(r.text)

    return base64.decodestring(j[u'content'])

def get_contact_for_user(owner):
    url = 'https://api.github.com/users/' + owner

    r = requests.get(url)
    j = json.loads(r.text)

    return j['email']

def get_contact_for_org(owner, repo):
    url = 'https://api.github.com/repos/' + owner + '/' + repo

    r = requests.get(url)
    j = json.loads(r.text)
    
    if not j['has_issues']:
        contact = 'https://github.com/' + owner + '/' + repo + '/issues'
        return contact
    else:
        import re

        EMAIL_REGEX = re.compile('[^@\s]+@[^@\s]+\.[^@\s]+')
        first_email = EMAIL_REGEX.search(get_readme(owner, repo))

        if first_email:
            return first_email.string[first_email.start():first_email.end()]
        else:
            return ""

if __name__ == '__main__':
    print get_readme(sys.argv[1], sys.argv[2])
    print get_contact_for_user(sys.argv[1])
    print get_contact_for_org("inveniosoftware","invenio")
