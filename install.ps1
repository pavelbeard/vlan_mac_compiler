Add-Type -AssemblyName PresentationFramework

$python_path = $env:path
$run = $PSScriptRoot + "\run.ps1"

if ($python_path -like "*Python*")
{
    CreateLink
}
else
{
    # установка python, если нет его на машине
    $python_exe = "$PSScriptRoot\python_installer"
    Set-Location -Path $python_exe

    try
    {
        Start-Process -FilePath "$python_exe\python-3.10.5-amd64.exe" -Verb RunAs -Wait

        CreateLink

        [System.Windows.MessageBox]::Show(
            "Установка завершена.
            Ярлык скрипта vlan_mac_compiler находится на рабочем столе.")
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

function CreateLink {
    $ShortcutPath = "C:\Users\$env:UserName\Desktop\vlan_mac_compiller.lnk"
    $WScriptObj = New-Object -ComObject ("WScript.Shell")
    $shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
    $shortcut.TargetPath = $run
    $shortcut.Save()
}