"""Produces the shebang of a script
"""
class fre_shebang:
    """ Creates a shebang to use at the top of a script"""
    def __init__(self, shellpath='/bin', shell='sh', echo=True):
        """Brief: Sets up the shebang
        Param:
            - shellpath The path to the shell
            - shell The name of the shell being used
            - echo True if the script will echo commands with -fx
        """
        self.shellpath = shellpath
        self.shell = shell
        self.echo = echo
        if self.echo:
            self.shebang = '#!'+shellpath+'/'+shell+' -fx'
        else:
            self.shebang = '#!'+shellpath+'/'+shell
    def get_shebang(self):
        """Brief: Getter routine that returns the shebang """
        return self.shebang
    def check(self, reference):
        """Brief: Checks the shebang in this object against a reference fed into the function
        Param:
            - reference A reference string to check the shebang against
        """
        if self.shebang != reference:
            print(".......... Here comes an error ..........")
            print(f"Shebang:   {self.shebang}")
            print(f"Reference: {reference}")
            raise ValueError("The generated shebang does not match the reference")

""" Tests for the shebang object """
""" Test 1: checking the default """
#reference = '#!/bin/sh -fx'
#default = fre_shebang()
#shebang = default.get_shebang()
#print ("Print default shebang "+reference)
#print (shebang)
#default.check(reference)
""" Test 2: Uses a different  """
#reference = '#!/bin/tcsh -fx'
#tcsh = fre_shebang(shell='tcsh')
#shebang = tcsh.get_shebang()
#print ("Print default shebang "+reference)
#print (shebang)
#tcsh.check(reference)
""" Test 3: Check all options """
#reference = '#!/bin/shell/csh'
#csh = fre_shebang(echo=False, shell='csh', shellpath="/bin/shell")
#shebang = csh.get_shebang()
#print ("Print default shebang "+reference)
#print (shebang)
#csh.check(reference)
"""Test 4: Expected failure to test reference error checking"""
# This is a previously used object and will not match with the current reference
#tcsh.check(reference)

#print ("Done!")
