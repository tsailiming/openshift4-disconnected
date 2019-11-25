# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display

from docker_image import reference

display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):


        ret = []
        for term in terms:

            try:
              ref = reference.Reference.parse(term)

              ret.append({'domain': ref.domain(), 
                          'path': ref.path(),
                          'name': ref['name']})

            except AnsibleParserError:
                raise AnsibleError("could parse docker image: %s" % term)
          
        return ret