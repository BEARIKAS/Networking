Get-ChildItem C:\Users -Recurse -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object FullName, @{Name="SizeMB";Expression={"{0:N2}" -f ($_.Length/1MB)}} -First 10