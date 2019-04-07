
#ifndef __HIREDIS_EXPORTS_H__
#define __HIREDIS_EXPORTS_H__


#if defined (_WIN32)
#  if defined (HIREDIS_EXPORTS)
#    define HIREDIS_EXPORT  __declspec (dllexport)
#  else
#    define HIREDIS_EXPORT  __declspec (dllimport)
#  endif   /* ! HIREDIS_EXPORTS */
#else
#  define HIREDIS_EXPORT
#endif     /* _WIN32 */

#endif // __HIREDIS_CCC_EXPORTS_H__

