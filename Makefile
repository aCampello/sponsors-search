.PHONY: docker-build
docker-build:
	docker build -t s-search:latest .

.PHONY: docker-push
docker-push: docker-build
	aws --profile personal ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin $(ECR)
	docker tag s-search:latest $(ECR)/s-search:latest
	docker push $(ECR)/s-search:latest
