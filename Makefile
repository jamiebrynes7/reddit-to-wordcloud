package:
	zip -j aws-lambda-package.zip common_lib.py aws_lambda_service.py 
	cd venv/lib/python3.5/site-packages && 	zip -x "*/__pycache__/*" -ur ../../../../aws-lambda-package.zip * 

clean:
	rm aws-lambda-package.zip

