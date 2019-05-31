# pymailflooder

## Setup
* Clone or download the repository
* Extract the file (if needed)
* Rename "config-example.json" to "config.json"
* Add valid usernames and passwords to the config


Valid config syntax:
``` json
{
    "accounts":{
        "c1": "Put Gmail users and passwords here:",
        "usrs":["user1", "user2"],
        "pwds":["pwd1", "pwd2"]
    }
}
```
Be sure that you're using Gmail accounts for this, as support for others has not been added yet. Do not include the @gmail.com at the end of the username, and make sure you've allowed access on each account to non-secure apps.