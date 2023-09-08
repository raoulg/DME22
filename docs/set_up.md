# Setting up your development environment

## windows: WSL2 or docker

Windows users will need WSL2 or the devcontainer.

- See [this](wsl2/wsl2.md) for wsl2 instructions.
- see [this](vscode/devcontainer.md) for the devcontainer instructions.

## Create an ssh-key

You will need to create a ssh-key and add it to gitlab. If you are on WSL2, you will need to do that INSIDE the WSL2 environment!

For instructions, see [this](ssh/01_setting_up_ssh.md).

## Create the code folder

This is not mandatory, but I recommend to create, inside your home folder, a `code` folder. This is a folder where you can put all your git repositories. This will make it easier to find them, and it will make it easier to find them in VScode.

You can do so with `mkdir ~/code`.\`
If you have another location you prefer, you are free to do that.

If the command line and all commands are new and confusing, you might want to take a break here and first study the [command line](commandline/commandline.md) tutorial.

## install git-lfs

For large files, we use git-lfs. You can install it with:

```bash
apt-get install -y git-lfs
```

on linux or

```bash
brew install git-lfs
```

on mac.

## Clone with git

Now, navigate to your `code` folder (or the equivalent location) and do `git clone git/url/here` where you copy the ssh or https url from git.

## SSH / PAT

We dont need ssh for this project, so you can skip this.

If you have set up your ssh-key inside the `~/.ssh` folder, git will find it and authenticate with that.

Alternatively, you can create a [PAT token on gitlab](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), and use that to clone with https. In that case, you do `git clone https://gitlab.com/han-aim/mads/course-materials-uos1.git` and you have to authenticate with your gitlab username and PAT token.

## Connect WSL to VScode

> NOTE: this is only for WSL2 users. Others can skip to the next section.

To make WSL work with vscode, you will need the WSL extension. Just search for WSL in extensions in VScode, and install it.

To connect to WSL with VScode, click the small blue icon in the bottom left corner of VScode with the two arrows, and select WSL with `Connect to WSL`. The blue icon will change, it will now say `WSL: Ubuntu`

## Open the git repo in VScode

In VScode, select `Open Folder`, select the folder you just cloned (so, `home/yourname/code/course-materials-uos1`), press ok.

You will be asked if you `Trust the authors`, click yes.

If you havent done so, install the necessary extensions, like: Python, jupyter, git-graph. You can find more details about recommended extensions [here](vscode/recommended.md).

## Install python

To get everything to work, we will need to have a proper way to install and manage both Python and the dependencies.

### Pyenv

We will use `pyenv` to manage our python versions.
You can install it with

```bash
curl https://pyenv.run | bash
```

for pyenv, and run

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

so that your terminal will find pyenv. More details are in the documentation [dependencies/02_version_management.md](dependencies/02_version_management.md).

For your build environment run:

#### for Ubuntu/WSL2:

```bash
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

#### Mac

and for macOS (which needs `brew` as a dependency, see [here](https://brew.sh/):

```bash
brew install openssl readline sqlite3 xz zlib tcl-tk
```

Remeber to restart your terminal after this.
Check if pyenv is installed with `pyenv --version` or `which pyenv`.

### Pick a python version

After this, you can install a python version. Lets check for the latest:

```bash
pyenv install --list | grep 3\.11
```

This gives you a list of latest versions available. Lets pick 3.11.5:

```bash
pyenv install 3.11.5
```

Now, if you do `pyenv versions` you should see 3.11.5 installed. Lets set that as the global version:

```bash
pyenv global 3.11.5
```

Now, if you do `python --version` you should see 3.11.5.
Everywhere this system (WSL2 or your mac) will now use this version of python.

It's easy to install additional versions of python, and switch between them. Just do `pyenv install 3.10.0` and you have it. You can also change it for a local folder (while keeping globally 3.11) with `pyenv local 3.10.0`.

### PDM

We will also need something for our dependencies. We will use pdm. For details, see our documentation in [dependencies/03_dependencies_management.md](dependencies/03_dependencies_management.md).

To install pdm, run:

```bash
curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

And restart the terminal. You can check with `pdm --version` if it is installed.

### Install dependencies

Now everything is ready to install the dependencies. In the root of the git repo, run:

```bash
pdm install
```

PDM will find the `pyproject.toml` file, and it will install all dependencies.
Restart VScode, and now it will find your venv automatically.

## Test a notebook

Now open a notebook (`lessons/04/iris.ipynb`) and in the right upper corner, click `select kernel` (or, a python version if it is already selected).
You should now see, among others, the python versions you installed with `pyenv`, but also a version inside the `.venv` folder inside your project.
Select that one, and run the notebook. If everything went well, your ready!
