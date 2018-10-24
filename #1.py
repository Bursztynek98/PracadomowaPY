# python/py
"""
#1 pracadomowa z programowawnia python.

Obiekty klasy.
machine <- PC <- NFS
      /\<- Xbox <- forza
      /\<- Mobile <- tetris
"""


class machine():
    pass


class PC(machine):
    pass


class Xbox(machine):
    pass


class Mobile(machine):
    pass


class tetris(Mobile):
    pass


class forza(Xbox):
    pass


class NFS(PC):
    pass
