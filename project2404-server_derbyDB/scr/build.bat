@echo off
SET "os_type=%OS%"
echo Start installing, your operating system type: %os_type%
SET "JAVA=..\Java"
SET "JLIB=lib"
IF EXIST "%JAVA%" (
    rmdir /s /q "%JAVA%"
)
IF EXIST "%JLIB%" (
    rmdir /s /q "%JLIB%"
)
mkdir "%JAVA%"
mkdir "%JLIB%"
curl -L -o "%JAVA%\openjdk-11.zip" "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_windows-x64_bin.zip"
curl -L -o "%JLIB%\apache-derby-10.14.2.0.zip" "https://archive.apache.org/dist/db/derby/db-derby-10.14.2.0/db-derby-10.14.2.0-bin.zip"
powershell -Command "Expand-Archive -Path '%JAVA%\openjdk-11.zip' -DestinationPath '%JAVA%'"
powershell -Command "Expand-Archive -Path '%JLIB%\apache-derby-10.14.2.0.zip' -DestinationPath '%JLIB%'"
del /f /q "%JAVA%\openjdk-11.zip"
del /f /q "%JLIB%\apache-derby-10.14.2.0.zip"
powershell -Command "(Get-Content '%JAVA%\jdk-11.0.2\lib\security\default.policy' -Raw) -replace 'grant codeBase', 'grant { permission java.security.AllPermission; };`n grant codeBase' | Set-Content '%JAVA%\jdk-11.0.2\lib\security\default.policy'"
SET "JVM=..\Java\jdk-11.0.2\bin"
SET "PATH=%cd%\%JVM%;%PATH%"
java -jar App.jar
rmdir /s /q res\db
del /f /q derby.log
rmdir /s /q "%JAVA%"
rmdir /s /q "%JLIB%"
echo Clean target completed.