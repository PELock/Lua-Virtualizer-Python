#!/usr/bin/env python

###############################################################################
#
# Lua Virtualizer WebApi interface usage example.
#
# In this example we will obfuscate sample source with default options.
#
# Version        : v1.0.0
# Language       : Python
# Author         : Bartosz Wójcik
# Web page       : https://www.pelock.com
#
###############################################################################

#
# include Lua Virtualizer module
#
from luavirtualizer import LuaVirtualizer

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.luavirtualizer import LuaVirtualizer

#
# create Lua Virtualizer class instance (we are using our activation key)
#
myLuaVirtualizer = LuaVirtualizer("ABCD-ABCD-ABCD-ABCD")

#
# source code in Lua format
#
scriptSourceCode = """local function greet(name)
  print("Hello, " .. name)
end
greet("Lua")
"""

#
# by default all obfuscation options are enabled, so we can just simply call
#
result = myLuaVirtualizer.obfuscate_script_source(scriptSourceCode)

#
# it's also possible to pass a Lua script file path instead of a string with the source e.g.
#
# result = myLuaVirtualizer.obfuscate_script_file("/path/to/project/script.lua")

#
# result[] array holds the obfuscation results as well as other information
#
# result["error"]         - error code
# result["output"]        - obfuscated code
# result["demo"]          - demo mode (missing or invalid key); limited to 1000 bytes; the server applies only flat code virtualization (code_virtualization=flat), ignoring every other strategy field
# result["license_expiration"] - license end date (Y-m-d), empty if none
# result["usages_total"]  - total obfuscations for this activation code
#
if result and "error" in result:

    # display obfuscated code
    if result["error"] == LuaVirtualizer.ERROR_SUCCESS:

        # format output code for HTML display
        print(result["output"])

    else:
        print(f'An error occurred, error code: {result["error"]}')

else:
    print("Something unexpected happen while trying to obfuscate the code.")
