if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell -Verb runAs -ArgumentList "Invoke-RestMethod https://raw.githubusercontent.com/noahonfyre/FyUTILS/master/get.ps1 | Invoke-Expression"
    Exit
}

Write-Output "Starting FyUTILS installation..."
Write-Output "Setting up variables..."
$fileName = "FyUTILS.exe"
$folderPath = Join-Path $env:USERPROFILE ".fy"
$filePath = Join-Path $folderPath $fileName
$githubApiUrl = "https://api.github.com/repos/noahonfyre/FyUTILS/releases/latest"

Write-Output "Creating local file..."
New-Item -ItemType Directory -Path $folderPath -Force | Out-Null

Write-Output "Fetching API information..."
$releaseInfo = Invoke-RestMethod -Uri $githubApiUrl

Write-Output "Processing data..."
$fileDownloadUrl = $releaseInfo.assets | Where-Object { $_.name -eq $fileName } | Select-Object -ExpandProperty browser_download_url

Write-Output "Downloading file from GitHub..."
Invoke-WebRequest -Uri $fileDownloadUrl -OutFile $filePath

Write-Output "Checking for environment variable..."
if (-not ($folderPath -in $env:Path)) {
    Write-Output "Backing up PATH to C:\PATHBACKUP.TXT..."
    Out-File -FilePath "C:\PATHBACKUP.TXT" -InputObject $env:Path -Force -Encoding utf8
    Write-Output "Adding directory to your environment variables..."
    [Environment]::SetEnvironmentVariable("Path", $env:Path + ";"$folderPath, "Machine")
}

Write-Output "Excluding FyUTILS directory from Windows Defender..."
if (Get-Command -ErrorAction SilentlyContinue Get-MpPreference) {
    $existingExclusions = Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
    if ($existingExclusions -contains $folderPath) {
        Write-Output "Exclusion for $folderPath already exists. No changes made."
    }
    else {
        $existingExclusions += $folderPath
        Set-MpPreference -ExclusionPath $existingExclusions
        Write-Output "Exclusion for $folderPath added successfully."
    }
}
else {
    Write-Warning "Windows Defender is not installed or not available on this system."
}

Write-Output " "
Write-Output "Installation of FyUTILS complete! Please consider starring this repository."
Write-Output "https://github.com/noahonfyre/FyUTILS"
Write-Output " "
Pause