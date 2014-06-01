#!/bin/bash
# Set the JAR name
jar="$1"

# Loop through the classes (everything ending in .class)
for class in $(jar -tf $jar | grep '.class'); do 
    # Replace /'s with .'s
    class=${class//\//.};
    # javap
    javap -public -classpath $jar ${class//.class/}; 
done
