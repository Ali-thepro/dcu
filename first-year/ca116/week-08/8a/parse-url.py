#!/usr/bin/env python3

import sys
url = sys.argv[1]

scheme = ""
host = ""
port = ""
path = ""
query = ""
fragment = ""

tokens = url.split("://")
scheme = tokens[0]
url = tokens[1]

tokens = url.split("#")
url = tokens[0]
if 1 < len(tokens):
    fragment = tokens[1]

tokens = url.split("?")
url = tokens[0]
if 1 < len(tokens):
    query = tokens[1]

tokens = url.split("/")
host_port = tokens[0]
path = "/" + "/".join(tokens[1:])

tokens = host_port.split(":")
host = tokens[0]

if 1 < len(tokens):
    port = tokens[1]


print("scheme:", scheme)
print("host:", host)
if 0 < len(port):
    print("port:", port)
print("path:", path)
if 0 < len(query):
    print("query-string:", query)
if 0 < len(fragment):
    print("fragment-id:", fragment)
