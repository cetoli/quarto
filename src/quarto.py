"""
############################################################
Quarto - Principal
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.2
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from tabuleiro import Tabuleiro
from mao import Mao
from casa import Casa
class Quarto:
    """Base do jogo com tabuleiro e duas maos."""
    def __init__(self, gui):
        """Constroi a casa que indica a peca que foi selecionada. """
        self.casa = Casa(gui,self,99)
        
    def build_base(self,gui):
        """Constroi as partes do Jogo. """
        self.build_tabuleiro(gui)
        self.build_mao(gui)
        #gui.rect(x=10, y= 10, width=800, heigth=600)
    def build_tabuleiro(self,gui):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        self.tabuleiro =Tabuleiro(gui,self)
    def build_mao(self,gui):
        """Constroi os dois espacos onde as pecas se iniciam."""
        self.mao1 =Mao(gui,self,0)
        self.mao2 =Mao(gui,self,1)

def main(doc):
  print('Quarto 0.1.0')
  quarto =  Quarto(doc)
  quarto.build_base(doc)

