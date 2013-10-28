import sys
import time 

import numpy as np
from nose.tools import nottest

def run_local_functions(prefix, locals_dict = None):
  if locals_dict is None:
    last_frame = sys._getframe()
    locals_dict = last_frame.f_back.f_locals

  good = set([])
  # bad = set([])
  for k, test in locals_dict.items():
    if k.startswith(prefix):
      print "Running %s..." % k
      try:
        test()
        print "\n --- %s passed\n" % k
        good.add(k)
      except:
        raise

  print "\n%d tests passed: %s\n" % (len(good), ", ".join(good))

@nottest
def run_local_tests(locals_dict = None):
  if locals_dict is None:
    last_frame = sys._getframe()
    locals_dict = last_frame.f_back.f_locals
  return run_local_functions("test_", locals_dict)

def eq(x,y):
  """
  print "x", x
  print "y", y
  print "x type", type(x)
  print "y type", type(y)
  if hasattr(x,'shape'): print "x shape", x.shape 
  if hasattr(y, "shape"): print "y shape", y.shape 
  if hasattr(x, 'strides'): print 'x strides', x.strides 
  if hasattr(y, 'strides'): print 'y strides', y.strides
  print "x raveled", np.ravel(x)
  print "y raveled", np.ravel(y)
  if hasattr(x, 'flags'): print "x flags", x.flags 
  if hasattr(y, 'flags'): print "y flags", y.flags
  """ 
  if x is None:
    return y is None 
  elif np.isscalar(x) and np.isnan(x):
    return np.isscalar(x) and np.isnan(y)
  elif isinstance(x, tuple) or isinstance(y, tuple):
    return type(x) == type(y) and len(x) == len(y) and all(eq(xi,yi) for xi, yi in zip(x,y))
  else:
    try:
      return np.allclose(x,y, atol=0.0001, rtol=0.001)
    except:
      return False 
    
def expect_eq(actual,expected, test_name = None):
  if test_name is None:
    test_name = ""
  else: 
    test_name = "[" + test_name + "] "
  assert eq(actual,expected), "%sExpected %s but got %s" % (test_name, expected,actual)
  
def copy(x):
  if isinstance(x, np.ndarray):
    return x.copy()
  else:
    return x

