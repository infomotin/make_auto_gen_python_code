from github import Github
import time
from datetime import datetime
import os
# //from curtsies.fmtfuncs import red, bold, green, on_blue, yellow
# //for colour


access_token = open("../src/token.txt", "r").read()
g = Github(access_token)
# print(g.get_user())
# for repo in g.get_user().get_repos():
#     print(repo.name)
end_time = time.time()
start_time = end_time-86400

# search_query = "language:python"
# search_query = "flask language:python created:2020-04-01..2021-04-02"


for i in range(50):
    try:
        start_time_in_str = datetime.utcfromtimestamp(
            start_time).strftime('%Y-%m-%d')
        end_time_in_str = datetime.utcfromtimestamp(
            end_time).strftime('%Y-%m-%d')
        search_query = f"language:python created:{start_time_in_str}..{end_time_in_str}"
        print(search_query)
        end_time -= 86400
        start_time -= 86400
        # print(start_time)
        result = g.search_repositories(search_query)
        # print("time dif")
        # print(end_time)
        # print(dir(result))
        print(result.totalCount)
        # continue1 = 0
        for rep in result:

            print(f"{rep.clone_url}")
            print(f"{rep.tags_url}")
            # clone Repository
            os.system(
                f"git clone {rep.clone_url} repos/{rep.owner.login}/{rep.name}")
            # print(f"{rep.get_labels()}")
            # print(f"{rep._clone_url}")
            # print(dir(rep))
            # counter = 0
            # for label in rep.get_labels()[:5]:
            #     counter = counter + 1
            #     # print(label)

            #     break
            # print(counter)
            print(start_time)

    except Exception as e:
        print(str(e))
        print("Wrong With something")
        time.sleep(120)
