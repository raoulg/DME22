# What is a devcontainer

A devcontainer is a Docker container that is used to develop a project. It is an easy way to set up your
development environment. This has upsides and downsides; the upside is that setting up the environment is
very easy, because the only thing you will need to install is Docker (you dont even need WSL2), and
inside the devcontainer everything is already set up.

The downside is that everything is already set up :) We think the skills to set up a solid
and deterministic environment, that will work even in production, are valuable.

This means the devcontainer is either intended for the beginners, or for the
experienced people, but not for everyone in between because they should learn
things like pyenv, pdm, git etc.

## How to use it

First, install the "Dev Containers" extension in VScode.
If you refresh VScode, and open the repository, it will detect the `.devcontainer` folder
and it will ask you if you want to reopen the repository in the devcontainer.

If you say yes, it will pull the image from dockerhub, and start the container.
You will now have everything you need:

- python 3.11.5
- pdm
- git lfs
- linting & formatting dependencies

You will also have some additional things:

- zsh shell (if you dont see colors, type `zsh` in the terminal)
- zoxide: a tool to quickly navigate to folders you use often. Once you have visited a folder with the `cd` command, you can type `z` followed by part of the foldername. So if you have visited `~/projects/learning-python`, you can type `z learn` to go there again, regardless of where you are. This will save a lot of typing
- exa: a nicer ls. Try the command `lsd` to see exa in action. This is aliased to `exa -h --icons --long --sort=mod`
- lefthook and lychee. You only need this if you want the automated linting with githooks. It is optional to use, but could be a good idea for your own project.
