name: Crash Report
description: Report a bug, that generated a crash.log file, which you can upload.
title: "[CRASH] <issue name>"
labels: crash
body:
- type: markdown
  attributes:
  value: "## Before you continue, please search our open/closed issues to see if a similar issue has been addressed."

- type: checkboxes
  attributes:
  label: I have searched through the issues and didn't find the solution to my problem.
  options:
    - label: Confirm
      required: true

- type: textarea
  id: description
  attributes:
  label: Bug description
  description: Short description of the bug that you found. Provide images/code if applicable.
  validations:
  required: true

- type: file
  id: crashfileupload
  attributes:
  label: Upload your crash.log file
  description: The file is located at: C:\Users\NAME\AppData\Roaming\FyUTILS\crash.log
  validations:
  required: true

- type: textarea
  id: extrainformation
  attributes:
  label: Additional information
  description: Is there anything else we should know about this bug?