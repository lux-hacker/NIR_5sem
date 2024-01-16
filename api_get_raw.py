from github import Github, Auth


def get_raw_github_repo_csv(repo_name: str, token: str, ignore_files: list[str], csv_file: str, is_malware: int) -> None:
    auth = Auth.Token(token)
    g = Github(auth=auth)
    repo = g.get_repo(repo_name)
    content = repo.get_contents("")
    with open(csv_file, "a") as malicious_csv:
        while content:
            file_content = content.pop(0)
            if file_content.type == "dir":
                content.extend(repo.get_contents(file_content.path))
            else:
                exe = file_content.path[file_content.path.rfind("."):]
                if exe in ignore_files:
                    continue
                malicious_csv.write(
                    f"{file_content.path},https://raw.githubusercontent.com/{repo_name}/main/{file_content.path},{is_malware}\n")
