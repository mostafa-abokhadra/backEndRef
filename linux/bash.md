### finding a file in the system
```bash
sudo find / -name mongo
```
- above example starts searching from the root dir
```bash
sudo find /mnt/c/Users/20115/documents/repos/backEndRef -name bash.md
```
- start Searching from backEndRef

### killing a program running in specific port
```bash
lsof -i :3000
```
- This will give you the PID (Process ID) of the application using that port.
- then Kill the process using the kill command:
```bash
kill -9 <PID>
```