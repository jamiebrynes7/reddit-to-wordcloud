ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


package: package-execute-service package-front-end package-polling

package-execute-service:
	zip -j aws-execute-generation.zip common_lib.py aws_execute_generation.py 
	cd venv/lib/python3.6/site-packages && 	zip -x "*/__pycache__/*" -ur $(ROOT_DIR)/aws-execute-generation.zip *

package-front-end:
	zip -j aws-front-end.zip aws_front_end.py 
	cd venv/lib/python3.6/site-packages && 	zip -x "*/__pycache__/*" -ur $(ROOT_DIR)/aws-front-end.zip *

package-polling:
	zip -j aws-polling.zip aws_polling.py 
	cd venv/lib/python3.6/site-packages && 	zip -x "*/__pycache__/*" -ur $(ROOT_DIR)/aws-polling.zip *

clean:
	rm aws*.zip
	rm -rf ./__pycache__