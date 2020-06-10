# aviSlackAlerts

## Goals
Ansible Playbook to send Slack Alert when an event is triggered.

## Prerequisites:
1. Make sure the controller is available at the IP defined in vars/creds.json
2. Make sure avisdk is installed:
```
pip install avisdk
ansible-galaxy install -f avinetworks.avisdk
```

## Environment:
Playbook(s) has/have been tested against:

### Ansible

```
avi@ansible:~/ansible/aviSlackAlerts$ ansible --version
ansible 2.9.5
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/avi/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /home/avi/.local/lib/python2.7/site-packages/ansible
  executable location = /home/avi/.local/bin/ansible
  python version = 2.7.12 (default, Oct  8 2019, 14:14:10) [GCC 5.4.0 20160609]
avi@ansible:~/ansible/aviSlackAlerts$
```

### Avi version

```
Avi 18.2.9
```

## Input/Parameters:

All the paramaters/variables are stored in var/params.yml. A variable needs to be configured with webhook_url like follow:
```
---
webhook_url: https://hooks.slack.com/services/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

alertscriptconfig:
  action_script: |
    #!/usr/bin/python
    import json, requests
    requests.packages.urllib3.disable_warnings()
    webhook_url = "{{ webhook_url }}"
    slack_data = {'text': "Your Virtual Service {{ item.0 }} is {{ item.1 }}"}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
       raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
    )
```

## Use the ansible playbook to:
1. Retrieve all the VS name and uuid
2. For each VS: Create Alert Script to check when VSs are up or down
3. For each VS: Create ActionGroupConfig when VSs are up or down
4. For each VS: Create AlertConfig when VSs are up
5. For each VS: Create AlertConfig when VSs are down

## Run the playbook:
ansible-playbook configureAlerts.yml

## Improvement:
throttle parameters default: 600
https://docs.ansible.com/ansible/latest/modules/avi_alertconfig_module.html
