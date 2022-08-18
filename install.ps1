$python_path = $env:path
if ($python_path -like "*Python*")
{
    $run = $PSScriptRoot + "\run.ps1"
    $ShortcutPath = "C:\Users\$env:UserName\Desktop\vlan_mac_compiller.lnk"
    $WScriptObj = New-Object -ComObject ("WScript.Shell")
    $shortcut = $WscriptObj.CreateShortcut($ShortcutPath)
    $shortcut.TargetPath = $run
    $shortcut.Save()

}
else
{

}