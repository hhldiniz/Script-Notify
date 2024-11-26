import subprocess

from arguments.argument_factory import ArgumentFactory
from email_sender import Email
from environment import Environment

if __name__ == "__main__":

    argument_factory = ArgumentFactory()

    script_path = argument_factory.script_path
    script = argument_factory.script

    print("Passed script: {}", script_path or script)

    email_sender = Email()

    # Run the script using subprocess.run()
    call_response = subprocess.run(
        ["bash", script_path or script], capture_output=True, text=True
    )

    call_return = f"Process returned with code {call_response.returncode}. Call response: {call_response.stdout}"

    print(call_return)

    email_sender.send_email(
        Environment.SENDER.value,
        Environment.PASSWORD.value,
        Environment.RECIPIENT.value,
        "Script Execution Complete",
        call_return,
    )
