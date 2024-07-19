# FyUTILS

Welcome to the [FyUTILS](https://github.com/noahonfyre/FyUTILS) wiki page!

We’ll walk you through the installation process of FyUTILS, how to customize your instance, and several ways to extend it.

# Table of Contents

<!-- TOC -->
* [FyUTILS](#fyutils)
* [Table of Contents](#table-of-contents)
* [Disclaimer](#disclaimer)
* [Installation](#installation)
    * [Troubleshooting Guide](#troubleshooting-guide)
  * [Used in FyUTILS](#used-in-fyutils)
    * [Languages](#languages)
    * [Tools](#tools)
  * [Credits and Acknowledgement](#credits-and-acknowledgement)
<!-- TOC -->

# Disclaimer

By proceeding, you acknowledge that you have read, understood, and agreed to comply with our [terms and conditions](https://github.com/noahzeisberg/FyUTILS/blob/master/TERMS.md). Failure to adhere to these terms may result in legal consequences. If you do not agree with these terms, refrain from downloading, installing, or using FyUTILS.

# Installation

To install FyUTILS, ensure you're running the latest versions of Windows and Windows Terminal. Also, you should be using an account with administrator permissions.

1. **Setting up the execution policy:**
   Open your PowerShell and paste the following command to bypass the remote code execution policy. This step is necessary for the installation to proceed.
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass -Force
   ```

2. **Installing FyUTILS:**
   Execute the following command in the current PowerShell session to start the installation:
   ```powershell
   irm https://noahonfyre.github.io/FyUTILS/get.ps1 | iex
   ```

3. **Starting FyUTILS:**
   To run FyUTILS, execute the `fyutils` command in a new shell session.


### Troubleshooting Guide
If something doesn't work, or you can't get FyUTILS to start, try the following steps:

1. **Restart your shell sessions:**

   Ensure you restart all your shell sessions. This includes closing all instances of PowerShell and Command Prompt, as they need to register the update to the system variables.

2. **Restart your PC:**

   If restarting the shell sessions doesn't resolve the issue, try restarting your PC. This will force all processes to restart and retrieve the most recent system variables.

3. **Check your PATH variable:**

   Open your search bar and search for `PATH`. Click on the section `Environment Variables`. Check the `PATH` variable for the path `C:\\Users\\%USERNAME%\\.fyutils`. If the path doesn't exist, add it to the variable.

4. **Get technical support:**

   If you need further help with the installation or setup of FyUTILS, you can check out our [discord server](https://dsc.gg/nyronium).


## Used in FyUTILS

### Languages
Here’s a list of every programming language involved in FyUTILS.

| Language:  | Use case:                       |
|------------|---------------------------------|
| Go         | Main Application                |
| Batch      | System Interactions             |
| PowerShell | Installer & System Interactions |
| Markdown   | Documentation                   |

### Tools

Here’s a list of tools, I use to develop and maintain FyUTILS.

| Tool:                                      | Use case:                                 |
|--------------------------------------------|:------------------------------------------|
| [Goland](https://www.jetbrains.com/go/)    | Go & PowerShell Development               |
| [GitHub](https://github.com)               | Version Control, Publishing, Distribution |
| [GitHub API](https://docs.github.com/rest) | Updating System                           |
| [Notion](https://notion.so)                | Documentation & Writing                   |
| [VS Code](https://vscode.dev)              | Additional Development                    |

## Credits and Acknowledgement
A huge thank you to all [contributors](https://github.com/noahzeisberg/FyUTILS/graphs/contributors) of this project. ♥️