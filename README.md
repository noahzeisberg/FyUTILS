# FyUTILS

Welcome to the [FyUTILS](https://github.com/noahonfyre/FyUTILS) wiki page!

We’ll walk you through the installation process of FyUTILS, how to customize your instance, and several ways to extend it.

# Table of Contents



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