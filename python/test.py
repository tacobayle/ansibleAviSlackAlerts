#!/usr/bin/python
import json, requests
requests.packages.urllib3.disable_warnings()
webhook_url = "https://hooks.slack.com/services/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"
slack_data = {'text': "Your Virtual Service vs2-http is up"}

response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
        )
if response.status_code != 200:
       raise ValueError(
               'Request to slack returned an error %s, the response is:\n%s'
               % (response.status_code, response.text)
               )

