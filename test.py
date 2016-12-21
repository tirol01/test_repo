#!/usr/bin/env python

import sys

def calc(a, b):
  try:
    result = float(a) + float(b)
  except:
    sys.stderr.write('input is not numeric.')
    return None

  if result.is_integer():
    return int(result)
  return result


if __name__ == '__main__':
  ret = calc('hoge', 2) 
  print(ret)
