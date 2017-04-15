from __future__ import print_function

import unittest
from six.moves import range

from pychemy.chem_structure import chem_structure
from pychemy.chem_structure import chem_graph
from pychemy.elements import ELEMENTS

# flake8: noqa E241


inchi1 = 'InChI=1/C5H5N5O/c6-5-9-3-2(4(11)10-5)7-1-8-3/h1H,(H4,6,7,8,9,10,11)/f/h8,10H,6H2'
inchi2 = 'InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3,(H,11,12)' # Aspirine


class ChemStructureTestCase(unittest.TestCase):

  def assertStringEqual(self, lhs, rhs):
    return self.assertEqual(str(lhs), str(rhs))


  def test_chem_structure_without_input(self):
    cs = chem_structure()
    self.assertEqual(cs.inchi, None)

  def test_chem_structure_with_inchi_input(self):
    cs = chem_structure(inchi=inchi1)
    self.assertEqual(cs.inchi, inchi1)
    self.assertEqual(cs.mol.NumAtoms(), 16)
    self.assertEqual(cs.mol.NumBonds(), 17)

  def test_graph_from_OBMol(self):
    cs = chem_structure(inchi=inchi1)
    graph = chem_graph.graph_from_OBMol(cs.mol)

    self.assertStringEqual(graph.number_of_nodes(), 16)
    self.assertStringEqual(graph.node[1]['atom'], ELEMENTS['C'])
    self.assertStringEqual(graph.node[2]['atom'], ELEMENTS['C'])
    self.assertStringEqual(graph.node[3]['atom'], ELEMENTS['C'])
    self.assertStringEqual(graph.node[4]['atom'], ELEMENTS['C'])
    self.assertStringEqual(graph.node[5]['atom'], ELEMENTS['C'])
    self.assertStringEqual(graph.node[6]['atom'], ELEMENTS['N'])
    self.assertStringEqual(graph.node[7]['atom'], ELEMENTS['N'])
    self.assertStringEqual(graph.node[8]['atom'], ELEMENTS['N'])
    self.assertStringEqual(graph.node[9]['atom'], ELEMENTS['N'])
    self.assertStringEqual(graph.node[10]['atom'], ELEMENTS['N'])
    self.assertStringEqual(graph.node[11]['atom'], ELEMENTS['O'])
    self.assertStringEqual(graph.node[12]['atom'], ELEMENTS['H'])
    self.assertStringEqual(graph.node[13]['atom'], ELEMENTS['H'])
    self.assertStringEqual(graph.node[14]['atom'], ELEMENTS['H'])
    self.assertStringEqual(graph.node[15]['atom'], ELEMENTS['H'])
    self.assertStringEqual(graph.node[16]['atom'], ELEMENTS['H'])

    for n in range(1, 17):
      self.assertTrue('X' in graph.node[n])
      self.assertTrue('Y' in graph.node[n])

    for edge in graph.edges():
      self.assertTrue('order' in graph[edge[0]][edge[1]])

    self.assertEqual(graph.number_of_edges(), 17)
    edge_set = [(1, 12), (12,  1),
                (1,  7),  (7,  1),
                (1,  8),  (8,  1),
                (2,  7),  (7,  2),
                (3,  8),  (8,  3),
                (2,  3),  (3,  2),
                (2,  4),  (4,  2),
                (4, 11), (11,  4),
                (4, 10), (10,  4),
               (10, 16), (16, 10),
                (5, 10), (10,  5),
                (5,  6),  (6,  5),
                (5,  9),  (9,  5),
                (3,  9),  (9,  3),
                (8, 15), (15,  8),
                (6, 13), (13,  6),
                (6, 14), (14,  6)]

    for edge in graph.edges():
      self.assertIn(edge, edge_set)
      edge_set.remove(edge)
      edge_set.remove((edge[1], edge[0]))

    self.assertEqual(edge_set, [])

  def test_chem_graph_with_empty_input(self):
    cg = chem_graph()
    self.assertEqual(cg.G.number_of_nodes(), 0)

  def test_chem_graph_from_OBMol(self):
    cs = chem_structure(inchi=inchi1)
    cg = chem_graph(cs.mol)
    self.assertEqual(cg.G.number_of_nodes(), 16)
    self.assertEqual(cg.G.number_of_edges(), 17)

  def test_chem_formula(self):
    cs = chem_structure(inchi=inchi1)
    cg = chem_graph(cs.mol)
    self.assertEqual(cg.chem_formula(), cs.chem_formula())

  def test_mass(self):
    cs = chem_structure(inchi=inchi1)
    cg = chem_graph(cs.mol)
    self.assertTrue(abs(cg.mass() - cs.mass()) / cg.mass() < 0.001)

  def test_gen_frag_with_no_additional_steps(self):
    cs = chem_structure(inchi=inchi1)
    cg = chem_graph(cs.mol)
    self.assertEqual(cg.gen_frag(0), [cg])

  def test_gen_frag_has_no_empty_molecules(self):
    cs = chem_structure(inchi=inchi1)
    cg = chem_graph(cs.mol)
    for level in range(0, 4):
      frag = cg.gen_frag(level)
      nonempty_frag = [f for f in frag if len(f.chem_formula()) > 0]
      self.assertEqual(frag, nonempty_frag)

  def test_gen_frag_with_additional_steps_uniqueness(self):
    cs = chem_structure(inchi=inchi1)
    cg = chem_graph(cs.mol)
    for level in range(1, 4):
      frag = cg.gen_frag(level)
      self.assertEqual(len(frag), len(set(frag)))
