# Create and write 
with open("file1.txt", "w") as f: 
    f.write("Hello, this is sample text!") 
 
# Read file 
with open("file1.txt", "r") as f: 
    content = f.read() 
    print("File content:", content) 
 
# Copy content to another file 
with open("file1.txt", "r") as source, open("file2.txt", "w") as dest: 
    for line in source: 
        dest.write(line)
