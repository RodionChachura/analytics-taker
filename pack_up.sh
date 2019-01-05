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