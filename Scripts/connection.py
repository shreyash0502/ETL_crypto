host = input("Enter the host name: ")
user = input("Enter the user name: ")

out = open('../connection.bat', 'w')
output = '@echo off\ntitle Connection Establishment\ncall mysql -h ' + host + ' -u ' + user + ' -p\npause'
out.write(output)
out.close()
