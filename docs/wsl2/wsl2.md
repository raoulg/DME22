# Using WLS2 on Windows

When creating software (including data scientists, even though some of them shy away from that idea) a common misconception is this is something between a programmer and their computer. However, writing code is much more a social process whereby others need to interact with your code. That also includes your future self, who will have forgotten what you did and why you did it.

This is why we want to encourage you to use a UNIX environment, even if you are on Windows. The reality is that

- most of the tools that are used in the software development process are made for UNIX environments, and will work better there.
- most servers run Linux
- other programmers will be using Linux or macOS in addition to Windows, and ideally you want to work with all of them.

This is not a problem, because Windows has a very good solution for this. The easiest way to do this is to use the Windows Subsystem for Linux (WSL2). This is a Linux kernel that runs on Windows, and allows you to use Linux tools and environments. This is not a virtual machine, so it is very fast and easy to use.

In early days, you would need to enable virtualisation. I'm not a 100% sure (can you ever be, with windows...) but I think this is no longer required. If you run into problems installing WSL2, you could try to enable it\[^1\]

Then installation is as simple as in Powershell:

```PowerShell
wsl --install
```

This will install Ubuntu by default, which is fine. You will need to reboot your computer directly afterwards.
Now, you can open a terminal and you will be in a Linux environment.

> NOTE: some people might have a laptop that is constrained by the ICT department. They might run into problems like being unable to upgrade Linux when doing `sudo apt update`. You should solve this with your ICT department.

> NOTE 2: On windows, there are multiple terminals or shells, like the powershell. I will always refer to the linux terminal from your WSL2 installation in the rest of these docs. Later on, you can access that via VScode.

The most up to date manual for installing WSL2 can be found at the [Microsoft website](https://learn.microsoft.com/en-us/windows/wsl/install).

[Step by step tutorial with video](https://pureinfotech.com/install-wsl-windows-11/).

You can also find a tutorial [here to set it up with VScode](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)
