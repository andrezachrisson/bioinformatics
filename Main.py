""" Own functions """
from read_clean import *

""" Modules """
from Bio import SeqIO
from Bio.Seq import Seq
import pdb
from dendropy.calculate import treecompare
import dendropy
from dendropy import Tree
import tempfile
from subprocess import Popen, PIPE
import os


def main():
    read_file('s001.align.1.msl')

    tns = dendropy.TaxonNamespace()
    tree1 = Tree.get_from_path(
            "ref.tree",
            "newick",
            taxon_namespace=tns)
    tree2 = Tree.get_from_path(
            "normal_tree",
            "newick",
            taxon_namespace=tns)
    tree1.encode_bipartitions()
    tree2.encode_bipartitions()
    print(treecompare.symmetric_difference(tree1, tree2))

    dirpath = os.path.dirname(os.path.realpath(__file__))
    print(dirpath)
    with tempfile.NamedTemporaryFile(dir = dirpath) as tempdir:






if __name__ == '__main__':
    main()
