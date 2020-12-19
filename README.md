# Smart-Photo-Album-with-NLP
# Voice Controlled Photo Album Search
![alt text](https://github.com/Zeus197/Smart-Photo-Album-with-NLP/blob/main/images/ApplicationUI.png)
# Frontend
Created a frontend in AWS S3 using HTML, CSS and Javascript to provide a web-app user-interface to interact with the chatbot.
Various open source libraries and frameworks were used for designing the UI/UX of the bot.
# Description
"Voice Based Photo Album Search" is a serverless, microservice driven web-based application, that can be searched using natural language through both text and voice. We can upload photos and search then similar to a image search engine. It is designed using multiple AWS components :-

AWS Transcribe, API-Gateway, Swagger, S3-Buckets, Lambda Functions, VPC, ElasticSearch, AWS Lex, AWS Rekognition, Cloud watch.

The Search query from the user is sent to AWS Lex which identifies the keywords from the query and searched the Elastic Search for the indices. If there is a match then it will return all the images that matched the search query. The search query can be text that the user enters or it can be a voice note where we would use AWS Transcribe to convert speech to text and then use the text for the search query.

The Upload workflow takes an image from the user local system and uplads it directly to S3 and then uses AWS rekognition to index the image which is later stored in Elastic search.
# Architecture
![alt text](https://github.com/Zeus197/Smart-Photo-Album-with-NLP/blob/main/images/ArchitectureDiagram.png)
# Sample Output
The user starts the mic and serches for a specific photo
![alt text](https://github.com/Zeus197/Smart-Photo-Album-with-NLP/blob/main/images/SeachOutput.png)
# References
[1. https://medium.com/@dhruvarora2/uploading-images-to-s3-via-api-gateway-put-request-435a774bcdb8](https://medium.com/@dhruvarora2/uploading-images-to-s3-via-api-gateway-put-request-435a774bcdb8)

[2. https://medium.com/@dhruvarora2/setup-an-ec2-instance-as-a-nat-gateway-217d9bce82a0](https://medium.com/@dhruvarora2/setup-an-ec2-instance-as-a-nat-gateway-217d9bce82a0)

[3. https://medium.com/@dhruvarora2/access-aws-services-like-rekognition-from-a-vpc-enabled-lambda-b1d6907bae93](https://medium.com/@dhruvarora2/access-aws-services-like-rekognition-from-a-vpc-enabled-lambda-b1d6907bae93)

[4. https://medium.com/@dhruvarora2/access-aws-services-like-rekognition-from-a-vpc-enabled-lambda-b1d6907bae93](https://medium.com/@dhruvarora2/access-aws-services-like-rekognition-from-a-vpc-enabled-lambda-b1d6907bae93)
