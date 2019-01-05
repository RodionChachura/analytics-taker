# $1 = function name
# $2 = bucket name
# $3 = bucket object name (zipped folder)

mkdir package
cp -a src/. package/

while read lib; do
  pip3 install $lib -t ./package
done <libs.txt

chmod -R +x ./package/
cd package
zip -r ../function.zip *
cd ..
rm -rf package

aws s3 cp $3 s3://$2/$3
aws lambda update-function-code --function-name $1 --s3-bucket $2 --s3-key $3