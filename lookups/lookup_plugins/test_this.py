from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):
#    def run(self, terms, variables=None, **kwargs):
    def run(self, terms, **kwargs):
        ret = ['hello']
        for term in terms:
            display.vvvv("Lookup term: %s" % term)
        return ret
