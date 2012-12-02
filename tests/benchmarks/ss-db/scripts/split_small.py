#!/usr/bin/python
# BEGIN_COPYRIGHT
#
# This file is part of SciDB.
# Copyright (C) 2008-2011 SciDB, Inc.
#
# SciDB is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SciDB is distributed "AS-IS" AND WITHOUT ANY WARRANTY OF ANY KIND,
# INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY,
# NON-INFRINGEMENT, OR FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for the complete license terms.
#
# You should have received a copy of the GNU General Public License
# along with SciDB.  If not, see <http://www.gnu.org/licenses/>.
# END_COPYRIGHT
#
import csv
import time
import os
import subprocess
import sys
import traceback
sys.path.append(os.getcwd()) # NOCHECKIN 
sys.path.append('/opt/scidb/12.3/lib')
import scidbapi as scidb


# Start the single instance server. 

def handleException(inst, exitWhenDone, op=None):
    traceback.print_exc()
    if op:
        print >> sys.stderr, "Exception while ", op
    print >> sys.stderr, "     Exception Type: %s" % type(inst)     # the exception instance
    print >> sys.stderr, "     Exception Value: %r" % inst 
    print >> sys.stderr, ""
    if(exitWhenDone):
        exit(2)

def main():
    size=3750
    db = scidb.connect("localhost", 1239)
    pos=[(496559,501159,0),(497861,496211,1),(663581,400678,2),(500464,498815,3),(495516,500117,4),(496818,495169,5),(498120,496471,6),(705023,442119,7),(500724,499075,8),(495776,500377,9),(497078,495429,10),(538927,276023,11),(499682,498033,12),(500984,499335,13),(496036,500637,14),(497338,495689,15),(580369,317465,16),(499942,498293,17),(501244,499595,18),(496296,500897,19),(497598,495949,20),(621811,358907,21),(500202,498553,22),(495254,499855,23),(496556,501157,24),(497858,496209,25),(663252,400349,26),(500462,498813,27),(495514,500115,28),(496816,495167,29),(498118,496469,30),(704694,441790,31),(500722,499073,32),(495774,500375,33),(497076,495427,34),(538598,275694,35),(499680,498031,36),(500982,499333,37),(496034,500635,38),(497336,495687,39),(580040,317136,40),(499940,498291,41),(501242,499593,42),(496294,500895,43),(497596,495947,44),(621481,358578,45),(500200,498551,46),(495252,499853,47),(496554,501155,48),(497856,496207,49),(662923,400019,50),(500460,498811,51),(495512,500113,52),(496814,495165,53),(498116,496467,54),(704365,441461,55),(500720,499071,56),(495772,500373,57),(497074,495425,58),(538269,275365,59),(499678,498029,60),(500980,499331,61),(496032,500633,62),(497334,495685,63),(579711,316807,64),(499938,498289,65),(501240,499591,66),(496292,500893,67),(497594,495945,68),(621152,358248,69),(500198,498549,70),(495250,499851,71),(496552,501153,72),(497854,496205,73),(662594,399690,74),(500458,498809,75),(495510,500111,76),(496812,495163,77),(498114,496465,78),(704036,441132,79),(496559,501159,80),(497861,496211,81),(663581,400678,82),(500464,498815,83),(495516,500117,84),(496818,495169,85),(498120,496471,86),(705023,442119,87),(500724,499075,88),(495776,500377,89),(497078,495429,90),(538927,276023,91),(499682,498033,92),(500984,499335,93),(496036,500637,94),(497338,495689,95),(580369,317465,96),(499942,498293,97),(501244,499595,98),(496296,500897,99),(497598,495949,100),(621811,358907,101),(500202,498553,102),(495254,499855,103),(496556,501157,104),(497858,496209,105),(663252,400349,106),(500462,498813,107),(495514,500115,108),(496816,495167,109),(498118,496469,110),(704694,441790,111),(500722,499073,112),(495774,500375,113),(497076,495427,114),(538598,275694,115),(499680,498031,116),(500982,499333,117),(496034,500635,118),(497336,495687,119),(580040,317136,120),(499940,498291,121),(501242,499593,122),(496294,500895,123),(497596,495947,124),(621481,358578,125),(500200,498551,126),(495252,499853,127),(496554,501155,128),(497856,496207,129),(662923,400019,130),(500460,498811,131),(495512,500113,132),(496814,495165,133),(498116,496467,134),(704365,441461,135),(500720,499071,136),(495772,500373,137),(497074,495425,138),(538269,275365,139),(499678,498029,140),(500980,499331,141),(496032,500633,142),(497334,495685,143),(579711,316807,144),(499938,498289,145),(501240,499591,146),(496292,500893,147),(497594,495945,148),(621152,358248,149),(500198,498549,150),(495250,499851,151),(496552,501153,152),(497854,496205,153),(662594,399690,154),(500458,498809,155),(495510,500111,156),(496812,495163,157),(498114,496465,158),(704036,441132,159)]
    for x,y,z in pos:
	query="store(reshape(slice(small_obs,Z,%d),<oid:int64 NULL,center:bool NULL,polygon:int32 NULL,sumPixel:int64 NULL,avgDist:double NULL,point:bool NULL>[J=%d:%d,%d,0,I=%d:%d,%d,0]),small_obs_%d)" %(z,x,x+size-1,size,y,y+size-1,size,z)    
	print query
    	result=db.executeQuery(query,"afl")
        db.completeQuery(result.queryID)
	if(z==19):
		break
    db.disconnect()     #Disconnect from the SciDB server. 

    print "Done!"
    sys.exit(0) #success
if __name__ == "__main__":
    main()