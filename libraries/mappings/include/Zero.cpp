#include "Zero.h"

#include <string>
using std::to_string;

mappings::Zero::Zero(uint64 size) : Layer(size, Type::zero)
{}

void mappings::Zero::Compute(const vector<unique_ptr<Layer>>& previousLayers)
{
    Clear();
}

void mappings::Zero::Serialize(JsonSerializer & serializer) const
{
    // version 1
    Layer::SerializeHeader(serializer, 1);

    serializer.Write("size", _output.size());
}

void mappings::Zero::Deserialize(JsonSerializer & serializer, int version)
{
    if (version == 1)
    {
        uint64 size = 0;
        serializer.Read("size", size);
        _output.resize(size);
    }
    else
    {
        throw runtime_error("unsupported version: " + to_string(version));
    }
}
