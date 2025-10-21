#!/usr/bin/perl
use strict;
use warnings;
use File::Copy;
use File::Path qw(make_path);
use Cwd;
use File::Find;
use File::Basename;
use File::Spec;  # To handle paths more robustly

# Step 1: Get the current directory and set up the temp_dir
my $current_dir = getcwd();
my $temp_dir = "$current_dir/out";
make_path($temp_dir) unless -d $temp_dir;

# Step 2: Prompt the user for the title
print "Enter the prefix for all the filenames: ";
my $title = <STDIN>;  # Read user input
chomp($title);        # Remove the newline character at the end of the input
print "The title is '$title'.\n";

# Step 3: Recursively find all files in the directory and subdirectories
my @files;

find(sub {
    # Only add files (not directories)
    if (-f $_ && $_ ne $0) {
        # Use File::Spec to ensure the full path is correct
        my $full_path = File::Spec->rel2abs($File::Find::name);
        push @files, $full_path;
    }
}, $current_dir);

# Count the number of files
my $file_count = scalar(@files);

# Determine the number of digits needed for padding
my $digit_format = length($file_count);

# Step 4: Process files and copy to temp folder with renamed filenames
my $index = 1;
foreach my $file (@files) {
    # Extract filename (without directory structure)
    my $name = fileparse($file);  # Extracts just the filename (basename)
    my ($basename, $extension) = $name =~ /^(.*?)(\.[^.]+)?$/;
    
    $extension //= '';  # Handle files with no extension

    # Step 2: Replace invalid characters (anything except A-Z, a-z, 0-9, and .) with "_"
    $basename =~ s/[^a-zA-Z0-9.]/_/g;

    # Step 3: Collapse multiple underscores into a single "_"
    $basename =~ s/_+/_/g;

    # Step 4: Remove leading and trailing underscores
    $basename =~ s/^_+|_+$//g;

    # Step 5: Convert name and extension to lowercase
    $basename = lc($basename);
    $extension = lc($extension);

    # Step 6: Format the index with leading zeros based on the digit format
    my $formatted_index = sprintf("%0*d", $digit_format, $index);

    # Step 7: Combine formatted index, processed name, and extension
    my $new_name = $title . $formatted_index . '-' . $basename . $extension;

    # Step 8: Print out the file details for debugging
    print "Processing file: $file\n";
    print "basename: $basename$extension\n";

    # Step 9: Copy the file to the temp folder with the new name
    if ($extension !~ /bat|pl/i) {  # If it does not contain `bat` or `pl`
        copy($file, "$temp_dir/$new_name") or die "Copy failed: $!";
    }

    $index++;
}

print "Files processed and copied to $temp_dir\n";

# Step 10: Ask the user if they want to continue
print "Do you want to continue? (y/n): ";
my $response = <STDIN>;
chomp($response);

if ($response eq 'y' || $response eq 'Y') {
    print "You chose to continue.\n";
} else {
    print "You chose not to continue.\n";
}
