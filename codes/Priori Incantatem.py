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
    code="aGVGaW5hbFNwZWxs"

 

    print(f'''

    {userName} (@{userLogin}), you are about to initiate the {spell}. Are you sure it?
    If yes, then the secret code assosciated with it is:
    {code}
        ''')
       

except Exception as e:
    print("Unkown Error occured, please try again later")