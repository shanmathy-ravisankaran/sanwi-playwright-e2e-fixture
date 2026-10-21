import subprocess

def unsafe_command(user_input):
    # INTENTIONALLY UNSAFE: test fixture only.
    subprocess.run(
        "echo " + user_input,
        shell=True,
        check=False
    )
