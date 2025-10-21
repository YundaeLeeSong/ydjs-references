#!/usr/bin/perl
use strict;
use warnings;

# Print "Hello, World!" message
print "Hello, World! (Perl)\n";

# Print the HOME directory
print "HOME directory: $ENV{USERPROFILE}\n";

# Print the current directory
use Cwd;
my $current_dir = getcwd();
print "Current directory: $current_dir\n";

# Pause the program
print "Press Enter to continue...\n";
<STDIN>;
