Set up a reverse SSH tunnel

### 1 - Reverse SSH Tunnel
On RPi4, run the following command to create a reverse SSH tunnel to RPi2:
```bash
ssh -R 50000:localhost:22 user@RPi2_IP
```
   - Replace `user` with the username on RPi2.
   - Replace `RPi2_IP` with the static IP address of RPi2. 

This command will allow RPi2 to connect to RPi4 via port 50000.

Keep the SSH session open. This command needs to remain running for the tunnel to stay active. 

### 2 - Execute Scripts on RPi4 from RPi2
On RPi2, you can now SSH into RPi4 using the reverse tunnel. Use the following command:
```bash
ssh -p 50000 user@localhost
```
   - Replace `user` with your username on RPi4.

Run your script: Once you are logged into RPi4, you can execute any script you want. For example, to create a file with the current date, you can run:
```bash
echo "Current date: $(date)" > ~/current_date.txt
```

### Example Workflow
1. On RPi4:
```bash
ssh -R 50000:localhost:22 user@RPi2_IP
```

2. On RPi2:
```bash
ssh -p 50000 user@localhost
```

3. On RPi4 (after logging in from RPi2):
```bash
echo "Current date: $(date)" > ~/current_date.txt
   ```

### Ideas 
- Ensure that SSH is installed and enabled on both Raspberry Pis.
- If you encounter any issues with permissions or connectivity, check your SSH configuration and firewall settings.
- You may want to set up SSH key authentication for easier access without needing to enter a password each time.

