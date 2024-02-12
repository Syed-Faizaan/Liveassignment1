import requests

def get_latest_commit(username, repository):
    url = f'https://api.github.com/repos/{username}/{repository}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        if commits:
            latest_commit = commits[0]['sha']
            return latest_commit
        else:
            return None
    else:
        print(f"Error: Unable to fetch commits. Status Code: {response.status_code}")
        return None

def main():
    # Replace these values with your GitHub username and repository name
    github_username = 'your_username'
    github_repository = 'your_repository'

    latest_commit = get_latest_commit(github_username, github_repository)

    if latest_commit:
        print(f"Latest commit in {github_repository}: {latest_commit}")
    else:
        print("Unable to fetch latest commit.")

if __name__ == "__main__":
    main()