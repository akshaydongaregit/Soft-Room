
import subprocess, time, os, sys

check_java = False
install_java = False
wget_elastic = False

def check_java():
  
   java = False

   cmd = ["java", "-version"]

   p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

   for line in iter(p.stdout.readline, b''):
       #print(">>> " + str(line.rstrip()))
       if line.rstrip().find(b'openjdk version "') >= 0 :
          #print("found")
          java = True

   return java

def install_java() :

   cmd = ["sudo", "apt" ,"install" ,"openjdk-8-jre-headless" ,"apt-transport-https" ,"-y"]
   p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

   for line in iter(p.stdout.readline, b''):
       print(str(line.rstrip()))

   p.wait()
   if(p.returncode == 0) :
      return True
   else :
      return False

def wget_elastic() :
   cmd = "wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - "
   p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,shell=True)

   for line in iter(p.stdout.readline, b''):
      print(str(line.rstrip()))
   
   p.wait()
   #print("wget_elastic : ",p.returncode)

   if(p.returncode == 0) :
      return True
   else :
      return False

def add_deb() :
   cmd = ' echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic.list'
   p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,shell=True)

   for line in iter(p.stdout.readline, b''):
      print(str(line.rstrip()))
   
   p.wait()
   if(p.returncode == 0) :
      return True
   else :
      return False


def install_elastic() :
   cmd = 'sudo apt update && sudo apt install elasticsearch -y'
   p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,shell=True)

   for line in iter(p.stdout.readline, b''):
      print(str(line.rstrip()))
   
   p.wait()
   if(p.returncode == 0) :
      return True
   else :
      return False


#  ----------   check java    ---------

if(check_java()) :
   print("install_java : ",install_java())

# ---------- java check complete -------------

#print("wget_elastic : ",wget_elastic())
#print("add deb : ",add_deb())
#print("install_elastic : ",install_elastic())
