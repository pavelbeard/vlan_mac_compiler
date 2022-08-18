Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

cd -Path $PSScriptRoot
python.exe main_vlan.py
Pause