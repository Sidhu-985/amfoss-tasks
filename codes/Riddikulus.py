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
    code="Uh1bnRzbWFuNC9U"
    print(f'''
    {userName} (@{userLogin}), you have found the right spell. As a part of your reward for solving the riddle,
    here is the secret code assosciated with it: {code}
    ''')

except Exception as e:
    print("Unkown Error occured, please try again later")