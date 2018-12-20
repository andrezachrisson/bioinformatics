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
from subprocess import Popen, PIPE, run
import os
import re
from shutil import copyfile
import time
import csv

def fastPhylo(normal_file, tempdir):
        """ Reduced noise tree"""
        with open(tempdir+'/red_fast', 'w') as file: #open in tempdir
            run(['fastprot','reduced_file'], stdin=PIPE, stdout=file, stderr=PIPE, encoding = 'utf8', cwd=tempdir) #cdw = tempdir

            # file.write(process.stdout.read())

        with open(tempdir+'/red_tree', 'w') as file:  #open in tempdir
            run(['fnj','red_fast', '-O', 'newick'], stdin=PIPE, stdout=file, stderr=PIPE, encoding = 'utf8', cwd=tempdir) #cdw = tempdir
            # file.write(process.stdout.read())

        """ Normal tree"""
        with open(tempdir+'/normal_fast', 'w') as file:  #open in tempdir
            run(['fastprot', normal_file], stdin=PIPE, stdout=file, stderr=PIPE, encoding = 'utf8')
            # file.write(process.stdout.read())

        with open(tempdir+'/normal_tree', 'w') as file: #open in tempdir
            run(['fnj','normal_fast', '-O', 'newick'], stdin=PIPE, stdout=file, stderr=PIPE, encoding = 'utf8', cwd=tempdir) #cdw = tempdir
            # file.write(process.stdout.read())
        return tree_compare (tempdir)

def tree_compare(tempdir):
        # CHANGE to tempdir
        tns = dendropy.TaxonNamespace()
        tree1 = Tree.get_from_path(
                tempdir+"/ref.tree",
                "newick",
                taxon_namespace=tns)
        tree2 = Tree.get_from_path(
                tempdir+"/normal_tree",
                "newick",
                taxon_namespace=tns)
        tree3 = Tree.get_from_path(
                tempdir+"/red_tree",
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
        os.chdir(data)
        with tempfile.TemporaryDirectory(dir = data) as tempdir:
            for filename in os.listdir(data):
                if os.path.isfile(filename):
                    #print(filename[0])
                    if filename[0] != '.':
                        if re.search(r'tree', filename):
                            copyfile(filename,tempdir+'/ref.tree')
                            statistics =[(filename,filename+'_reduced')]
                            break


            for filename in os.listdir(data):
                if os.path.isfile(filename):
                    if filename[0] != '.' and not re.search(r'tree', filename):
                            if read_file(filename, tempdir):
                                statistics.append(fastPhylo(filename, tempdir))
                            else:
                                pass
        all_testdata.append(statistics)
    os.chdir(dirpath)
    with open('results.csv','w') as f:
        for row in all_testdata:
            writer = csv.writer(f)
            writer.writerows(row)

if __name__ == '__main__':
    main()
