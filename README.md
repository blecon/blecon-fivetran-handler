# Fivetran Handler for Blecon. 

This Blecon Handler reformats device requests into a stream of events suitable for ingestion into Fivetran.

To deploy this to your AWS account, run 

    sam build
    sam deploy --guided 

To set up SAM, follow [this guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) including the prerequisites.