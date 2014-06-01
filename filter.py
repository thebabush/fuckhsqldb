#!/usr/bin/env python

import sys

allowed_types = [
  "void",
  "short",
  "java.lang.Short",
  "int",
  "java.lang.Integer",
  "long",
  "java.lang.Long",
  "java.math.BigDecimal",
  "double",
  "java.lang.Double",
  "java.lang.String",
  "java.sql.Date",
  "java.sql.Time",
  "java.sql.Timestamp",
  "java.lang.Byte[]",
  "boolean",
  "java.lang.Boolean",
  "java.sql.Array",
  "java.sql.ResultSet",
  ]

def is_public_class(tokens):
  if tokens[-1] == "{" and tokens[0] == "public":
    return True


inside_a_class = False
methods = []
last_class = None
def mangle(line):
  global inside_a_class, last_class, methods
  
  tokens = line.strip().split()
  #print tokens
  
  if len(tokens) == 0:
    return

  if tokens[0] == "{":
    return
  
  if is_public_class(tokens):
    inside_a_class = True
    last_class = line
    return
    
  if tokens[-1] == "}":
    inside_a_class = False
    
    if len(methods) > 0:
      ret = last_class + "\n" + "\n".join(methods) + "\n}\n\n"
      methods = []
      return ret
 
  if len(tokens[-1]) < 3 or tokens[-1][-2] != ")":
    return
  
  if tokens[0] != "public" or tokens[1] != "static" or not ((tokens[2] in allowed_types) or (tokens[2][:-2]) in allowed_types):
    return
  
  start = line.find("(")
  finish = line.find(")")
  args = line[start+1:finish]
  for arg in args.split(", "):
    if not (arg in allowed_types or arg[:-2] in allowed_types):
      return
  
  methods.append(line)

while True:
  line = sys.stdin.readline()
  if line != "":
    line = mangle(line[:-1])
    if line != None:
      print line
  else:
    break
