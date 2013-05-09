#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Quarto - Teste
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/08
:Status: This is a "work in progress"
:Revision: 0.1.2
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
import unittest
from quarto import Quarto
import peca
peca.bw_a = lambda a, b: a & b
peca.bw_na = lambda a, b: ~a & b

class TestQuarto(unittest.TestCase):

    def setUp(self):
        class Gui(object):
            pass
            def __getitem__(self, x):
                return self
           
            def setAttribute(self, *x):
                self.opacity = 0.5
       
        self.gui = Gui()
        self.gui.onclick = object()
        self.app = Quarto(self.gui)

    def test_tabuleiro(self):
        "garante que tem casas no tabuleiro."
        self.app.build_tabuleiro(self.gui)
        t = self.app.tabuleiro
        self.assertEqual(len(t.casas),16)
    def test_mao(self):
        "garante que tem pecas na mao."
        self.app.build_mao(self.gui)
        m = self.app.mao1
        self.assertEqual(len(m.pecas),8)
    def test_outra_mao(self):
        "garante que tem casas na outra mao."
        self.app.build_mao(self.gui)
        m = self.app.mao2
        self.assertEqual(len(m.pecas),8)
    def test_escolhe_peca(self):
        "peca sai da mao e vai para a base."
        self.app.build_base(self.gui)
        m = self.app.mao2
        #: a peca inicia na mao
        p = m.pecas[0]
        self.assertEqual(p.local,m)
        #: a peca escolhida vai para a casa
        p.escolhida()
        self.assertEqual(p.local,self.app.casa)
        self.assertEqual(len(m.pecas),7)
    def test_nao_pode_escolher__outra_peca(self):
        "nao pode escolher outra peca, peca fica na mao."
        self.app.build_base(self.gui)
        #: a peca inicia na mao
        p = self.app.mao1.pecas[0]
        #: a peca escolhida vai para a casa
        p.escolhida()
        #: uma segunda peca nao pode ser escolhida
        q = self.app.mao1.pecas[1]
        q.escolhida()
        self.assertEqual(q.local,self.app.mao1)
    def test_escolhe_casa(self):
        "peca sai da base e vai para a casa."
        self.app.build_base(self.gui)
        m = self.app.mao2
        t = self.app.tabuleiro
        #: a peca inicia na mao
        p = m.pecas[0]
         #: a peca escolhida vai para a casa
        p.escolhida()
        c = t.casas[0]
        c.escolhida()
        self.assertEquals(p.local,c)
        self.assertEquals(self.app.casa.peca,None)
    def test_escolhe_peca_na_casa(self):
        "peca permanece na casa quando escolhida no tabuleiro."
        self.app.build_base(self.gui)
        m = self.app.mao2
        t = self.app.tabuleiro
        #: a peca inicia na mao
        p = m.pecas[0]
         #: a peca escolhida vai para a casa
        p.escolhida()
        c = t.casas[0]
        c.escolhida()
         #: a peca escolhida fica na casa
        p.escolhida()
        self.assertEquals(p.local,c)
        self.assertEquals(self.app.casa.peca,None)
    def test_escolhe_casa_sem_peca_selecionada(self):
        "nada acontece, nenhuma peca pode ser movida para a casa."
        self.app.build_base(self.gui)
        m = self.app.mao2
        t = self.app.tabuleiro
        c = t.casas[0]
        c.escolhida()
        self.assertEquals(c.peca,None)
    def test_verifica_combinacao_de_pecas(self):
        "retorna verdadeiro se as pecas combinam."
        self.app.build_base(self.gui)
        m = self.app.mao2
        p = m.pecas[0]
        self.assertTrue(p.combina(m.pecas))
        n = self.app.mao1
        p = n.pecas[0]
        nc = n.pecas[0:2]+m.pecas[6:8]
        self.assertFalse(p.combina(nc), 'nao combina %s %s'%(
            [i.name for i in nc], p.rodada))
        self.assertTrue(p.combina(n.pecas))
        self.assertTrue(p.combina([i for i in n.pecas if i.name%2]))
        self.assertTrue(p.combina([i for i in n.pecas if not i.name%2]))
    def test_verifica_combinacao_vencedora(self):
        "indica nas pecas e na casa base que houve uma combinacao vencedora."
        self.app.build_base(self.gui)
        pecas = self.app.mao2.pecas[0:5]
        casas = self.app.tabuleiro.casas[0:4]
        p = pecas[-1]
        self.assertEquals(self.app.casa.peca,None)
        #__ = [casa.recebe(peca) for casa, peca in zip(casas,pecas)]
        __ = [peca.escolhida() or casa.escolhida() for casa, peca in zip(casas,pecas)]
        print(self.app.casa)
        self.assertEquals(self.app.casa._estado_corrente,self.app.casa._casa_morta)
        p.escolhida()
        self.assertEquals(p.local,self.app.mao2)
        self.assertEquals(p._estado_peca,p._estado_pode_posicionar)
        self.assertEquals(self.gui.opacity,0.5)
        self.assertEquals(self.app.casa.peca,None)
        



if __name__ == '__main__':
    unittest.main()