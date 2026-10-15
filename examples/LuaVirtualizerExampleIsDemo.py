#!/usr/bin/env python

###############################################################################
#
# Lua Virtualizer WebApi interface usage example.
#
# In this example we will verify our activation key status.
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
# login to the service
#
result = myLuaVirtualizer.login()

#
# result[] array holds the information about the license
#
# result["demo"]          - demo mode (missing or invalid key); limited to 1000 bytes; the server applies only flat code virtualization (code_virtualization=flat), ignoring every other strategy field
# result["license_expiration"] - license end date (Y-m-d), empty if none
# result["usages_total"]  - total obfuscations for this activation code
# result["string_limit"]  - max. source code size allowed (it's 1000 bytes for demo mode)
#
if result:

    print(f'Demo version status - {"True" if result["demo"] else "False"}')
    print(f'License expiration - {result.get("license_expiration")}')
    print(f'Total obfuscations - {result.get("usages_total")}')
    print(f'Max. source code size - {result["string_limit"]}')

else:
    print("Something unexpected happen while trying to login to the service.")
