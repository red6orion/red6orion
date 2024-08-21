import datetime
import pytz-2024.1.tar.gz
import re
import os
from github import Github

def get_greeting():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_tz)
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def update_readme(greeting):
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()

    new_content = re.sub(r'(Доброе утро|Добрый день|Добрый вечер|Доброй ночи)',
                         greeting, content, count=1)

    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(new_content)

def main():
    greeting = get_greeting()
    update_readme(greeting)

    # Обновляем README на GitHub
    g = Github(os.environ['GITHUB_TOKEN'])
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    contents = repo.get_contents("README.md")
    repo.update_file(contents.path, f"Update greeting to {greeting}", 
                     new_content, contents.sha)

if __name__ == "__main__":
    main()
