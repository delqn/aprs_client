#!/usr/bin/perl

use Ham::APRS::FAP qw(parseaprs);
use MIME::Base64;
#my $aprspacket = 'OH2RDP>BEACON,OH2RDG*,WIDE:!6028.51N/02505.68E#PHG7220/RELAY,WIDE, OH2AP Jarvenpaa';

my $aprspacket = decode_base64($ARGV[0]);
my %packetdata;
my $retval = parseaprs($aprspacket, \%packetdata);

print "\{";

if ($retval == 1) {
        # decoding ok, do something with the data
	while (my ($key, $value) = each(%packetdata)) {
	    if (($key ne "body") && ($key ne "origpacket")){
		print "\"$key\": \"$value\",";}
	}
} else {
	print "\"Parsing failed\": \"$packetdata{resultmsg} ($packetdata{resultcode})\"";
}
print "\"blah\":\"bleh\"}";
