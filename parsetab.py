
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVnonassocUMINUSDIV LPAREN MINUS NUMBER PLUS RPAREN TIMESexpr : expr PLUS exprexpr : expr MINUS exprexpr : MINUS expr %prec UMINUSexpr : expr TIMES expr\n        | expr DIV exprexpr : NUMBERexpr : LPAREN expr RPAREN'
    
_lr_action_items = {'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,],[2,6,2,-6,2,2,2,2,2,-3,6,-1,-2,-4,-5,-7,]),'NUMBER':([0,2,4,5,6,7,8,],[3,3,3,3,3,3,3,]),'LPAREN':([0,2,4,5,6,7,8,],[4,4,4,4,4,4,4,]),'$end':([1,3,9,11,12,13,14,15,],[0,-6,-3,-1,-2,-4,-5,-7,]),'PLUS':([1,3,9,10,11,12,13,14,15,],[5,-6,-3,5,-1,-2,-4,-5,-7,]),'TIMES':([1,3,9,10,11,12,13,14,15,],[7,-6,-3,7,7,7,-4,-5,-7,]),'DIV':([1,3,9,10,11,12,13,14,15,],[8,-6,-3,8,8,8,-4,-5,-7,]),'RPAREN':([3,9,10,11,12,13,14,15,],[-6,-3,15,-1,-2,-4,-5,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,2,4,5,6,7,8,],[1,9,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr PLUS expr','expr',3,'p_add','plex_arithematic.py',49),
  ('expr -> expr MINUS expr','expr',3,'p_sub','plex_arithematic.py',53),
  ('expr -> MINUS expr','expr',2,'p_expr2uminus','plex_arithematic.py',57),
  ('expr -> expr TIMES expr','expr',3,'p_mult_div','plex_arithematic.py',61),
  ('expr -> expr DIV expr','expr',3,'p_mult_div','plex_arithematic.py',62),
  ('expr -> NUMBER','expr',1,'p_expr2NUM','plex_arithematic.py',71),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_parens','plex_arithematic.py',74),
]