import base64
from github import Github
from pprint import pprint

# Github username
username = "algorhythms"
# pygithub object
g = Github("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")
# get that user by username
user = g.get_user(username)

def check_repo(repo):
    print("Full name:", repo.full_name)
    print("Language:", repo.language)
    print("-"*50)

    if repo.language == "Python":
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                if ".py" in file_content.name:
                    f = open(file_content.name,'w')
                    print("Storing " + file_content.name+"...")
                    f.write(base64.b64decode(file_content.content).decode())
                    f.close()
    else:
        print("Skipped")    

for repo in user.get_repos():
    check_repo(repo)
    print("="*100)