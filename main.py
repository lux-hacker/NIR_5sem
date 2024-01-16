from api_get_raw import get_raw_github_repo_csv
from config import TOKEN


def main():
    repo = input("Enter GitHub repository likes 'OWNER/REPOSITORY_NAME': ")
    csv_file = input("Enter path to csv file: ")
    is_malware = int(input("Enter 0 if repo is legal and 1 for malware: "))
    archive = [".7z", ".zip", ".tar.gz", ".tgz", ".rar"]
    other_file = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".md", ".asm", ".txt"]
    useless_file = archive + other_file
    get_raw_github_repo_csv(repo, TOKEN, useless_file, csv_file, is_malware)


if __name__ == "__main__":
    main()
