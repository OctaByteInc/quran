gcloud builds submit --tag gcr.io/$PROJECT_ID/python-grpc-quran:$SHA .

kubectl apply -f ./deployment.yaml
kubectl set image deployments/quran-grpc python-grpc-quran=gcr.io/$PROJECT_ID/python-grpc-quran:$SHA