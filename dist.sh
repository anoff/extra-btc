#!/bin/sh

FOLDER=dist/
FILE=dist.zip

echo "Cleaning $FOLDER folder & old builds"
rm -rf $FOLDER
rm -f $FILE
mkdir -p $FOLDER
echo "Installing pip dependencies.."
pip install -r requirements.txt -t $FOLDER > /dev/null

cp -r lib $FOLDER/lib
cp *.py $FOLDER

echo "Zipping folder.."
zip -r $FILE $FOLDER/* > /dev/null

echo "Done"
