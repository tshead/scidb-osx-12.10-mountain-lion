########################################
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
#
# END_COPYRIGHT
########################################
#set(generator_src
#  benchGen.cpp
#)

#add_executable(gen ${generator_src})
#set_target_properties(gen PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${SSDB_OUTPUT_DIRECTORY})
add_executable(ssdbgen benchGen.cpp)
extractDebugInfo("${GENERAL_OUTPUT_DIRECTORY}" "ssdbgen" ssdbgen)
set_target_properties(ssdbgen PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${GENERAL_OUTPUT_DIRECTORY})

