# quran

# About gRPC
[https://cloud.google.com/endpoints/docs/grpc/about-grpc](https://cloud.google.com/endpoints/docs/grpc/about-grpc)

# ESP v2 on K8s
[https://github.com/GoogleCloudPlatform/esp-v2](https://github.com/GoogleCloudPlatform/esp-v2)
[Doc](https://github.com/GoogleCloudPlatform/esp-v2/blob/master/doc/esp-v2-on-k8s.md)

# Run ESP (Extensible Service Proxy) on Kubernetes
[https://github.com/GoogleCloudPlatform/endpoints-samples/tree/master/k8s](https://github.com/GoogleCloudPlatform/endpoints-samples/tree/master/k8s)

gcloud container clusters get-credentials NAME --zone ZONE

gcloud endpoints services deploy api_descriptor.pb api_config.yaml

# Set your project ID as a variable to make commands easier:
GCLOUD_PROJECT=<Your Project ID>

gcloud container builds submit --tag gcr.io/${GCLOUD_PROJECT}/python-grpc-hello:1.0 .


https://cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#grpc-transcoding
