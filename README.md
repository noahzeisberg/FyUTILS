# FyUTILS

Welcome to the [FyUTILS](https://github.com/noahonfyre/FyUTILS) wiki page!

We’ll walk you through the installation process of FyUTILS, how to customize your instance, and several ways to extend it.

## Table of Contents

<!-- TOC -->
* [FyUTILS](#fyutils)
  * [Table of Contents](#table-of-contents)
  * [Disclaimer](#disclaimer)
  * [Features](#features)
    * [Reliability](#reliability)
    * [Customizability](#customizability)
    * [Extensibility](#extensibility)
  * [Installation](#installation)
    * [Creating a Terminal profile](#creating-a-terminal-profile)
    * [Troubleshooting Guide](#troubleshooting-guide)
  * [Used in FyUTILS](#used-in-fyutils)
    * [Languages](#languages)
    * [Tools](#tools)
  * [Credits and Acknowledgement](#credits-and-acknowledgement)
<!-- TOC -->

## Disclaimer

By proceeding, you acknowledge that you have read, understood, and agreed to comply with our [terms and conditions](https://github.com/NoahOnFyre/FyUTILS/blob/master/TERMS.md). Failure to adhere to these terms may result in legal consequences. If you do not agree with these terms, refrain from downloading, installing, or using FyUTILS.

## Features

Here’s a brief overview of the features, FyUTILS has to offer. If you’d like to skip this part click here to get to [the installation](#installation).

### Reliability

FyUTILS is actively developed to ensure a seamless user experience. We promptly address reported bugs and welcome feature requests from our community. Your input, whether bug reports or feature ideas, is crucial in shaping FyUTILS. Join our forums to engage in discussions and contribute to the tool's ongoing evolution. Rest assured, our commitment to regular updates and improvements is unwavering. Thank you for being part of the FyUTILS community and helping us, building an even more robust and quality tool in upcoming releases.

### Customizability

You can customize FyUTILS through [Themes](#FyUTILS). Themes can change the overall appearance of FyUTILS through simple JSON configuration files. They can be installed via the FUEL manager, just like normal FUELS.

###  Extensibility

FyUTILS is extendable through so-called **FUELS** (*FyUTILS Extensions and Libraries*), which can be installed via the `fuel` command. It also offers a wide range of support through the integrated execution support of executables in the PATH variable.

## Installation

To install FyUTILS, ensure you're running the latest versions of Windows, Windows Terminal, and Windows Console Host. Also, you should be using an account with administrator permissions.

1. **Install a Nerd Font:**

   Download and install a [Nerd Font](https://www.nerdfonts.com/font-downloads) and apply it to your Terminal. This step is crucial for the installation, as it provides the icons used in FyUTILS.

2. **Setting up the execution policy:**

   Open your PowerShell and paste the following command to bypass the remote code execution policy. This step is necessary for the installation to proceed.


```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force
```

1. **Installing FyUTILS:**

   Execute the following command in the current PowerShell session to start the installation:


```powershell
irm https://noahonfyre.github.io/FyUTILS/get.ps1 | iex
```

1. **Starting FyUTILS:**

   To run FyUTILS, execute the `fyutils` command in a new shell session.


### Creating a Terminal profile

If you’re going to use FyUTILS very often, you may like to create a Terminal profile for FyUTILS:

1. **Open Windows Terminal:**

   Launch the Windows Terminal application on your computer. You can find it in the Start menu or by searching for **“Windows Terminal”** in the search bar.

2. **Access Settings:**

   Click on the downward arrow icon located in the title bar or press `Ctrl` + `,` to open the Settings menu.

3. **Navigate to Profiles:**

   In the Settings menu, select the **“Profiles”** tab on the left sidebar.

4. **Create a New Profile:**

   Scroll down to the “Add a profile” section. Click on the **“Add”** button to create a new profile.

5. **Configure the New Profile:**

   Change the name of the Profile to **“FyUTILS”** and the command line to `fyutils`.

6. **Save Changes:**

   Once you have configured the new profile, click the **“Save”** button to apply the changes.

7. **Close and Reopen Windows Terminal:**

   Close the Settings menu and restart Windows Terminal to see your new profile. You can switch between profiles using the tabs at the top of the terminal window.

### Troubleshooting Guide

If something doesn't work, or you can't get FyUTILS to start, try the following steps:

1. **Restart your shell sessions:**

   Ensure you restart all your shell sessions. This includes closing all instances of PowerShell and Command Prompt, as they need to register the update to the system variables.

2. **Restart your PC:**

   If restarting the shell sessions doesn't resolve the issue, try restarting your PC. This will force all processes to restart and retrieve the most recent system variables.

3. **Check your PATH variable:**

   Open your search bar and search for PATH. Check your PATH for the path “C:\Users\USERNAME\.fyutils”. If the path doesn't exist, add it to the variable.

4. **Get technical support:**

   If you need further help with the installation or setup of FyUTILS, you can check out our [discord server](https://dsc.gg/nyronium).


## Used in FyUTILS

### Languages

Here’s a list of every programming language involved in FyUTILS.

| Language:   | Use case:                       |
|-------------|---------------------------------|
| Go (Golang) | Main Application                |
| Batch       | System Interactions             |
| PowerShell  | Installer / System Interactions |
| Markdown    | Documentation                   |

### Tools

Here’s a list of tools, I use to develop and maintain FyUTILS.

| Tool:              | Use case:                                 |
|--------------------|-------------------------------------------|
| Goland             | Go & PowerShell Development               |
| GitHub             | Version Control, Publishing, Distribution |
| GitHub API         | Updating System                           |
| Notion             | Documentation & Writing                   |
| Visual Studio Code | Additional Development                    |

## Credits and Acknowledgement

FyUTILS would not have been possible without the contributions from the open-source community. I am very grateful for their efforts and dedication. I would also like to thank the users for their valuable feedback, which has helped me improve and evolve this tool.

I would also like to thank JetBrains. Their IDEs have been instrumental in my work, providing me with an efficient and reliable platform for coding. Their innovative tools have greatly enhanced my productivity and I appreciate their contribution to this project. You can check out their IDEs [here](https://jetbrains.com).