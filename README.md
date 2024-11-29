# Script Notify

This project works as a wrapper for a bash script so you can be notified when your bash finishes running.

## How to use it

### You can define your configuration by

1. Using environment variables
   | Variable    | Description | Required |
   |-------------|-------------|----------|
   | RECIPIENT | Email of whom is going to receive the message | Yes |
   | SENDER | Sender of the email. Also email username used in the login process | Yes |
   | PASSWORD | Your generate password or default account password. This depends on your current security configurations. | Yes |
   | SCRIPT_PATH | Path to the script that will run | Yes |
```bash
SCRIPT_PATH=<path-to_script> RECIPIENT=<email-recipient> SENDER=<email-sender> PASSWORD=<your-email-password> python main.py
```
2. Passing as arguments in the CLI

```bash 
python main.py --script-path <path-to_script> --recipient <email-recipient> --sender <email-sender> --password <your-email-password>
```