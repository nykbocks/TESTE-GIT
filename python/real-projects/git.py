
import os

repo = input("qual repositorio? -->")

os.system(f"git remote add {repo} https://github.com/nykbocks/{repo}")
file = input("que arquivo? -->")
branch = input("qual branch? -->")

os.system(f"git switch {branch}")

os.system(f"git add {file}")

os.system("git commit")

os.system(f"git push {repo}")
