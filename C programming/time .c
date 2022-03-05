Let me just see if I have this correct...

You have a program that your wrote, that is a 'server'.  You are installing it on a program, which will be your server.  You want this program to only run for 15 days, then quit?  If this is what you are doing, then get back to me.  Dates are ussually stored like so:
yyyyddmm.  This is just a simple thing... IT ADDS UP TO A LONG... which would be linear... which means, it's very easy to check for.

#include <time.h>

time_t TheStart;
time_t Current;
time_t ExpireTime = 24L*60L*60L * 15;

//24 hours, 60 minutes, 60 seconds.
//* 15 = total time in seconds for 15
//days.

TheStart = time(NULL);
ExpireTime += TheStart;  //15 days + current date.

//Write Expire time to a file...

Current = time(NULL);

//Checks time by the second!
//So, it's 15 days to the second!
if (Current > ExpireTime)
{
   //Went over the time!
   //Say, you can't go on!
   return -1;
}
