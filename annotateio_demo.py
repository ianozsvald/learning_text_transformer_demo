# coding=UTF8
"""Annotate.io demo  to show how we learn a transformation sequence for data cleaning"""
from __future__ import print_function, unicode_literals
import requests
import json

# Tested on:
# Python 3.4, 2.7 (the unicode examples work but looks a bit odd when
# printed on 2.7)

# To learn more go to: http://annotate.io

root_url = "http://api.annotate.io"  # API URL

# show the docstring for this module as a bit of help for the user
print(__doc__)

# call / with a GET and confirm a 200 'OK' status code to confirm that the
# site it running
resp = requests.get(root_url)
assert resp.status_code == 200, "If we don't get a 200 OK then maybe the server is down?"

# Use a POST to call /learn with examples of
# the desired inputs and outputs
root_url = root_url
query = {'inputs': ['Accenture PLC',
                    'Accenture Europe',
                    'Société Générale',
                    'SociÃ©tÃ© GÃ©nÃ©rale'],
         'outputs': ['accenture',
                     'accenture europe',
                     'societe generale',
                     'societe generale']}
print()
print("Training phase - we use `inputs` to learn a transformation to get to the desired `outputs`:")
print("inputs:", query['inputs'])
print("outputs:", query['outputs'])
print("Calling Annotate.io...")
resp = requests.post(root_url + "/learn",
                     data=json.dumps(query),
                     headers={'Content-Type': 'application/json'})
assert resp.status_code == 200

# store the code that we're sent
transforms = resp.json()['transforms']
print("Training phase complete, now we have a `transforms` code")

# Use a POST to call /transform with the code
# and new inputs, we'll receive outputs back
query = {'inputs': ['RBS PLC',  # token 'Ltd' that needs stripping
                    'Royal Bank of Scotland PLC',
                    'Lancôme',  # non-ASCII characters
                    ' Estée Lauder  '  # spare prefix/suffix whitespace
                    ],
         'transforms': transforms}
print()
print("Data cleaning phase - we use the `transforms` that we've learned on previously unseen `inputs` items to generate new `outputs`):")
print("inputs:", query['inputs'])

resp = requests.post(root_url + "/transform",
                     data=json.dumps(query),
                     headers={'Content-Type': 'application/json'})
assert resp.status_code == 200
result = resp.json()
print("We now have a transformed result:")
print("outputs:", result['outputs'])

print("\nPretty printed:")
print("{inp:>30}    {out:>30}".format(
    inp="Previously unseen input:", out="Annotate's output:"))
for (inp, out) in zip(query['inputs'], result['outputs']):
    print("{inp:>30} -> {out:>30}".format(inp=inp, out=out))

print(
    "\nThe transforms that are used in this demo include: Lowercase, Strip white-space, Convert unicode to ASCII, Strip token (to remove 'Ltd'), Fix badly encoded unicode")
