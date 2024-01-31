import subprocess
import json
import os
try:
    userData = subprocess.getstatusoutput(f'gh api -H "Accept: application/vnd.github+json" /user')
    user=json.loads(userData[1])
    userName=user['name']
    userLogin=user['login']
    file=os.path.basename(__file__)
    spell=file.split('.')[0]
    code="aHR0cHM6Ly9naX"

 

    print(f'''

    {userName} (@{userLogin}), you are about to use the {spell} spell. Are you sure this is the right one?
    If yes, then the secret code assosciated with it is:
    {code}
        ''')
       

except Exception as e:
    print("Unkown Error occured, please try again later")