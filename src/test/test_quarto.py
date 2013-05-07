#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Quarto - Teste
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
import unittest
from quarto import Quarto

class TestQuarto(unittest.TestCase):

    def setUp(self):
        class Gui(object):
            pass
            def __getitem__(self, x):
                return self
           
        
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


if __name__ == '__main__':
    unittest.main()