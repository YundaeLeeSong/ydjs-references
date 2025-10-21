JDK="../Java"
LIB="lib"
# Remove existing 'lib' directory if it exists
rm -rf lib

# Create a directory to store JavaFX in the current working directory
mkdir lib

# Download JavaFX 11 SDK into the 'lib' subdirectory
curl -L -o lib/javafx-sdk-11.tar.gz https://download2.gluonhq.com/openjfx/11.0.2/openjfx-11.0.2_linux-x64_bin-sdk.zip

# Extract the downloaded archive
unzip lib/javafx-sdk-11.tar.gz -d lib/

# Clean up the archive file
rm lib/javafx-sdk-11.tar.gz




# Create a directory to store JDK in the current working directory
mkdir jdk

# Download JDK 11 for Linux into the 'jdk' subdirectory
curl -L -o "jdk/openjdk-11-linux.tar.gz" "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz"

# Extract the downloaded archive
tar -xvzf "jdk/openjdk-11-linux.tar.gz" -C jdk/ --strip-components=1

# Clean up the archive file
rm "jdk/openjdk-11-linux.tar.gz"

# Display completion message
echo "OpenJDK 11 for Linux has been downloaded and installed in the 'jdk' directory."
