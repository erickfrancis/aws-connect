__author__ = 'erickfrancis'

import boto.ec2

conn = boto.ec2.connect_to_region('sa-east-1', aws_access_key_id='',
                                  aws_secret_access_key='')
instances = []

for instance in conn.get_only_instances():
    instances.append({
        'id':instance.id,
        'state':instance.state,
        'key':instance.key_name,
        'end_point':instance.ip_address
    })

print(instances)