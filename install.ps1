Set-ExecutionPolicy -Scope CurrentUser Bypass
Add-Type -AssemblyName PresentationFramework


$python_path = $env:path
$run = $PSScriptRoot + "\run.ps1"
$pkgs = "$PSScriptRoot\packages"
$ShortcutPath = "C:\Users\$env:UserName\Desktop\vlan_mac_compiller.lnk"
$local_env = "$PSScriptRoot\local-venv"

function Create-Link {
    
    $WScriptObj = New-Object -ComObject ("WScript.Shell")
    $shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
    $shortcut.TargetPath = $run
    $shortcut.Save()
}

function Setup-Packages {
    python.exe -m venv $local_env
    Set-Location -Path "$local_env\Scripts"
    & ".\activate"
    Set-Location -Path $pkgs
    Start-Process -FilePath "$local_env\Scripts\python.exe" -Args ".\setup.py"
}

if ($python_path -like "*Python*")
{
    if(-Not(Test-Path -Path $local_env))
    {
        Setup-Packages
    }

    if (-Not (Test-Path -Path $ShortcutPath -PathType Leaf))
    {
        Create-Link
        [System.Windows.MessageBox]::Show("Ярлык скрипта vlan_mac_compiler находится на рабочем столе.")
    }
}
else
{
    # установка python, если нет его на машине
    $python_exe = "$PSScriptRoot\python_installer"
    Set-Location -Path $python_exe

    try
    {
        Start-Process -FilePath "$python_exe\python-3.10.5-amd64.exe" -Verb RunAs -Wait

        if (Test-Path -Path $pkg)
        {
            cd -Path $pkg
            python.exe setup.py

            Create-Link

            [System.Windows.MessageBox]::Show(
                    "Установка завершена.
                    Ярлык скрипта vlan_mac_compiler находится на рабочем столе.")
        }
        else
        {
            throw "Путь $pkg не найден"
        }

    }
    catch [InvalidOperationException]
    {
        [System.Windows.MessageBox]::Show(
            "Установка прервана пользователем")
    }
#    catch [AuthenticationException]
#    {
#        [System.Windows.MessageBox]::Show(
#            "Неверные данные пользователя")
#    }
}

