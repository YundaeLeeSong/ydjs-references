#!/usr/bin/perl
use strict;
use warnings;
use File::Copy;
use File::Path qw(make_path);
use Cwd;

print "Enter the prefix of all the filenames: ";
my $title = <STDIN>;  # Read user input
chomp($title);        # Remove the newline character at the end of the input

print "The title is $title.\n";



# Get current directory and list all filenames
my $current_dir = getcwd();
opendir(my $dh, $current_dir) or die "Cannot open directory: $!";
my @files = grep { -f $_ && $_ ne $0 } readdir($dh);  # Exclude the script itself
closedir($dh);

# Count the number of files
my $file_count = scalar(@files);

# Determine the number of digits needed for padding
my $digit_format = length($file_count);

# Create a temp folder
my $temp_dir = "$current_dir/out";
make_path($temp_dir) unless -d $temp_dir;


# Process files and copy to temp folder with renamed filenames
my $index = 1;
foreach my $file (@files) {
    # Split filename into base name and extension
    my ($name, $extension) = $file =~ /^(.*?)(\.[^.]+)?$/;
    
    $extension //= '';  # Handle files with no extension

    # Step 1: Replace invalid characters (anything except A-Z, a-z, 0-9, and .) with "_"
    $name =~ s/[^a-zA-Z0-9.]/_/g;

    # Step 2: Collapse multiple underscores into a single "_"
    $name =~ s/_+/_/g;

    # Step 3: Remove leading and trailing underscores
    $name =~ s/^_+|_+$//g;

    # Step 4: Convert name and extension to lowercase
    $name = lc($name);
    $extension = lc($extension);

    # Step 5: Format the index with leading zeros based on the digit format
    my $formatted_index = sprintf("%0*d", $digit_format, $index);

    # Step 6: Combine formatted index, processed name, and extension
    my $new_name = $title . $formatted_index . '-' . $name . $extension;


    print "$extension\n";
    # Copy the file to the temp folder with the new name
    if ($extension !~ /bat|pl/i) { # does not contains either `bat` or `pl`?
        copy($file, "$temp_dir/$new_name") or die "Copy failed: $!";
    }

    $index++;
}

print "Files processed and copied to $temp_dir\n";


print "Do you want to continue? (y/n): ";
my $response = <STDIN>;
chomp($response);

if ($response eq 'y' || $response eq 'Y') {
    print "You chose to continue.\n";
} else {
    print "You chose not to continue.\n";
}