$day = 4
$downloadToPath = "D:\git\adventofcode2021\in\$day.txt"
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("session", "53616c7465645f5fc754b2eba2d8dcb8675d9af72754df96ed952695a1fc55850d59966e82e8419eba312e96bc89bebbc84c2ce9087dd5b66b8203c106be6177", "/", ".adventofcode.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://adventofcode.com/2021/day/$day/input" -WebSession $session -OutFile $downloadToPath
