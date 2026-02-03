train:
	mlflow run . \
	--env-manager local \
	--experiment-name 'customer churn' \
	--run-name cucumber \
	-P dataset=/home/tii/datasets/customer_churn/WA_Fn-UseC_-Telco-Customer-Churn.csv