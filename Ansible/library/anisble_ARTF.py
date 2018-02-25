#!/usr/bin/python
import json

from ansible.module_utils.basic import AnsibleModule
from pprint import pprint

def call_artifactory(module, product_name, product_version):
  if (product_name == "Apache" or product_name == "apache"):
      new_product_name = product_name.lower() + "-http"
      
      module.exit_json(msg="Successful execution", dir_product_name="%s" % new_product_name, changed=True)
  elif (product_name == "JBoss_EAP" or product_name == "jboss" or product_name == "JBoss"):
      new_product_name = product_name[:5].lower()
      print(new_product_name)
      module.exit_json(msg="Successful execution", dir_product_name="%s" % new_product_name, changed=True)
  elif (product_name == "Tomcat" or product_name == "tomcat"):
      new_product_name = product_name.lower()
      module.exit_json(msg="Successful execution", dir_product_name="%s" % new_product_name, changed=True)

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