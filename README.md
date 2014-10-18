```
riley@rileydotbiz:~/code/bencode-py (master)$ ipython
Python 2.7.5 (default, Mar  9 2014, 22:15:05)
Type "copyright", "credits" or "license" for more information.

IPython 1.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import bencode

In [2]: bencode.encode({
   ...:     'name': 'Riley',
   ...:     'ages': [26, 27],
   ...:     'parent': {
   ...:         'name': 'Scott',
   ...:     },
   ...: })
Out[2]: 'd4:agesli26ei27ee4:name5:Riley6:parentd4:name5:Scottee'

In [3]: bencode.decode('d4:agesli26ei27ee4:name5:Riley6:parentd4:name5:Scottee')
Out[3]: {'ages': [26, 27], 'name': 'Riley', 'parent': {'name': 'Scott'}}
```
