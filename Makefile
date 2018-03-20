ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

package:
	zip -j aws-lambda-package.zip common_lib.py aws_lambda_service.py 
	cd venv/lib/python3.6/site-packages && 	zip -x "*/__pycache__/*" -ur $(ROOT_DIR)/aws-lambda-package.zip *

clean:
	rm aws-lambda-package.zip
	rm -rf ./__pycache__