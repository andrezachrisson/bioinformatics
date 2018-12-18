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
import re

def fastPhylo(tempdir):
        os.chdir(tempdir)

        """ Reduced noise tree"""
        with open('red_fast', 'w') as file:
            process = Popen(['fastprot','reduced_file'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8', cwd = tempdir)
            file.write(process.stdout.read())

        with open('red_tree', 'w') as file:
            process = Popen(['fnj','red_fast', '-O', 'newick'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8', cwd = tempdir)
            file.write(process.stdout.read())

        """ Normal tree"""
        with open('normal_fast', 'w') as file:
            process = Popen(['fastprot','s001.align.1.msl'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8', cwd = tempdir)
            file.write(process.stdout.read())

        with open('normal_tree', 'w') as file:
            process = Popen(['fnj','normal_fast', '-O', 'newick'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8', cwd = tempdir)
            file.write(process.stdout.read())
        pdb.set_trace()

        tree_compare (tempdir)

def tree_compare(tempdir):
        tns = dendropy.TaxonNamespace()
        os.chdir('/home/andre/Documents/Bioinformatics/bioinformatics')
        tree1 = Tree.get_from_path(
                "ref.tree",
                "newick",
                taxon_namespace=tns)
        tree2 = Tree.get_from_path(
                tempdir + "/"+ "normal_tree",
                "newick",
                taxon_namespace=tns)
        tree3 = Tree.get_from_path(
                tempdir + "/"+ "red_tree",
                "newick",
                taxon_namespace=tns)
        tree1.encode_bipartitions()
        tree2.encode_bipartitions()
        print(treecompare.symmetric_difference(tree1, tree2))
        print(treecompare.symmetric_difference(tree1, tree3))
        print(" ")

def main():
    dirpath = os.path.dirname(os.path.realpath(__file__))
    with tempfile.TemporaryDirectory(dir = dirpath) as tempdir:
        directory = dirpath + '/TEST_DATA/asymmetric_2.0'
        os.chdir(tempdir)
        for filename in os.listdir(directory):
            if filename[0] != '.':
                if re.search('tree', filename):
                    copyfile(filename,'ref.tree')
                    break
        pdb.set_trace()

        for filename in os.listdir(directory):
            if filename[0] != '.':
                    copyfile(filename,filename)
                    read_file(filename, tempdir)
                    fastPhylo(tempdir)




if __name__ == '__main__':
    main()
