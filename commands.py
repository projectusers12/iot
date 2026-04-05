1. Basic File & Directory Commands

man
Shows manual/help for any command.
Example:  man ls

ls
Lists files in the current directory.
Example:  ls
          ls -l        (detailed list)
          ls -a        (show hidden files)

cd
Changes directory.
Example:  cd Desktop
          cd ..        (go back one level)
          cd /home/pi  (go to absolute path)

pwd
Shows current directory path.
Example:  pwd

mkdir
Creates a new folder.
Example:  mkdir project

rmdir
Removes an empty directory.
Example:  rmdir myfolder

rm
Deletes files or folders. Be careful - no recycle bin!
Example:  rm file.txt
          rm -r foldername   (delete folder and all contents)

cp
Copies files or directories.
Example:  cp a.txt b.txt
          cp -r folder1 folder2   (copy entire folder)

mv
Moves or renames files.
Example:  mv old.txt new.txt                 (rename)
          mv file.txt /home/pi/Desktop        (move)

touch
Creates an empty file or updates its timestamp.
Example:  touch notes.txt

cat
Displays file content.
Example:  cat file.txt

head
Shows first 10 lines of a file.
Example:  head logfile.txt

tail
Shows last 10 lines of a file.
Example:  tail logfile.txt
          tail -f logfile.txt   (live updates)

chmod
Changes file permissions.
Example:  chmod +x script.sh   (make file executable)

2. SSH & System Commands

ssh
Connect to another machine remotely.
Example:  ssh pi@192.168.1.10

df
Shows disk usage.
Example:  df -h   (human readable sizes)

dd
Used to copy disks, USB drives, or SD cards. Dangerous if wrong path!
Example:  dd if=/dev/sda of=backup.img

tree
Shows folder structure like a tree.
Example:  tree

zip
Compress files into a zip archive.
Example:  zip files.zip file1 file2
          zip -r folder.zip foldername   (zip entire folder)

unzip
Extract a zip archive.
Example:  unzip files.zip

tar
Create or extract .tar / .tar.gz archives.
Create:   tar -czvf backup.tar.gz folder/
Extract:  tar -xzvf backup.tar.gz

3. Searching Commands

grep
Search for text inside files.
Example:  grep "error" logfile.txt

awk
Processes text line-by-line.
Example:  awk '{print $1}' data.txt   (prints first column)

find
Search for files by name or property.
Example:  find . -name "*.txt"
          find / -type f -size +10M   (files bigger than 10MB)

whereis
Shows the location of a command.
Example:  whereis python3

4. Networking Commands

ping
Checks if a device or website is reachable.
Example:  ping google.com

hostname
Shows the device name.
Example:  hostname

ifconfig
Shows IP address and network info.
Example:  ifconfig
Note: Install with  sudo apt install net-tools  if not available.
