Get-ChildItem C:\Users -Recurse -ErrorAction SilentlyContinue | 
    Where-Object { -not $_.PSIsContainer } |
    Sort-Object Length -Descending |
    Select-Object Name, @{Name="SizeMB";Expression={"{0:N2}" -f ($_.Length/1MB)}} -First 10