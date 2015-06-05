'''
import base64
import json
'''
import sys
import requests
import re

from contact import get_readme

def has_docs(owner, repo):
    url = 'https://github.com/' + owner + '/' + repo + '/tree/master/doc'

    try:
        r = requests.get(url)
        r.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        try:
            r = requests.get(url+'s')
            r.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            # parse Readme file
            #DOCS_REGEX = re.compile('[^a-zA-Z]Documentation[^a-zA-Z]')
            DOCS_REGEX = re.compile('### Documentation\s')
            readme = get_readme(owner, repo)
            docs = DOCS_REGEX.search(readme)

            return docs.end() == 0
'''
            if docs.end() != 0:
                return True
            else:
                docs = DOCS_REGEX.search(readme)
'''

if __name__ == "__main__":
    #print has_docs(sys.argv[1], sys.argv[2])
    print "mathemage", "Matrixpp",     has_docs("mathemage", "Matrixpp")
    print "MSusik", "beard",           has_docs("MSusik", "beard")
    print "MSusik", "matraz",          has_docs("MSusik", "matraz")
    print "dzenbot", "dznemptydataset",has_docs("dzenbot", "dznemptydataset")
