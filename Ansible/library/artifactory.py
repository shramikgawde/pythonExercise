#!/usr/bin/python
import json
def call_artifactory(module, product_name, product_version):
  if product_name == "Apache":
      new_product_name = product_name + "-http"
      module.exit_json(msg="%s" % new_product_name, changed=True)
  elif product_name == "jboss":
      new_product_name = product_name + "_EAP"
      module.exit_json(msg="%s" % new_product_name, changed=True)
  elif product_name == "tomcat":
      module.exit_json(msg="%s" % product_name, changed=True)
