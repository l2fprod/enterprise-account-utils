#!/bin/bash
export THIS_DIR="$( cd "$(dirname "$0")" ; pwd -P )"

ibmcloud login -a $ENDPOINT --apikey $API_KEY -r $REGION

ibmcloud account enterprise accounts --recursive --output JSON > accounts.json
ibmcloud account enterprise account-groups --recursive --output JSON > account-groups.json

python3 $THIS_DIR/enterprise2gv.py
dot enterprise.gv -Tpng -o enterprise.png
