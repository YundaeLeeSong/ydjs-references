#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

# This script automates the process of finding and consolidating files.
# It recursively searches for files with "resume" in their name (case-insensitive),
# copies them to an 'out' directory, and logs their original absolute paths.
# If files with the same name are found, it renames them to avoid overwriting.

# --- Standard Perl Modules ---
# File::Find: For traversing directory trees.
# File::Copy: For copying files.
# Cwd: For resolving absolute paths (Cross-platform way to get 'current working directory').
# File::Spec: For constructing platform-independent file paths.
# File::Basename: For parsing file paths.
use File::Find;
use File::Copy qw(copy);
use Cwd qw(abs_path);
use File::Spec;
use File::Basename qw(basename fileparse);

# --- Configuration ---
# The directory where matching files will be copied.
my $output_dir = 'out';
# The file that will list the absolute paths of all copied files.
my $log_file_name = 'out.txt';
# The directory to start the search from. '.' means the current directory.
my $search_dir = '.';
# The keyword to look for in filenames (case-insensitive).
my $search_term = 'resume';

# --- Main Script Logic ---

# 1. Ensure the output directory exists.
# The '-d' operator checks if a directory exists.
unless (-d $output_dir) {
    print "Creating output directory: '$output_dir'...\n";
    # Create the directory, or terminate with an error message if it fails.
    mkdir $output_dir or die "Error: Could not create directory '$output_dir': $!\n";
}

# 2. Find all files matching the criteria.
# We'll store the relative paths of matching files in this array.
my @resume_files;

# The find() function from File::Find takes a subroutine as its first argument
# and the starting directory as its second.
find(
    sub {
        # This subroutine is executed for every file and directory found.
        # The current item's name is in the default variable: $_

        # We proceed only if the item is a file ('-f') and its name
        # matches our search term in a case-insensitive way ('/i').
        if ( -f $_ && /$search_term/i ) {
            # $File::Find::name contains the full relative path (e.g., 'subdir/my_resume.pdf').
            # We will store this relative path and resolve its absolute path later.
            push @resume_files, $File::Find::name;
        }
    },
    $search_dir
);

# 3. Exit gracefully if no matching files were found.
unless (@resume_files) {
    print "No files containing the word '$search_term' were found.\n";
    exit;
}

# 4. Prepare and open the log file for writing.
# File::Spec->catfile is a portable way to join path components (like 'out/out.txt').
my $log_file_path = File::Spec->catfile($output_dir, $log_file_name);
open my $log_fh, '>', $log_file_path
  or die "Error: Could not open log file '$log_file_path' for writing: $!\n";

print "Found " . scalar(@resume_files) . " resume file(s). Copying to '$output_dir' and logging...\n";

# 5. Iterate over the found files, copy them, and log their paths.
foreach my $relative_path (@resume_files) {
    my $original_basename = basename($relative_path);
    my $dest_path = File::Spec->catfile($output_dir, $original_basename);

    # Check if a file with the same name already exists in the destination.
    # If so, this is a "duplicated filename" and we must rename it.
    if (-e $dest_path) {
        # Apply the renaming convention: filename-parentdir.ext
        my ($name, $path, $suffix) = fileparse($relative_path, qr/\.[^.]*/);
        my $parent_dir = basename($path);

        # Only create a new name if there is a parent directory to use.
        if ($parent_dir ne '.' && $parent_dir ne '') {
            my $new_basename = "$name-$parent_dir$suffix";
            $dest_path = File::Spec->catfile($output_dir, $new_basename);

            # Final check: if the *new* name also exists, we have a collision
            # (e.g., from 'a/notes/cv.doc' and 'b/notes/cv.doc').
            # In this case, warn the user and skip this file to prevent data loss.
            if (-e $dest_path) {
                warn "Warning: Collision after renaming for '$relative_path'. Destination '$dest_path' already exists. Skipping.\n";
                next; # Skip to the next file in the loop
            }
        } else {
            # This is a duplicate file in the root of the search directory.
            # We have no parent directory to create a unique name, so we must skip it.
            warn "Warning: Duplicate filename '$original_basename' found in a root directory. Cannot create a unique name. Skipping.\n";
            next; # Skip to the next file in the loop
        }
    }

    # Use the determined destination path for copying.
    if ( copy($relative_path, $dest_path) ) {
        # If copy was successful, resolve the absolute path for the log file.
        my $absolute_path = abs_path($relative_path);
        if (defined $absolute_path) {
            print $log_fh "$absolute_path\n";
        } else {
            # As a fallback, log the relative path if resolution fails.
            warn "Warning: Could not get absolute path for '$relative_path'. Logging relative path instead.\n";
            print $log_fh "$relative_path\n";
        }
    }
    else {
        # If copy failed, print a warning to the console but continue with the script.
        warn "Warning: Could not copy '$relative_path' to '$dest_path': $!\n";
    }
}

# 6. Close the log file handle to ensure all data is written to disk.
close $log_fh;

print "Process complete.\n";
print "Log file created at: '$log_file_path'\n";

