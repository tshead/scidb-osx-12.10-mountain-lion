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

# shared library for user defined objects
set (find_stars_src
    plugin.cpp
    LogicalFindStars.cpp
    PhysicalFindStars.cpp
    PixelProvider.cpp
    Cook.cpp
)

add_library(findstars SHARED ${find_stars_src})
set_target_properties(findstars PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${GENERAL_OUTPUT_DIRECTORY}/plugins)
extractDebugInfo("${GENERAL_OUTPUT_DIRECTORY}/plugins" "libfindstars${CMAKE_SHARED_LIBRARY_SUFFIX}" findstars)

if (APPLE)
  set_target_properties(findstars PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
endif (APPLE)

