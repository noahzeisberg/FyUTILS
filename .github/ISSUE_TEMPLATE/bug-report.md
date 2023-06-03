name: Bug Report
description: Report a bug, that you either don't have a cue how it's happening or a bug whose solution you already know.
title: "[BUG] <issue name>"
labels: bug
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

- type: textarea
  id: howtoreplicate
  attributes:
  label: Possible fixes or solutions
  description: List any possible fixes/suggestions that you have in mind that could solve this issue.
  validations:
  required: true

- type: textarea
  id: extrainformation
  attributes:
  label: Additional information
  description: Is there anything else we should know about this bug?