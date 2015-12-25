#!/usr/bin/perl
#!/usr/bin/env perl

use Ham::APRS::FAP qw(parseaprs);
#my $aprspacket = 'OH2RDP>BEACON,OH2RDG*,WIDE:!6028.51N/02505.68E#PHG7220/RELAY,WIDE, OH2AP Jarvenpaa';

my $aprspacket = $ARGV[0];

my %packetdata;
my $retval = parseaprs($aprspacket, \%packetdata);
if ($retval == 1) {
    # decoding ok, do something with the data
    print "\{";
    while (my ($key, $value) = each(%packetdata)) {
        print "\"$key\": \"$value\",";
    }
} else {
    warn "\"Parsing failed\": \"$packetdata{resultmsg} ($packetdata{resultcode})\"";
}
print "\}";
