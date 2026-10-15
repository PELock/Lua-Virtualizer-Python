#!/usr/bin/env python

###############################################################################
#
# Lua Virtualizer WebApi interface usage example.
#
# In this example we will obfuscate sample source with every public option
# set, so you can see the full client surface and turn flags on or off.
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
from luavirtualizer import CodeVirtualization, LuaVirtualizer, RenameStyle

#
# if you don't want to use Python module, you can import directly from the file
#
#from pelock.luavirtualizer import LuaVirtualizer

#
# create Lua Virtualizer class instance (we are using our activation key)
#
myLuaVirtualizer = LuaVirtualizer("ABCD-ABCD-ABCD-ABCD")

#
# should the source code be compressed (both input & compressed)
#
myLuaVirtualizer.enable_compression = False

#
# globals
#
# fixed random seed for reproducible obfuscation output (optional)
#
myLuaVirtualizer.seed = None

#
# randomization density / intensity (0-100)
#
myLuaVirtualizer.randomization_density = None

#
# identifier renaming style: RenameStyle.IL, O0, HEX, or MANGLED
#
myLuaVirtualizer.rename_style = RenameStyle.IL

#
# Lua dialect. "auto" (default) omits the POST field.
# Explicit values: 5.1, 5.2, 5.3, 5.4, 5.5, luajit, luau.
#
myLuaVirtualizer.target = "auto"

#
# code virtualization (exactly one): VM, FSA, or FLAT
# set to None to skip virtualization
#
myLuaVirtualizer.code_virtualization = CodeVirtualization.VM

#
# protection (opt-in on the service for --all; shown enabled here so every flag is visible)
#
# protection against tampering with protected code (integrity verification)
#
myLuaVirtualizer.self_defending = True

#
# protection linker (decoy call graph; requires self_defending)
#
myLuaVirtualizer.protection_linker = True

#
# insert anti-debugging detections
#
myLuaVirtualizer.detect_debugger = True

#
# insert virtual machine (anti-VM) detections
#
myLuaVirtualizer.anti_vm = True

#
# insert anti-sandbox detections
#
myLuaVirtualizer.anti_sandbox = True

#
# insert anti-emulators (CPU) detections
#
myLuaVirtualizer.anti_emulator = True

#
# renaming
#
# rename variable names to random string values
#
myLuaVirtualizer.rename_variables = True

#
# rename parameter names to random string values
#
myLuaVirtualizer.rename_parameters = True

#
# rename function names to random string values
#
myLuaVirtualizer.rename_functions = True

#
# rename function call references consistently with renamed functions
#
myLuaVirtualizer.rename_function_calls = True

#
# shuffle function order in the output source
#
myLuaVirtualizer.shuffle_functions = True

#
# fold/resolve constant expressions at obfuscation time
#
myLuaVirtualizer.resolve_constants = True

#
# strings
#
# split strings into concatenated chunks
#
myLuaVirtualizer.split_strings = True

#
# apply light transformations/mutations to string literals
#
myLuaVirtualizer.modify_strings = True

#
# encrypt strings using randomly generated polymorphic encryption algorithms
#
myLuaVirtualizer.encrypt_strings = True

#
# store string fragments in char-code array vaults
#
myLuaVirtualizer.string_char_array_vault = True

#
# numeric
#
# encrypt integers
#
myLuaVirtualizer.encrypt_integers = True

#
# encrypt floating point numbers
#
myLuaVirtualizer.encrypt_floating = True

#
# replace binary operators with mixed boolean-arithmetic (MBA) equivalents
#
myLuaVirtualizer.mba_binops = True

#
# represent integers via floating-point math
#
myLuaVirtualizer.integers_to_floating = True

#
# move integers to arrays
#
myLuaVirtualizer.integers_to_arrays = True

#
# move floats to arrays
#
myLuaVirtualizer.floats_to_arrays = True

#
# apply redundant xor / affine integer masks
#
myLuaVirtualizer.affine_integer_mask = True

#
# encrypted array literals
#
# encrypt integer array literals
#
myLuaVirtualizer.array_int_crypt = True

#
# encrypt character array literals
#
myLuaVirtualizer.array_char_crypt = True

#
# encrypt floating-point array literals
#
myLuaVirtualizer.array_double_crypt = True

#
# encrypt string array literals
#
myLuaVirtualizer.array_string_crypt = True

#
# decoy value pools
#
# insert a shared bucket of random noise values used by other strategies
#
myLuaVirtualizer.insert_random_value_bucket = True

#
# populate the random value bucket with decoy integers
#
myLuaVirtualizer.random_bucket_integers = True

#
# populate the random value bucket with decoy arrays
#
myLuaVirtualizer.random_bucket_arrays = True

#
# populate the random value bucket with decoy functions
#
myLuaVirtualizer.random_bucket_functions = True

#
# populate the random value bucket with decoy characters
#
myLuaVirtualizer.random_bucket_characters = True

#
# populate the random value bucket with anti-regex decoy noise
#
myLuaVirtualizer.random_bucket_anti_regex = True

#
# populate the random value bucket with autostart decoy stubs
#
myLuaVirtualizer.random_bucket_autostart = True

#
# opaque predicates & noise
#
# rewrite selected statements using ternary operators
#
myLuaVirtualizer.insert_ternary_operators = True

#
# replace boolean conditions with equivalent complex expressions
#
myLuaVirtualizer.complexify_booleans = True

#
# insert opaque predicate branches
#
myLuaVirtualizer.opaque_branches = True

#
# insert opaque mixer chains into control flow
#
myLuaVirtualizer.opaque_mixer_chain = True

#
# insert dead code
#
myLuaVirtualizer.insert_dead_code = True

#
# wrap code in try/finally blocks with dead noise
#
myLuaVirtualizer.try_finally_noise = True

#
# decoys
#
# insert decoy functions
#
myLuaVirtualizer.decoy_functions = True

#
# insert decoy lambda expressions
#
myLuaVirtualizer.lambda_decoys = True

#
# insert literal padding noise
#
myLuaVirtualizer.literal_padding = True

#
# insert fake import statement markers
#
myLuaVirtualizer.fake_import_markers = True

#
# use dynamic getattr()-based indirect calls
#
myLuaVirtualizer.dynamic_getattr_calls = True

#
# rewrite absolute imports into __import__ / getattr
#
myLuaVirtualizer.obfuscate_imports = True

#
# insert dead callback/event registration stubs
#
myLuaVirtualizer.callback_registration_stubs = True

#
# other
#
# strip comments from the output source
#
myLuaVirtualizer.remove_comments = True

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

#
# Per-function marker (source syntax, not a library import). The marker is the
# first statement of a function. The engine reads it and strips it.
#
# local function f()
#   LUAVIRTUALIZER(VM(FSA), OBFUSCATION(encrypt_strings, NUMBERS))
#   return 1
# end
#
# VM(VM|FSA|FLAT|NONE) selects the dispatcher; NONE stays native Lua.
# OBFUSCATION(...) is a blacklist: NONE, ALL, group names NAMES, STRINGS,
# NUMBERS, BOOLEANS, SHAPE, BUCKET, CALLS, COMMENTS, PROTECT, or a specific
# snake_case strategy flag.
