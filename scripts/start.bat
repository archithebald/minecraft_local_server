@echo off
setlocal enabledelayedexpansion

:: Default values
set RAM_MAX=2048
set RAM_MIN=1024
set JAR_PATH="C:\Users\djegh\Desktop\GenerateMinecraftServer\server\server.jar"

:: Check for user-provided parameters
if not "%~1"=="" set RAM_MAX=%1
if not "%~2"=="" set RAM_MIN=%2
if not "%~3"=="" set JAR_PATH=%3

:: Start the server
java -Xmx%RAM_MAX%M -Xms%RAM_MIN%M -jar %JAR_PATH% nogui