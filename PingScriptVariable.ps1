# If arguments are given, use them as hosts
# Otherwise try to load from hosts.txt
# Or fall back to defaults

param (
    [string[]]$Hosts
)

if (-not $Hosts) {
    if (Test-Path "hosts.txt") {
        $Hosts = Get-Content "hosts.txt"
    }
    else {
        $Hosts = @("8.8.8.8", "1.1.1.1")
    }
}

foreach ($h in $Hosts) {
    try {
        if (Test-Connection -ComputerName $h -Count 1 -Quiet -ErrorAction SilentlyContinue) {
            Write-Host "[UP]   $h is reachable"
        }
        else {
            Write-Host "[DOWN] $h is not reachable"
        }
    }
    catch {
        Write-Host "[ERROR] Could not check $h : $_"
    }
}