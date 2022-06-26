host = input("Enter the host name: ")
user = input("Enter the user name: ")
password = input("Enter password: ")

out2 = open('config.py', 'w')
output2 = 'config = "mysql://' + user + ':' + password + '@' + host + '/etlproject"\n'
out2.write(output2)
out2.close()

out = open('../connection.bat', 'w')
output = '@echo off\ntitle Connection Establishment\ncall mysql -h ' + host + ' -u ' + user + ' -p\npause'
out.write(output)
out.close()
