
#ifndef _REPLICATION_H
#define _REPLICATION_H

#ifdef __cplusplus
extern "C"
{
#endif


void replicationDiscardCachedMaster(void);
void replicationResurrectCachedMaster(int newfd);
void replicationSendAck(void);
void putSlaveOnline(client* slave);
int cancelReplicationHandshake(void);

#ifdef __cplusplus
}
#endif

#endif
