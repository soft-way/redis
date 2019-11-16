#ifndef __RELEASE__H
#define __RELEASE__H


#define REDIS_GIT_SHA1 "00000000"
#define REDIS_GIT_DIRTY "0"
#define REDIS_BUILD_ID "SOFTWAY-PC0-1554291189"

#ifdef __cplusplus
extern "C"
{
#endif

char* redisGitSHA1();
char* redisGitDirty();
unsigned long long redisBuildId();

#ifdef __cplusplus
}
#endif

#endif