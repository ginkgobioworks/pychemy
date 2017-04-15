import pybel


def convert_inchi_to_formula(inchi_string):
  """
  Converts InChI to formula. Depends on/uses openbabel.
  """
  return pybel.readstring('inchi', inchi_string).formula
