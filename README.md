```python
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
