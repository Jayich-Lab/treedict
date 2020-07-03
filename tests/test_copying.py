#!/usr/bin/env python

# Copyright (c) 2009-2011, Hoyt Koepke (hoytak@gmail.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     - Neither the name 'treedict' nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY Hoyt Koepke ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Hoyt Koepke BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import random, unittest, collections
from treedict import TreeDict, getTree
import treedict
from copy import deepcopy, copy

from hashlib import md5
import random

from common import *

class TestCopying(unittest.TestCase):

    ############################################################
    # Copying the tree

    def testCopying_01(self):
        p1 = makeTDInstance('root')
        p1.a = 123

        p2 = copy(p1)

        self.assertTrue(p1 == p2)
        self.assertTrue(p1.hash() == p2.hash())
        
    def testCopying_01d(self):
        p1 = makeTDInstance('root')
        p1.a = 123

        p2 = deepcopy(p1)

        self.assertTrue(p1 == p2)
        self.assertTrue(p1.hash() == p2.hash())

    def testCopying_02_dangling(self):
        p1 = makeTDInstance('root')
        p1.a

        p2 = copy(p1)

        self.assertTrue(p1 == p2)
        self.assertTrue(p1.hash() == p2.hash())

    def testCopying_02d_dangling(self):
        p1 = makeTDInstance('root')
        p1.a

        p2 = deepcopy(p1)

        self.assertTrue(p1 == p2)
        self.assertTrue(p1.hash() == p2.hash())

    def testCopying_03_Dangling_AttributeError(self):
        
        p = makeTDInstance()

        def f():
            p.a.b.copy()

        self.assertRaises(AttributeError, f)

    def testCopying_04_dangling_AttributeError_correct_node(self):
        
        p = makeTDInstance()
        ae_msg = ''

        try:
            p.aduvulksjucmfiddkjdo.b.copy()
        except AttributeError as ae:
            ae_msg = str(ae)

        # Make sure it propegates up so the error message is sent from
        # the root dangling node.
        self.assertTrue('aduvulksjucmfiddkjdo' in ae_msg)


    def testCopying_05(self):
        
        p = makeTDInstance('root')
        b = p.makeBranch('b').copy()

        self.assertTrue(p.b.branchName() == 'b', p.b.branchName())
        self.assertTrue(b.branchName(add_tree_name = True) == 'b', b.branchName(add_tree_name = True))
        self.assertTrue(p.b.branchName(add_path = True, add_tree_name = True) == 'root.b',
                     p.b.branchName(add_path = True, add_tree_name = True))

    def testCopying_05b(self):
        
        p = makeTDInstance('root')
        b = copy(p.makeBranch('b'))

        self.assertTrue(p.b.branchName() == 'b', p.b.branchName())
        self.assertTrue(b.branchName(add_tree_name = True) == 'b', b.branchName(add_tree_name = True))
        self.assertTrue(p.b.branchName(add_path = True, add_tree_name = True) == 'root.b',
                     p.b.branchName(add_path = True, add_tree_name = True))

    def testCopying_05c(self):
        
        p = makeTDInstance('root')
        b = deepcopy(p.makeBranch('b'))

        self.assertTrue(p.b.branchName() == 'b', p.b.branchName())
        self.assertTrue(b.branchName(add_tree_name = True) == 'b', b.branchName(add_tree_name = True))
        self.assertTrue(p.b.branchName(add_path = True, add_tree_name = True) == 'root.b',
                     p.b.branchName(add_path = True, add_tree_name = True))

    def testCopying_05b_central_system(self):
        # This test constrains the central system to have the same
        # name system as regular trees (I was tempted to do it
        # otherwise to make the constraints of copied branches
        # easier.)

        p = getTree('tc_root')
        b = p.makeBranch('b').copy()
    
        self.assertTrue(b.branchName(add_tree_name = True) == 'b', b.branchName(add_tree_name = True))
        self.assertTrue(p.b.branchName(add_path = True, add_tree_name = True) == 'tc_root.b',
                     p.b.branchName(add_path = True, add_tree_name = True))

    def testCopying_05b_central_system(self):
        # This test constrains the central system to have the same
        # name system as regular trees (I was tempted to do it
        # otherwise to make the constraints of copied branches
        # easier.)

        p = getTree('tc_root')
        b = p.makeBranch('b').copy()
    
        self.assertTrue(b.branchName(add_tree_name = True) == 'b', b.branchName(add_tree_name = True))
        self.assertTrue(p.b.branchName(add_path = True, add_tree_name = True) == 'tc_root.b',
                     p.b.branchName(add_path = True, add_tree_name = True))

    def testCopying_05b_central_system(self):
        # This test constrains the central system to have the same
        # name system as regular trees (I was tempted to do it
        # otherwise to make the constraints of copied branches
        # easier.)

        p = getTree('tc_root')
        b = p.makeBranch('b').copy()
    
        self.assertTrue(b.branchName(add_tree_name = True) == 'b', b.branchName(add_tree_name = True))
        self.assertTrue(p.b.branchName(add_path = True, add_tree_name = True) == 'tc_root.b',
                     p.b.branchName(add_path = True, add_tree_name = True))

    def testCopying_06_setting_linked_branch_02_copy(self):
        p = makeTDInstance()

        p.a = p.defs.a1

        p.defs.a1.v = 1

        p2 = p.copy()

        p2.defs.a1.v = 2

        self.assertTrue(p.a.v == 1)
        self.assertTrue(p2.a.v == 2)

    def testCopying_06_setting_linked_branch_04_deepcopy_func(self):
        p = makeTDInstance()

        p.a = p.defs.a1

        p.defs.a1.v = 1

        p2 = deepcopy(p)  # only difference from above

        p2.defs.a1.v = 2

        self.assertTrue(p.a.v == 1)
        self.assertTrue(p2.a.v == 2)

    def testCopying_07_unfrozen(self):
        p = makeTDInstance()

        p.x = 1
        p.b.c.x = 2
        p.b.c.y = 1

        p.freeze()

        self.assertTrue(p.isFrozen())
        self.assertTrue(p.b.isFrozen())
        self.assertTrue(p.b.c.isFrozen())

        p2 = p.copy()

        self.assertTrue(not p2.isFrozen())
        self.assertTrue(not p2.b.isFrozen())
        self.assertTrue(not p2.b.c.isFrozen())
        
        p3 = copy(p)
        
        self.assertTrue(not p3.isFrozen())
        self.assertTrue(not p3.b.isFrozen())
        self.assertTrue(not p3.b.c.isFrozen())

    def testCopying_07a_Regression(self):

        p = makeTDInstance()

        p.a.b = [1,2,3,4,534]
        p.a.c = [1,22,534]
        p.b   = [1,2,3]

        p2 = makeTDInstance()

        p2.a.b = [1,2,3,4,534]
        p2.a.c = [1,22,534]
        p2.b   = [1,2,3]

        p3 = copy(p)
        
        self.assertTrue(p == p2)
        self.assertTrue(p == p3)

    def testCopying_07a_Regression_mutability_count_test(self):
        
        p = makeTDInstance()

        p.a.b = [1,2,3,4,534]
        p.a.c = [1,22,534]
        p.b   = [1,2,3]

        p2 = copy(p)

        self.assertTrue(p._numMutable() == p2._numMutable())
        self.assertTrue(p.a._numMutable() == p2.a._numMutable())

    def testCopying_07b_Regression_empty_branches(self):

        p = makeTDInstance()
        p.makeBranch("a")

        p2 = copy(p)
       
        self.assertTrue(p.a == p2.a)
        self.assertTrue(p.a.parentNode() is p)
        self.assertTrue(p2.a.parentNode() is p2)
        self.assertTrue(p.a is not p2.a)

    def testCopying_08_makeTDInstanceValues(self):

        p = makeTDInstance()

        ab = p.a.b = makeTDInstance()

        q = p.copy()

        self.assertTrue(p == q)
        self.assertTrue(p.a is not q.a)
        self.assertTrue(ab is q.a.b)

    def testCopying_09_LinkedValuesPreserved(self):

        p = makeTDInstance()
        p.a.x = 1
        p.al = p.a

        q = p.copy()

        self.assertTrue(p.a is not q.a)
        self.assertTrue(q.al is q.a)
        
    def testCopying_09_LinkedValuesPreserved(self):

        p = makeTDInstance()
        p.a.x = 1
        p.b = p.a

        q = p.copy()

        self.assertTrue(p.a is not q.a)
        self.assertTrue(q.b is q.a)

    def testCopying_09_LinkedValuesPreserved_Reversed(self):

        p = makeTDInstance()
        p.b.x = 1
        p.a = p.b

        q = p.copy()

        self.assertTrue(p.b is not q.b)
        self.assertTrue(q.b is q.a)

    def testCopying_09_LinkedValuesPreserved(self):

        p = makeTDInstance()
        p.a.x = 1
        p.b = p.a

        q = p.copy()

        self.assertTrue(p.a is not q.a)
        self.assertTrue(q.b is q.a)

    def testCopying_10_Cousins(self):

        p = makeTDInstance()
        p.a.c.x = 1
        p.b.c = p.a.c

        q = p.copy()

        self.assertTrue(p.a is not q.a)
        self.assertTrue(p.a.c is not q.a.c)
        self.assertTrue(q.b.c is q.a.c)

    def testCopying_10_Cousins_subcopy(self):

        p = makeTDInstance()
        p.a.c.x = 1
        p.b.c = p.a.c
        p.b.d.x = 1

        qb = p.b.copy()

        self.assertTrue(qb.c.rootNode() is p)
        self.assertTrue(qb.d.rootNode() is qb)
        self.assertTrue(qb.d.x == 1)

    def testCopying_11_Cousins_multiple_copy(self):
        p = random_selflinked_tree(0, 4)
        # print "\np_before = "
        # print p.makeReport()

        q = p.copy()

        # print "\np = "
        # print p.makeReport()

        # print "\nq = "
        # print q.makeReport()

        self.assertTrue(q == p)

    def testCopying_12_Large_straight(self):
        p = random_selflinked_tree(0, 100)

        q = p.copy()

        for k, v in p.iteritems(branch_mode='all', recursive = True):

            if type(v) is makeTDInstance:

                pbn = p[k].branchName(add_path = True)
                qbn = q[k].branchName(add_path = True)

                self.assertTrue(pbn == qbn, "qbn = %s != %s = pbn" % (qbn, pbn))

                self.assertTrue(p[k] is not q[k])
                self.assertTrue(p[k] == q[k])

    def testCopying_13_Large_interwoven(self):
        p = random_selflinked_tree(0, 100)

        for bk, b in p.iteritems(recursive = False, branch_mode = 'only'):

            q = b.copy()

            # print "#"*40

            # print "\nbk = %s; b = " % bk
            # print b.makeReport()

            # print "\nbk = %s q = " % bk
            # print q.makeReport()

            for k, v in b.iteritems(branch_mode='all', recursive = True):

                if type(v) is makeTDInstance:

                    pbn = v.branchName(add_path = True)
                    qbn = q[k].branchName(add_path = True)

                    if q[k].rootNode() is not q:
                        self.assertTrue(q[k].rootNode() is p)
                        self.assertTrue(q[k] is v)
                    else:
                        self.assertTrue(v is not q[k])
                        self.assertTrue(pbn == bk + '.' + qbn, "pbn='%s' != '%s' = bk+qbn" % (pbn, bk+'.' + qbn))

    # Also need tests covering cases where flags are cleared on copied
    # nodes

    # Also need to add tests for copying with links and that the
    # proper link-parental relations are preserved in copying.

if __name__ == '__main__':
    unittest.main()

