[link to index](/readme.md)  
# Git read me
git is a method of version control and can be combined with github for online version control

## Setting up git
[how to set up git](https://kbroman.org/github_tutorial/pages/first_time.html)  
[how to set up git properly](https://medium.com/@aklson_DS/how-to-properly-setup-your-github-repository-windows-version-ea596b398b)  
[how to stop UAC prompts using scheduler](https://www.makeuseof.com/tag/stop-annoying-uac-prompts-how-to-create-a-user-account-control-whitelist-windows/)

## Good practice
- rename master to main

## Common git commands:
- `git status`
- `git add filename`
- `git commit -m "message"`
- `git push`

## Extra commands
- `git reset --hard origin/main`
    - forces a pull and reset a branch

## fixing .gitignore not tracking
```
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
git push
```

## Best practice
- don't work in the main branch