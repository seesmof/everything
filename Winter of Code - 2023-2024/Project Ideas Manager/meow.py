from click_shell import shell


@shell(prompt="sees-shell > ", intro="Welcome to sees-shell!")
def sees_shell():
    pass


@sees_shell.command()
def help():
    print(
        """
Here is a list of all commands:

help: See this list           
hello-world: Prints a message
add: Add two numbers
create-file: Create a new file and write into it
exit: Exit the shell
"""
    )


if __name__ == "__main__":
    sees_shell()
