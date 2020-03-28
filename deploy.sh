gcloud builds submit --tag gcr.io/utopian-button-227405/python-grpc-quran:$SHA .

kubectl apply -f ./deployment.yaml
kubectl set image deployments/quran-grpc python-grpc-quran=gcr.io/utopian-button-227405/python-grpc-quran:$SHA