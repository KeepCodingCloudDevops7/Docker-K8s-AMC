kubectl apply -f namespace -f app -f configmaps -f db -f service


namespace/kp-practica created
deployment.apps/app-deploy created
service/db unchanged
configmap/db-config created
secret/user-config created
statefulset.apps/app-statefulset created
service/app-service created
service/db-service created
Error from server (InternalError): error when creating "service/app-ingress.yaml": Internal error occurred: failed calling webhook "validate.nginx.ingress.kubernetes.io": failed to call webhook: Post "https://ingress-nginx-controller-admission.ingress-nginx.svc:443/networking/v1/ingresses?timeout=10s": service "ingress-nginx-controller-admission" not found


##Cambiar namespace y ver en cual estoy


kubectl config set-context --current --namespace=kp-practica

kubectl config view --minify --output 'jsonpath={..namespace}'
