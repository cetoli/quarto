"""
############################################################
Quarto - Casa
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
class A:
    def __init__(self):
        self.c =2
        class B:
            def go(inner):
                print (self.c)
        self.b = B()
    def go(self):
        self.b.go()
        

        
        
a=A()
a.go()
class Casa:
    """Casa onde se coloca pecas"""
    def __init__(self, gui, local, name):
        "local onde nasce, o nome da casa"
        class CasaVazia(object):
            """Estado que representa a casa vazia."""
            def recebe(s, peca):
                "esta casa recebe peca quando esta vazia"
                self.peca = peca
                self.peca.move(self)
                self._estado_corrente = self._casa_cheia
            def entrega(s, casa):
                "vazia nao entrega a peca pedida"
                pass

        class CasaCheia(object):
            """Estado que representa a casa cheia."""
            def recebe(s, peca):
                "esta casa nao recebe peca quando esta cheia"
                pass
            def entrega(s, casa):
                "entrega a peca pedida, que sai daqui"
                casa.recebe(self.peca)
                self._estado_corrente = self._casa_vazia
        
        self.gui, self.local, self.name = gui, local, name
        self.peca = None
        self._estado_corrente = self._casa_vazia = CasaVazia()
        self._casa_cheia = CasaCheia()
    def escolhida(self):
        "remove peca da base e poe aqui"
        self.local.casa.entrega(self)
    def recebe(self, peca):
        "esta casa recebe peca quando esta vazia"
        self._estado_corrente.recebe(peca)
    def entrega(self, casa):
        "entrega a peca pedida, que sai daqui"
        self._estado_corrente.entrega(casa)
    def sai(self, peca):
        "a peca escolhida sai daqui"
        self.peca = None
        self._estado_corrente = self._casa_vazia
