# Automated linting

## Lefthook

The first tool we use is lefthook.

From their intro post:

> No matter if you’re working on an open source project with the whole world as your oyster, or if you’re “blooming” in a walled garden of proprietary commercial software—you’re still working on a team. And even with a well-organized system of pull requests and code reviews, maintaining the code quality across a large codebase with dozens of contributors is not an easy task.

This is the reason we like to use formatters and linters. The downside of that is, you will need to
run the formatters and linters, which means: first run black, then isort, then lint with ruff, then check with myopy, etc etc. This is tedious and error prone. One solution is to make a `Makefile`, but you will still have to manually run `make lint` or something along those lines.

That is where lefthook comes in. Again, from their intro post:

> However, when you’re working on a project, you’re most interested in writing that project’s code—not the code that checks it.

What lefthook will do is it will inject scripts that `hook into` your git commands. You can define pre-commit, pre-push and pre-merge hooks. The `pre-` means just what you expect; just before you commit, this will be kicked off.

```yml
pre-commit:
  commands:
    black:
      files: git ls-files
      glob: '*.{py, ipynb}'
      run: black {staged_files}
      stage_fixed: true
    isort:
      files: git ls-files
      glob: '*.py'
      run: isort {staged_files}
      stage_fixed: true
    clean-jupyter:
      files: git ls-files
      glob: '*.ipynb'
      run: pdm run jupyter nbconvert --clear-output --inplace {staged_files}
      stage_fixed: true
    ruff:
      files: git ls-files
      glob: '*.py'
      run: pdm run ruff {staged_files}
    mypy:
      glob: '*.py'
      run: pdm run mypy --pretty {staged_files}
```

Here you see a simplified version of our lefthook.yml file. It defines a `pre-commit` hook, and it will run every time just before you try to commit something. Lets pick out one of the commands and see what it does:

`black` will run the black formatter on all python and ipynb files (this is what the `glob` filter is for) tracke by git (this is what `git ls-files` does) that are staged (this is where the `{staged_files}` come in) for commit.

So it will work just on the few files you commit, which is to speed things up. This way, you dont have to run `black myfile.py` or `black myfolder` by hand.

It will then stage the changes it made (done by `stage_fixed: true`), because black will actually change how your code looks, which means the file you are going to commit might look different from the file you are working on. This is a good thing, because it means you dont have to worry about formatting anymore.

## Cleaning jupyter notebooks

Be aware that `clean-jupyter` will clean up your jupyter notebooks. The reason for this is that jupyter notebooks will change every time you run a cell; there is a counter that keeps track of how often a cell has been run, and you dont want to commit things like that. This also means that all the output of your cells is removed. This might interfere with the workflow of some people, that are used to treat their jupyter notebooks as some sort of storage for their results. I consider this bad practice: if there is anything you want to store (eg, because it takes a long time to execute), store the output as a seperate file. In addition to that, jupyter notebooks shouldnt be used to reliable create output, you should move your code to a script anyway (see the section `growing up from jupyter notebooks` at the end of `lessons/04_collection_and_pipelines/02_cleaning_data.ipynb`)

# Running lefthook

There are a few ways you can run lefthook:

## locally as a git hook

You should install  `lefthook` on your machine to do this. Their [installation guide](https://github.com/evilmartians/lefthook/blob/master/docs/install.md) has a lot of flavors.

```bash
curl -1sLf 'https://dl.cloudsmith.io/public/evilmartians/lefthook/setup.deb.sh' | sudo -E bash
sudo apt install lefthook
```

One of the hooks is lychee; it will check for broken links in the markdown files. To do this, it will need to install [lychee](https://github.com/lycheeverse/lychee).

```bash
curl -sSf 'https://sh.rustup.rs' | sh -s -- -y
apt install gcc pkg-config libc6-dev libssl-dev
```

For Rust, pick the default option 1.

After this, you can simply do `lefthook install` in the project directory where you find the `lefthook.yml` file.
After this, the hooks will run automatically when you commit or merge with git.

You can also kick off the lefthook by hand, by doing `lefthook run pre-commit` from the command line.

## Fixing problems with VScode or other GUI git tools

lefthook runs checks with dependencies like `black`, `bandit`, etc. This means that the environment in which you execute lefthook needs to know where to find these programs.

If you run lefthook from a terminal, the `pdm` environment needs to be activated. This can be done manually by running `eval $(pdm venv activate)`. The problem with using git from your vscode is that it wont activate this environment and it will complain that it cant find `black` or `bandit`. The solution: you need to tell lefthook where to find these things.

1. Find out where your venv is located. If you run `pdm venv activate` from your terminal, this command will output the location of your venv. Remove the `/activate` part from the path, such that it looks something like this: `/home/mads/.venv/course-materials-uos1-KNtHm8fd-mads-course/bin/` where `home` and `mads` will be different locations for your machine.
1. Create a `.lefthook-local.yml` file. This will be used, well, locally. In there, add a line that points to your local config, like this: `rc: .lefthookrc`
1. Create a `.lefthookrc` file. This will be used by lefthook to find the executables. In there, add a line that points to your venv, like this: `PATH=$HOME/mads/.venv/course-materials-uos1-KNtHm8fd-mads-course/bin:$PATH`. What this does, it will tell where to look for commands like `bandit`, and it will now look into that  `.venv` location.
1. Update your hooks by running `lefthook install -f`.
1. Profit.

You should now be able to use vscode (or other git tools) and it will run lefthook without complaining about missing executables.

## via the ci pipeline

There is a `Dockerfile` in the project, along with `gitlab-ci.yml` file. You could choose not to install lefthook locally, or supress lefthook by adding `--no-verify` to your git commands. However, at the moment you push something to remote, the gitlab-ci pipeline will run, which will build the `Dockerfile` that contains all dependencies (lefthook, lychee, pdm, etc) and it will check all your files, not just the staged files.

If the pipeline fails, you can see that on gitlab under `build` and then `Pipelines` or `Jobs`. Clicking on the status will give you a log of what tests passed and what failed, if any.
