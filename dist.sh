#!/bin/sh

FOLDER=dist
FILE=dist.zip
PCKG=pckg.zip

echo "Cleaning $FOLDER folder & old builds"
rm -rf $FOLDER
rm -f $FILE
mkdir -p $FOLDER
#echo "Installing pip dependencies.."
#pip install -r requirements.txt -t $FOLDER/ > /dev/null
# copy ec2 installs
cp $PCKG $FILE

cp -r lib $FOLDER/lib
cp *.py $FOLDER/

echo "Zipping folder.."
cd $FOLDER
zip -qr ../$FILE *
cd ..

echo "Done"
