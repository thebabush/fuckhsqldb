# Java JAR methods parser

This is a simple shell script + python script to parse a JAR file and extract only public static methods with a pre-defined set of arguments and return types.

## Usage

> ./parser.sh /path/to/jar/file 2> /dev/null | ./filter.py > output.txt

## Why

I wrote this to find out what methods I could call from inside HSQLDB (using the 'CALL' statement) for security purposes... In case you're wondering, I found nothing interesting.
