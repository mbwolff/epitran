#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
import _epitran


class TestTurkish(unittest.TestCase):
    def setUp(self):
        self.epi = _epitran.Epitran(u'tur-Latn')

    def test_transliterate1(self):
        self.assertEqual(self.epi.transliterate(u'Haziran\'da'), u'haziɾan\'da')
        self.assertEqual(self.epi.transliterate(u'Hazeran’da'), u'hazeɾan’da')
        self.assertEqual(self.epi.transliterate(u'otoparkın'), u'otopaɾkɯn')

    def test_transliterate2(self):
        self.assertEqual(self.epi.transliterate(u'"'), u'"')
        self.assertEqual(self.epi.transliterate(u'\''), u'\'')
        self.assertEqual(self.epi.transliterate(u'’'), u'’')
        self.assertEqual(self.epi.transliterate(u'‘'), u'‘')

    def test_transliterate_norm_punc1(self):
        self.assertEqual(self.epi.transliterate(u'Haziran\'da', normpunc=True), u'haziɾan\'da')
        self.assertEqual(self.epi.transliterate(u'Hazeran’da', normpunc=True), u'hazeɾan\'da')
        self.assertEqual(self.epi.transliterate(u'otoparkın', normpunc=True), u'otopaɾkɯn')

    def test_transliterate_norm_punc2(self):
        self.assertEqual(self.epi.transliterate(u'"', normpunc=True), u'"')
        self.assertEqual(self.epi.transliterate(u'\'', normpunc=True), u'\'')
        self.assertEqual(self.epi.transliterate(u'’', normpunc=True), u'\'')
        self.assertEqual(self.epi.transliterate(u'‘', normpunc=True), u'\'')

    def test_robust_trans_pairs(self):
        self.assertEqual(self.epi.robust_trans_pairs(u'’'), [(u'’', u'')])
        self.assertEqual(self.epi.robust_trans_pairs(u'du’da'), [(u'd', u'd'), (u'u', u'u'), (u'’', u''), (u'd', u'd'), (u'a', u'a')])

    def test_case_cat_graph_phon_tuples_cat(self):
        self.assertEqual(self.epi.case_cat_graph_phon_tuples(u'\'')[0][1], u'P')
        self.assertEqual(self.epi.case_cat_graph_phon_tuples(u'’')[0][1], u'P')
        self.assertEqual(self.epi.case_cat_graph_phon_tuples(u'‘')[0][1], u'P')
        self.assertEqual(self.epi.case_cat_graph_phon_tuples(u' ')[0][1], u'Z')
        self.assertEqual(self.epi.case_cat_graph_phon_tuples(u'Buluk')[0][1], u'L')

    def test_word_to_pfvector(self):
        self.assertEqual(self.epi.word_to_pfvector(u'’')[0][:2], (u'P', 0))
        self.assertEqual(self.epi.word_to_pfvector(u'‘')[0][:2], (u'P', 0))
        self.assertEqual(self.epi.word_to_pfvector(u'Hazeran’da')[7][:2], (u'P', 0))
