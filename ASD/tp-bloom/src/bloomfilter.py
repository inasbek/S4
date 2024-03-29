# -*- coding: utf-8 -*-

""":mod:`bloomfilter` module : Implements a bloomfilter.

:author: `FIL - Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2016, january

"""

def create (n,f,m):
    """
    Creates a new empty Bloom filter of size :math:`2^n`

    :param n: the log of the size of the filter
    :type n: int
    :param f: the hash function whose should take as input two 
              parameters: the value to be hashed and the number 
              of the subfunction used
    :type f: function(any,int)
    :param m: the number of functions provided by *f*
    :return: the new Bloom filter
    :rtype: dict
    """
    bloomfilter= dict()
    for i in range (2**n):
        bloomfilter[i]=False #Creates 2^n cells (size of the table) default value = False (empty)
    bloomfilter["function"]=f #Function used to creates hashcode
    bloomfilter["nb_function"]=m #Number of functions
    return bloomfilter

def add (bf, e):
    """
    Adds *e* to *bf*.

    :param bf: A Bloom filter
    :type bf: dict
    :param e: The element to be added
    :type e: Any
    """
    for i in range (0,bf["nb_function"]):
        cell_position = bf["function"](e,i) % (len(bf)-2) 
        bf[cell_position]=True

def contains (bf, e):
    """
    Returns True if *e* is in *bf*.

    :param bf: A Bloom filter
    :type bf: dict
    :param e: The element to be tested
    :type e: Any
    """
    for i in range (0,bf["nb_function"]):
        cell_position = bf["function"](e,i) % (len(bf)-2)
        if bf[cell_position] == False:
            return False
    return True


        
    
