#!/bin/bash
os_type=$(uname)
echo "Start installing, your operating system type: $os_type"
JAVA="../Java"
JLIB="lib"
if [ -d "$JAVA" ]; then
    rm -rf "$JAVA"
fi
if [ -d "$JLIB" ]; then
    rm -rf "$JLIB"
fi
mkdir "$JAVA"
mkdir "$JLIB"
curl -L -o "$JAVA/openjdk-11.tar.gz" "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_osx-x64_bin.tar.gz"
curl -L -o "$JLIB/apache-derby-10.14.2.0.tar.gz" "https://archive.apache.org/dist/db/derby/db-derby-10.14.2.0/db-derby-10.14.2.0-bin.tar.gz"
tar -xzf "$JAVA/openjdk-11.tar.gz" -C "$JAVA/"
tar -xzf "$JLIB/apache-derby-10.14.2.0.tar.gz" -C "$JLIB/"
rm "$JAVA/openjdk-11.tar.gz"
rm "$JLIB/apache-derby-10.14.2.0.tar.gz"
JVM="../Java/jdk-11.0.2/bin"
export PATH="$(pwd)/${JVM}:$PATH"
java -jar App.jar
rm -rf res/db
rm -f derby.log
rm -rf "$JAVA"
rm -rf "$JLIB"
echo "Clean target completed."