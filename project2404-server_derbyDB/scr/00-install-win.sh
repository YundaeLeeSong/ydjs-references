# Remove existing directory if it exists
if [ -d "$JAVA" ]; then
    rm -rf "$JAVA"
fi
if [ -d "$JLIB" ]; then
    rm -rf "$JLIB"
fi

# create directories
mkdir "$JAVA"
mkdir "$JLIB"
mkdir "$JLIB/kotlin-stdlib-1.6.10"
mkdir "$JLIB/ojdbc-11"

# Download archives
# -L: follow HTTP redirects and download the file from the new location.
# -o <file>: specify the name of the file you want to save the downloaded content to.
# [substitute for -o] -O: save the downloaded file with the same name as the filename in the URL.
curl -L -o "$JAVA/openjdk-11.0.2.zip" "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_windows-x64_bin.zip"
curl -L -o "$JAVA/kotlin-compiler-1.6.10.zip" "https://github.com/JetBrains/kotlin/releases/download/v1.6.10/kotlin-compiler-1.6.10.zip"
curl -L -o "$JAVA/apache-ant-1.10.14.zip" "https://archive.apache.org/dist/ant/binaries/apache-ant-1.10.14-bin.zip"
curl -L -o "$JLIB/kotlin-stdlib-1.6.10/kotlin-stdlib-1.6.10.jar" https://repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-stdlib/1.6.10/kotlin-stdlib-1.6.10.jar
curl -L -o "$JLIB/javafx-sdk-11.0.2.zip" "https://download2.gluonhq.com/openjfx/11.0.2/openjfx-11.0.2_windows-x64_bin-sdk.zip"
curl -L -o "$JLIB/db-derby-10.14.2.0.zip" "https://archive.apache.org/dist/db/derby/db-derby-10.14.2.0/db-derby-10.14.2.0-bin.zip"
curl -L -o "$JLIB/ojdbc-11/ojdbc11.jar" "https://download.oracle.com/otn-pub/otn_software/jdbc/233/ojdbc11.jar"


# Extract the downloaded archives
unzip "$JAVA/openjdk-11.0.2.zip" -d "$JAVA"
unzip "$JAVA/kotlin-compiler-1.6.10.zip" -d "$JAVA"
unzip "$JAVA/apache-ant-1.10.14.zip" -d "$JAVA"
unzip "$JLIB/javafx-sdk-11.0.2.zip" -d "$JLIB"
unzip "$JLIB/db-derby-10.14.2.0.zip" -d "$JLIB"

# Clean up the archive files
rm "$JAVA/openjdk-11.0.2.zip"
rm "$JAVA/kotlin-compiler-1.6.10.zip"
rm "$JAVA/apache-ant-1.10.14.zip"
rm "$JLIB/javafx-sdk-11.0.2.zip"
rm "$JLIB/db-derby-10.14.2.0.zip"