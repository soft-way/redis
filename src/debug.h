#ifndef __DEBUG__H
#define __DEBUG__H



#ifdef __cplusplus
extern "C"
{
#endif

void _serverAssert(const char* estr, const char* file, int line);

#ifdef __cplusplus
}
#endif

#endif