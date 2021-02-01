import subprocess
import argparse

from shlex import shlex


def print_lesson_setup(lesson_id: int):
    result_msg = {
        1: "openssh-clients installed on controller",
        2: "inventory file created",
        3: "python3 installed on clients",
        4: "updated the content of /etc/motd",
    }
    print(
        "{:40} --- {:6}".format(
            result_msg[lesson_id], "\x1b[1;32;40m" + "Success!" + "\x1b[0m"
        )
    )


def get_user_args():

    script_description = """
PORTUGUÊS:
    Script para certificar que os passos anteriores a lição recebida
    foram realizados
    Usado caso queria realizar alguma lição sem começar do inicio   

ENGLISH:
    Script to make sure all the steps before the one received were
    properly done
    Used in case you want to start somewhere different than the beginning 
    """
    parser = argparse.ArgumentParser(
        description=script_description, formatter_class=argparse.RawTextHelpFormatter
    )
    # TODO parse the README.md for available lessons
    parser.add_argument("-l", "--lesson", type=int, choices=range(2, 5))

    args = parser.parse_args()
    return args


def run_local_command(command):
    shell_format_command_list = list(shlex(command, punctuation_chars=True))
    command_result = subprocess.run(shell_format_command_list, stdout=subprocess.PIPE)
    if command_result.returncode != 0:
        print(command_result)
        raise RuntimeError(f"Unexpected error running the command:\n{command}")
    return command_result
