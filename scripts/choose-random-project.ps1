$programmingLanguage = @("CSharp", "Javascript", "Python", "Rust", "Typescript", "Elm") | Get-Random
$project = @(1..28) | Get-Random

Write-Host "Code Project $project in $programmingLanguage..."