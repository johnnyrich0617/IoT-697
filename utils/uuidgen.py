import uuid
import netifaces

'''
Utility to Generate a type 5 UUID
'''


def generate_uuid(name='', domain='.snhu.edu'):
    mac = netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr'].encode('utf-8')
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, mac+'.'+name+domain))
