"""
############################################################
Quarto - Mao
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/02
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from peca import Peca
class Mao:
    """Espaco do jogo onde as pecas iniciam. """
    def __init__(self, gui, local, name = 0):
        " colecao de pecas vazias"
        self.gui, self.local, self.name = gui, local, name
        self.pecas = []
        self.build(gui)
    @property
    def casa(self):
        "retorna a casa da base"
        return self.local.casa
        
    def build(self, gui):
        "monta as pecas a serem escolhidas. "
        self.pecas = [Peca(gui,self,i + self.name*8) for i in range(8)]
    def _escolhida(self, peca):
        "a peca escolhida move para a casa da base"
        self.local.escolhida(peca)
    def sai(self, peca):
        "a peca escolhida sai daqui"
        self.pecas.remove(peca)
