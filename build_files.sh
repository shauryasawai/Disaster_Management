
echo "BUILD START"
python3.9 -m pip install -r requirements.txt --target ./package
cd package
zip -r9 ../function.zip .
cd ..
zip -r9 function.zip .
echo "BUILD END"
