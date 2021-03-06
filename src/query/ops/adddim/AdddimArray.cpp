/*
**
* BEGIN_COPYRIGHT
*
* This file is part of SciDB.
* Copyright (C) 2008-2012 SciDB, Inc.
*
* SciDB is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation version 3 of the License.
*
* SciDB is distributed "AS-IS" AND WITHOUT ANY WARRANTY OF ANY KIND,
* INCLUDING ANY IMPLIED WARRANTY OF MERCHANTABILITY,
* NON-INFRINGEMENT, OR FITNESS FOR A PARTICULAR PURPOSE. See
* the GNU General Public License for the complete license terms.
*
* You should have received a copy of the GNU General Public License
* along with SciDB.  If not, see <http://www.gnu.org/licenses/>.
*
* END_COPYRIGHT
*/

/**
 * @file AdddimArray.cpp
 *
 * @brief Adddim array implementation
 *
 * @author Konstantin Knizhnik <knizhnik@garret.ru>
 */

#include "AdddimArray.h"

namespace scidb {

    using namespace boost;
    using namespace std;

    inline void addDim(Coordinates const& src, Coordinates& dst) 
    {
        for (size_t i = 0, n = src.size(); i < n; i++) { 
            dst[i+1] = src[i];
        }
    }
        
    inline void delDim(Coordinates const& src, Coordinates& dst)
    {
        for (size_t i = 0, n = dst.size(); i < n; i++) { 
            dst[i] = src[i+1];
        }
    }
        

    //
    // Adddim chunk iterator methods
    //
    Coordinates const& AdddimChunkIterator::getPosition()
    {
        Coordinates const& inPos = DelegateChunkIterator::getPosition();
        addDim(inPos, outPos);
        return outPos;
    }

    bool AdddimChunkIterator::setPosition(Coordinates const& outPos)
    {
        if (outPos[0] != 0) { 
            return false;
        }
        delDim(outPos, inPos);
        return DelegateChunkIterator::setPosition(inPos);
    }

    AdddimChunkIterator::AdddimChunkIterator(DelegateChunk const* chunk, int iterationMode)
    : DelegateChunkIterator(chunk, iterationMode),
      outPos(chunk->getArrayDesc().getDimensions().size()),
      inPos(outPos.size()-1)
    {
        outPos[0] = 0;
    }

    //
    // Adddim chunk methods
    //
	Coordinates const& AdddimChunk::getFirstPosition(bool withOverlap) const
    {
        Coordinates const& inPos = DelegateChunk::getFirstPosition(withOverlap);
        addDim(inPos, ((AdddimChunk*)this)->outPos);
        return outPos;
    }

	Coordinates const& AdddimChunk::getLastPosition(bool withOverlap) const
    {
        Coordinates const& inPos = DelegateChunk::getLastPosition(withOverlap);
        addDim(inPos, ((AdddimChunk*)this)->outPos);
        return outPos;
    }

    AdddimChunk::AdddimChunk(AdddimArray const& array, DelegateArrayIterator const& iterator, AttributeID attrID)
    : DelegateChunk(array, iterator, attrID, true),
      outPos(array.getArrayDesc().getDimensions().size())
    {
        outPos[0] = 0;
    }
      
    void AdddimChunk::setInputChunk(ConstChunk const& inputChunk)
    {
        DelegateChunk::setInputChunk(inputChunk);
        isClone = !inputChunk.isSparse();
    }

    //
    // Adddim array iterator

    Coordinates const& AdddimArrayIterator::getPosition()
    {
        Coordinates const& inPos = DelegateArrayIterator::getPosition();
        addDim(inPos, outPos);
        return outPos;
    }

    bool AdddimArrayIterator::setPosition(Coordinates const& outPos)
    {
        if (outPos[0] != 0) { 
            return false;
        }
        delDim(outPos, inPos);
        return DelegateArrayIterator::setPosition(inPos);
    }

    AdddimArrayIterator::AdddimArrayIterator(AdddimArray const& array, AttributeID attrID, boost::shared_ptr<ConstArrayIterator> inputIterator)
    : DelegateArrayIterator(array, attrID, inputIterator),
      outPos(array.getArrayDesc().getDimensions().size()),
      inPos(outPos.size()-1)
    {
    }

    //
    // Adddim array methods
    //

    DelegateChunk* AdddimArray::createChunk(DelegateArrayIterator const* iterator, AttributeID id) const
    {
       return new AdddimChunk(*this, *iterator, id);
    }

    DelegateChunkIterator* AdddimArray::createChunkIterator(DelegateChunk const* chunk, int iterationMode) const
    {
        return new AdddimChunkIterator(chunk, iterationMode);
    }

    DelegateArrayIterator* AdddimArray::createArrayIterator(AttributeID id) const
    {
        return new AdddimArrayIterator(*this, id, inputArray->getConstIterator(id));
    }    

    AdddimArray::AdddimArray(ArrayDesc const& desc, boost::shared_ptr<Array> const& array)
    : DelegateArray(desc, array)
    {
    } 
}

