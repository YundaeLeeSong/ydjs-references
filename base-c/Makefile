# This is a minimal Makefile for GNU Make.
#
# It defines two "targets":
# 1. 'all': The default target that builds the program.
# 2. 'clean': A target to remove compiled files.

# Set the C compiler. 'gcc' is the standard.
CC = gcc

# Define the name of our final executable
TARGET = hello

#
# Default Target: 'all'
# This is the target that 'make' will build if you just type 'make'.
# It "depends" on the $(TARGET), so 'make' will look for
# a rule to build $(TARGET) next.
#
all: $(TARGET)

#
# Build Target: $(TARGET)
# This rule tells 'make' how to build the file named in $(TARGET).
# It "depends" on the .c file with the same name.
#
# $< is an automatic variable meaning "the first dependency" (hello.c)
# $@ is an automatic variable meaning "the target name" (hello)
#
$(TARGET): $(TARGET).c
	$(CC) $< -o $@
	@echo "Build complete. Run with ./${TARGET}"

#
# Clean Target: 'clean'
# This rule is not for building, but for cleaning up.
# It removes the compiled executable.
# The '-f' flag for 'rm' (remove) means "force," so it
# won't error if the file doesn't exist.
#
clean:
	@echo "Cleaning up build files..."
	rm -f $(TARGET) $(TARGET).exe

#
# Phony Targets
# We declare 'all' and 'clean' as .PHONY.
# This tells 'make' that these are not actual files.
# It prevents 'make' from getting confused if a file
# named 'clean' ever exists.
#
.PHONY: all clean