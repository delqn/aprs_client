## APRS packet ingestion tools

### Prerequisities and Installation
1. Install cpnam: `brew install cpanm`
2. Install perl modules: `sudo cpanm --installdeps .`


### Running it

Command line APRS client:
`echo user N0DEC pass 14999 vers ncat 1.0 filter b/N0DEC* | nc noam.aprs2.net 14580`
