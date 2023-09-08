## What is a Command Line Interface (CLI)?

The CLI on an operating system is basically a program that allows you to interact with your computer using text commands. The CLI is also referred to as the terminal, a shell or console. It enables users to perform various tasks, execute programs, and manage files and directories by typing specific commands instead of using a graphical user interface (GUI), like windows or MacOS.

If you have seen them before, CLI's can often appear as a bunch of words, seprated by different symbols or signs. An important symbol is the seperator between the prompt and the command. The prompt gives you information about context in which you are executing the command (often username, computername and the directory you are in). The separator between the prompt and the command is often a dollar sign ($). A standard prompt looks like this:

```bash
username@computer_name ~/Documents$_
```

A command is the text-based input that you put in the prompt. A command can have argunemts, options and flags.

- Arguments are values given by a user and are read in order from first to
  last. For example, this command is called with three file names as arguments in the directory `~/Documents`.

  ```bash
  username@computer_name ~/Documents$read CodestyleStandards.md cooiecutter.md depencencies.md
  ```

- Options are named key-value pairs. Keys start with one or two dashes (- or --), and a user can separate the key and value with an equal sign (=) or a space (see Option). This command is called with two options:

  ```bash
  $results student_results.xlsx --count=5 --index 2
  ```

- Flags are like options, but without a paired value. Instead, their presence indicates a particular value. This command is called with two flags:

  ```bash
  $results student_results.xlsx --count=5 --averages --projects_only
  ```

> The command line is favored by many experienced IT-professionals because it allows for automation, scripting, efficient use of system resources and a deeper level of control. Using the command line will improve your understanding of the context in which you are working, it will improve communication with other developers and overall steepens your learning curve in becoming a better data scientist.

## Learn the essentials

If you are new or unfimiliar with the command line, we recommend that you work trought the following sections of the [geekforgeeks](https://www.geeksforgeeks.org/linux-commands/) tutorial:

### absolute must haves

- [sudo command](https://www.geeksforgeeks.org/sudo-command-in-linux-with-examples/)

*navigation*

- [ls command](https://www.geeksforgeeks.org/ls-command-in-linux/)
- [cd command](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/)
- [pwd command](https://www.geeksforgeeks.org/pwd-command-in-linux-with-examples/)

**exercise**: navigate to the directory where you cloned this repository. Check the `pwd`. Now cd to the `docs` directory and check the `pwd` again. List content with `ls`. Now cd back to the directory where you cloned this repository.

file management

- [mkdir command](https://www.geeksforgeeks.org/mkdir-command-in-linux-with-examples/)
- [rm command](https://www.geeksforgeeks.org/rm-command-linux-examples)
- [cp command](https://www.geeksforgeeks.org/cp-command-linux-examples/)
- [mv command](https://www.geeksforgeeks.org/mv-command-linux-examples/)
- [touch command](https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/)

**excercise**: create a new directory called `test` in the directory where you cloned this repository with `mkdir`. Create a new file called `test.txt` in the `test` directory with `touch`. Create a `test2` directory. Copy the `test.txt` file to the `test2` directory. Move the `test.txt` file to the `docs` directory. Remove the `test.txt` file from the `docs` directory. Remove the `test` and `test2` directory.

searching

- [grep](https://www.geeksforgeeks.org/grep-command-in-unixlinux/)
- [find command](https://www.geeksforgeeks.org/find-command-in-linux-with-examples/)
- [locate command](https://www.geeksforgeeks.org/locate-command-in-linux-with-examples/?ref=lbp)
- [wich command](https://www.geeksforgeeks.org/which-command-in-linux-with-examples/)

**excercise**: show locations of the `python`, `pyenv`, `ls` and `mkdir` commands with `which`. Find all files with the name `README.md` in the directory where you cloned this repository with `find`. Find all files with the name `README.md` in the directory where you cloned this repository with `locate`. Find all files with the **word** `README.md` in the directory where you cloned this repository with `grep`.

screenprinting

- [cat command](https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/)
- [echo command](https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/)
- [less command](https://www.geeksforgeeks.org/less-command-linux-examples/)

### nice to haves

remote

- [ssh command](https://www.geeksforgeeks.org/ssh-command-in-linux-with-examples/)
- [scp command](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/)

processes

- [ps command](https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/)
- [top command](https://www.geeksforgeeks.org/top-command-in-linux-with-examples/)
- [kill command](https://www.geeksforgeeks.org/kill-command-in-linux-with-examples/)
- [source command](https://www.geeksforgeeks.org/source-command-in-linux-with-examples/)
- [systemctl command](https://www.geeksforgeeks.org/start-stop-restart-services-using-systemctl-in-linux/)

miscellaneous

- [df command](https://www.geeksforgeeks.org/df-command-in-linux-with-examples/)
- [apropos command](https://www.geeksforgeeks.org/apropos-command-in-linux-with-examples/)
- [nano command](https://www.geeksforgeeks.org/nano-text-editor-in-linux/)
- [vim editor](https://www.geeksforgeeks.org/nano-vs-vim-editor-whats-the-difference-between-nano-and-vim-editors/)
- [neovim as ide](https://www.youtube.com/watch?v=stqUbv-5u2s)

> NOTE: If you do not have a GeeksforGeeks account, the pop-up asking you to create an account can be quite annoying. If this is a showstopper for you and don't want to create an account, [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial) is good alternative. You can also check out the [Linux Command Line for Beginners](https://www.youtube.com/playlist?list=PLS1QulWo1RIb9WVQGJ_vh-RQusbZgO_As) playlist on YouTube.

We reccommend that you try out some of the commands in your own shell-interface. We do not expect that you understand every command right away, but it is important that you get a feel for the command line and and get familiarized with the basic commands. Use the resources provided here as reference when you encouter a command you do not understand.
