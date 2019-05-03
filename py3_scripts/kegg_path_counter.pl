#!/usr/bin/env perl

use strict;
use warnings;
use autodie;
use feature 'say';
use Getopt::Long;
use Pod::Usage;
use Cwd;

my %opts = get_opts();
my @args = @ARGV;

if ($opts{'help'} || $opts{'man'}) {
    pod2usage({
        -exitval => 0,
        -verbose => $opts{'man'} ? 2 : 1
    });
}

#Start script here.
#ARGV will hold input files from uproc

@ARGV or pod2usage("Please provide uproc files");

my $out_dir = $opts{'out_dir'} || cwd();
my $keggpaths = $opts{'lookup_key_file'} || 'kegg_to_path';

unless (-d $out_dir) {
    make_path($out_dir);
}

open my $keggpaths_fh, '<', $keggpaths;
my $count = 0;
my @print;

my @file_names = join"\t", @ARGV;
say "KEGG Pathway\t", @file_names;

my %kegg_path_lookup;
while (<$keggpaths_fh>) {
    chomp;
    my ($ko, $path) = split("\t");
    push @{$kegg_path_lookup{$ko}}, $path;
}
#use Data::Dumper;
#say Dumper(\%kegg_path_lookup);


my %path_sample_ct;
for my $file(@ARGV) {
    open my $fh, '<', $file;
    while (<$fh>) {
        chomp;
        my ($ko, $count) = split(',');
        for my $path1(@{$kegg_path_lookup{$ko}}) {
            if (!exists $path_sample_ct{$path1}{$file}) {
                $path_sample_ct{$path1}{$file} = $count;
            }
            else {
                my $current_count = $path_sample_ct{$path1}{$file};
                my $new_count = $count + $current_count;
                $path_sample_ct{$path1}{$file} = $new_count;
            }

        }
    }
}

for my $path2 (keys %path_sample_ct) {
    my @print= ();
    for my $file(@ARGV) { 
        my $count = $path_sample_ct{$path2}{$file} || 0;
        push (@print, $count);
    }
    say join "\t", $path2, @print;
}




# --------------------------------------------------
sub get_opts {
    my %opts;
    GetOptions(
        \%opts,
        'help',
        'man',
        'lookup_key_file=s',
        'out_dir=s',
    ) or pod2usage(2);

    return %opts;
}

__END__

# --------------------------------------------------

=pod

=head1 NAME

kegg_path_counter.pl - a UProC output library building script

=head1 SYNOPSIS

  kegg_path_counter.pl -l lookup_file file1 [file2...]

Options:

  --help            Show brief help and exit
  --man             Show full documentation
  --lookup_key_file File should be a csv file of pathways and ids

=head1 DESCRIPTION

This script  will create a tab delimited file with a library count of UProC files and correspodning KEGG pathways given a lookup file formatted as ID \t Description.



=head1 SEE ALSO

https://github.com/basmith89/megaplasmid_compare

=head1 AUTHOR

Brian A. Smith E<lt>basmith@email.arizona.eduE<gt>.

University of Arizona

=head1 COPYRIGHT

Copyright (c) 2018 basmith

This module is free software; you can redistribute it and/or
modify it under the terms of the GPL (either version 1, or at
your option, any later version) or the Artistic License 2.0.
Refer to LICENSE for the full license text and to DISCLAIMER for
additional warranty disclaimers.

=cut
