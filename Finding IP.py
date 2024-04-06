import socket

hostname = socket.gethostname()

print ("You Are Working Here" + hostname)
print("Your IP Is " + socket.gethostbyname(hostname))

url= input("ENTER URL TO SCAN >>>>")
print("THE IP FOR " + url + " IS " +socket.gethostbyname(url))
