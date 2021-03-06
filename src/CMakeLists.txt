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

add_subdirectory("capi")
add_subdirectory("network")
add_subdirectory("system")
add_subdirectory("smgr")
add_subdirectory("util")
add_subdirectory("mpi")
add_subdirectory("linear_algebra")

if (NOT WITHOUT_SERVER)
    add_subdirectory("array")
    add_subdirectory("query")

    file(GLOB include_src "../include/*.h" "../include/array/*.h" "../include/system/*.h"
            "../include/query/*.h" "../include/util/*.h")

    add_executable(scidb network/entry.cpp ${include_src})
    extractDebugInfo("${GENERAL_OUTPUT_DIRECTORY}" "scidb" scidb)
    set_target_properties(scidb PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${GENERAL_OUTPUT_DIRECTORY})
    target_link_libraries(scidb network_lib util_lib system_lib qproc_lib array_lib
        ${LIBRT_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT} ${CMAKE_DL_LIBS})
endif()
