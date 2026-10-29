# File Handling

# case 1 - if the file is not present

# created file handler object which can be used to read or write
f = open('sample.txt', 'w')         # name of the file and opening in write mode and locarion is not provided
f.write('Hello world')      # writing inside the file
f.close()
# since file is closed hence this will not work
f.write('hello')