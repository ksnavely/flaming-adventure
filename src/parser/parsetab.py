
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'u-g\x18\xd4*Z\xd7{a\xef\x14\xce\x98F\xd7'
    
_lr_action_items = {'SAY':([0,1,],[1,1,]),'STRING':([0,1,2,3,4,5,],[2,2,-3,5,5,-2,]),'$end':([2,3,4,5,],[-3,0,-1,-2,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,],[3,4,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> SAY expression','expression',2,'p_expression_say','hw_01.py',46),
  ('expression -> expression STRING','expression',2,'p_words_expression','hw_01.py',50),
  ('expression -> STRING','expression',1,'p_string_expression','hw_01.py',55),
]
