sysadmin@localhost:~$ cat /tmp/inside_setup.sh                                  
cd /app                                                                         
                                                                                
# create emulated bins                                                          
rm /sbin/fdisk                                                                  
cp sbin/fdisk /sbin/fdisk                                                       
cp sbin/system_init /lib/system_init                                            
cp sbin/start_webserver /usr/bin/start_webserver                                
                                                                                
gcc tmp/init.c -o /sbin/init                                                    
                                                                                
# logging                                                                       
rm /etc/rsyslog.conf                                                            
cp etc/rsyslog.conf /etc/rsyslog.conf                                           
                                                                                
cp etc/default/useradd /etc/default/useradd 

rm /etc/rsyslog.d/50-default.conf                                               
cp etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf                 
cp var/log/dmesg /var/log/dmesg                                                 
chown root:adm /var/log/dmesg                                                   
                                                                                
# dns                                                                           
rm /etc/bind/named.conf.local                                                   
cp etc/bind/named.conf.local /etc/bind/named.conf.local                         
cp etc/bind/db.example.com /etc/bind/db.example.com                             
cp etc/bind/db.localdomain /etc/bind/db.localdomain                             
cp etc/bind/db.192 /etc/bind/db.192           

cp etc/udev/udev.conf /etc/udev/udev.conf                                       
cp etc/udev/rules.d/70-persistent-cd.rules /etc/udev/rules.d/70-persistent-cd.ru
les                                                                             
cp etc/udev/rules.d/README /etc/udev/rules.d/README                             
                                                                                
# Setup users                                                                   
cp etc/skel/bashrc /etc/skel/.bashrc                                            
cp etc/skel/bashrc /root/.bashrc                                                
                                                                                
cp etc/skel/selected_editor /etc/skel/.selected_editor                          
cp etc/skel/selected_editor /root/.selected_editor                              
                                                                                
                                                                                
useradd -d /root -g operator operator                                           
useradd -m -s /bin/bash -c "System Administrator,,,," -G sudo,adm sysadmin      
echo "sysadmin:netlab123" | chpasswd                                            
echo "root:netlab123" | chpasswd                                                
                                    

# remove daily and weekly crons                                                 
rm -rf /etc/cron.daily/*                                                        
rm -rf /etc/cron.weekly/*                                                       
                                                                                
# Colored MOTD with user accounts                                               
echo -e "\nThis lab has two user accounts (username :: password )\n\n   \033[31m
root\033[0m     :: \033[1;34mnetlab123\033[0m\n   \033[31msysadmin\033[0m :: \03
3[1;34mnetlab123\033[0m\n\nPress the \033[32m[Enter]\033[0m key to begin...\n" >
 /etc/motd                                                                      
                                                                                
# Add user directory folders                                                    
cd /home/sysadmin                                                               
touch .sudo_as_admin_successful                                                 
# sed 's/session\s*optional\s*pam_mail.so\s*standard/#session optional pam_mail.
so standard/g' -i /etc/pam.d/login                                              
cp -r /app/home/sysadmin/* /home/sysadmin/                                      
mkdir -p Desktop Documents Downloads Music Pictures Public Templates Videos     
chown -R sysadmin:sysadmin /home/sysadmin                                       
cp /usr/share/dict/words /home/sysadmin/Documents                               
                                                                                
cd /root                                                                        
mkdir -p Desktop Documents Downloads Music Pictures Public Templates Videos 

# set vi as default text editor                                                 
update-alternatives --set editor /usr/bin/vim.tiny                              
                                                                                
# Copy, replace or edit needed config files                                     
#                                                                               
rm -rf /app                                                                     
                                                                                
# Update mlocate db                                                             
updatedb                  

