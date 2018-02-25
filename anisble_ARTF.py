#!/usr/bin/python
    from ansible.module_utils.basic import AnsibleModule

    def call_artifactory(mod_artf):
        print ("test".format(product_name,product_version))

    def main():
        mod_artf = AnsibleModule(
            argument_spec=dict(
                product_name=dict(required=True),
                product_version=dict(required=True)

            )
        )

        call_artifactory(mod_artf)

if __name__=='__main__':
    main()