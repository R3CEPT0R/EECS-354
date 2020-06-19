#!/usr/bin/python

import os
import sys
import random
from popen2 import Popen3

def run(out):
  langs = ["c", "ruby", "shell", "mysql"]

  if len(sys.argv) > 1:
    newlangs = []
    for lang in sys.argv[1:]:
      if lang in langs:
        newlangs.append(lang)
      else:
        print >> sys.stderr, 'Ignoring language %s' % lang
    langs = newlangs

  total_passed = 0
  total_tests = 0
  cwd = os.getcwd()

  for lang in langs:
    print >> out, "Testing %s...\n%s" % (lang, "-"*70);

    os.chdir('%s/%s' % (os.path.dirname(__file__), lang))
    print >> out, 'Building...'
    p = Popen3('./build')
    out.write(p.fromchild.read())
    status = p.wait()

    testcount = 4
    successcount = 0
    linecount = 0

    if status:
      print >> out, 'Failed to build.'

    else:
      if lang == 'c': testcount = 3
      if lang == 'mysql': testcount = 5
      if lang == 'shell': testcount = 8
      command = os.popen('./testrig', 'r')

      while True:
        line = command.readline()
        if not line: break
        linecount += 1
        if linecount > testcount:
          print >> out, 'Error: saw too many lines. Make sure you aren\'t printing anything.'
          successcount = 0
          break

        if lang == 'python':
          if (line.strip() == 'True'): successcount += 1
        else:
          if (line.strip() == 'correct'): successcount += 1

      command.close()

    os.chdir(cwd)
    print >> out, "Passed %i out of %i tests.\n" % (successcount, testcount)
    total_passed += successcount
    total_tests += testcount

  os.chdir(cwd)
  return total_passed, total_tests

if __name__ == '__main__':
  run(sys.stdout)
