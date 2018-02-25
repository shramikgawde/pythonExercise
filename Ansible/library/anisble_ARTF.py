#!/usr/bin/python
import json

from ansible.module_utils.basic import AnsibleModule
from pprint import pprint

def call_artifactory(module, product_name, product_version):
  if product_name == "Apache":
      new_product_name = product_name + "-http"
      module.exit_json(msg="%s" % new_product_name, changed=True)
  elif product_name == "jboss":
      new_product_name = product_name + "_EAP"
      module.exit_json(msg="%s" % new_product_name, changed=True)
  elif product_name == "tomcat":
      module.exit_json(msg="%s" % product_name, changed=True)



def main():
  module = AnsibleModule(
    argument_spec=dict(
      product_name=dict(required=True),
      product_version=dict(required=True)

    )
  )
  
  product_name = module.params['product_name']
  product_version = module.params['product_version']
  call_artifactory(module, product_name, product_version)
if __name__=='__main__':
    main()