Set-ExecutionPolicy -Scope CurrentUser Bypass

cd -Path "$PSScriptRoot\local-venv\Scripts"
& ".\activate"
cd -Path "..\.."
Start-Process -FilePath "$PSScriptRoot\local-venv\Scripts\python.exe" -Args ".\main_vlan.py"
Pause