/**
 * @author: Mohsen Naderi (mohsen@mnaderi.com)
 *
*/


#include <exception>

int main(int argc, const char *argv[])
{
    try
    {
        //return sim.run(argc, argv);
        return 0;
    }
    catch(std::exception& e)
    {
        std::cerr << "Got exception: " << e.what() << std::endl;
        return 1;
    }
    catch(...)
    {
        std::cerr << "Got unknown exception" << std::endl;
        return 1;
    }
}
