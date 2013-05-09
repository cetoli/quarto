"""
############################################################
Quarto - Tabuleiro
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/08
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from casa import Casa
class Tabuleiro:
    """Campo do jogo onde se joga as pecas"""
    def __init__(self, gui, local):
        self.local = local
        self.casas = []
        self.build(gui)
        self.build_crivo()
    def build(self, gui):
        " Constroi uma colecao de dezesseis casas"
        self.casas = [Casa(gui, self, i).build() for i in range(16)]
    def build_crivo(self):
        " Constroi um crivo para detectar a solucao do game"
        self.crivo = [ [key for key in range(16) if key//4 == key%4]
            ,[key for key in range(16) if key//4 == 3-key%4]
        ]
        self.crivo += [ [key for key in range(16) if key//4 == row]
            for row in range(4)]
        self.crivo += [ [key for key in range(16) if key%4 == row] 
            for row in range(4)]
    @property
    def casa(self):
        "retorna a casa da base"
        return self.local.casa
    def venceu(self):
        "trava a casa de selecao colocando ela no estado morta."
        print('venceu tabuleiro',self.local.casa)
        self.local.casa.morta()
    def recebe(self, esta_peca):
        "verifica se esta peca e vencedora"
        def _a_combinacao_eh_vencedora(conf, a_peca):
            comb = [self.casas[key].peca for key in conf if self.casas[key].peca]
            return len(comb) == 4 and a_peca.combina(comb)
        
        _vencedora = [conf for conf in self.crivo
                      if _a_combinacao_eh_vencedora(conf, esta_peca)]
        for conf in _vencedora:
            self.venceu()
            _casas = [self.casas[casa].venceu() for casa in conf]
        
