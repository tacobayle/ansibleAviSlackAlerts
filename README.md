# aviAlerts
## Prerequisites:
1. Make sure the controller is available at the IP defined in vars/creds.json
2. Make sure avisdk is installed:
```
pip install avisdk==18.1.5b3
ansible-galaxy install -f avinetworks.avisdk
```

## Input:
1. Make sure vars/creds.json is defined properly
```
{"avi_credentials": {"username": "admin", "controller": "192.168.139.130", "password": "Avi_2019", "api_version": "17.2.14"}}
```

## Use the ansible playbook to:
1. Retrieve all the VS name and uuid
2. For each VS: Create Alert Script to check when VSs are up or down
3. For each VS: Create ActionGroupConfig when VSs are up or down
4. For each VS: Create AlertConfig when VSs are up
5. For each VS: Create AlertConfig when VSs are down

## Parameters:
All the paramaters/variables are stored in var/params.yml

## Run the playbook:
ansible-playbook configureAlerts.yml

## Tests:
Playbooks have been tested against:
- Environment: LSC (wo cluster)
- Avi 17.2.14
- 2.8.0.dev0

## Improvement:
throttle parameters default: 600
https://docs.ansible.com/ansible/latest/modules/avi_alertconfig_module.html
