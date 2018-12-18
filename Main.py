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
from shutil import copyfile

def fastPhylo(normal_file):
        """ Reduced noise tree"""
        with open('red_fast', 'w') as file: #open in tempdir
            process = Popen(['fastprot','reduced_file'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8') #cdw = tempdir
            file.write(process.stdout.read())

        with open('red_tree', 'w') as file:  #open in tempdir
            process = Popen(['fnj','red_fast', '-O', 'newick'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8') #cdw = tempdir
            file.write(process.stdout.read())

        """ Normal tree"""
        with open('normal_fast', 'w') as file:  #open in tempdir
            process = Popen(['fastprot', normal_file], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8')
            file.write(process.stdout.read())

        with open('normal_tree', 'w') as file: #open in tempdir
            process = Popen(['fnj','normal_fast', '-O', 'newick'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding = 'utf8') #cdw = tempdir
            file.write(process.stdout.read())
        return tree_compare ()

def tree_compare():
        # CHANGE to tempdir
        tns = dendropy.TaxonNamespace()
        tree1 = Tree.get_from_path(
                "ref.tree",
                "newick",
                taxon_namespace=tns)
        tree2 = Tree.get_from_path(
                "normal_tree",
                "newick",
                taxon_namespace=tns)
        tree3 = Tree.get_from_path(
                "red_tree",
                "newick",
                taxon_namespace=tns)
        tree1.encode_bipartitions()
        tree2.encode_bipartitions()
        tree3.encode_bipartitions()
        distance_normal = treecompare.symmetric_difference(tree1, tree2)
        distance_reduced = treecompare.symmetric_difference(tree1, tree3)
        return distance_normal, distance_reduced

def main():
    dirpath = os.path.dirname(os.path.realpath(__file__))
    directory = dirpath + '/TEST_DATA'
    all_testdata =[]
    for data in os.listdir(directory):

        data = directory +'/' + data
        with tempfile.TemporaryDirectory(dir = dirpath) as tempdir:
            os.chdir(tempdir)
            for filename in os.listdir(data):
                #print(filename[0])
                if filename[0] != '.':
                    if re.search(r'tree', filename):
                        copyfile(data+'/'+filename,'ref.tree')
                        print(filename)
                        statistics =[filename]
                        break


            for filename in os.listdir(data):
                if filename[0] != '.' and not re.search(r'tree', filename):
                        copyfile(data+'/'+filename,filename)
                        if read_file(filename, tempdir):
                            statistics.append(fastPhylo(filename))
                        else:
                            pass
        print(statistics)
        all_testdata.append(statistics)

if __name__ == '__main__':
    main()
