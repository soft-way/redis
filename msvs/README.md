# build redis on windows                                                      
                                                                              
1. git clone https://github.com/soft-way/redis.git                            
2. follow deps/jemalloc/msvc/ReadMe.txt to generate jemalloc header files for Windows            
   sh -c "CC=cl ./autogen.sh" (in x64 Native Tools Command Prompt for VS 2019)
3. open msvs\RedisServer.sln in Visual Studio Community 2019                  
4. build RedisServer project
