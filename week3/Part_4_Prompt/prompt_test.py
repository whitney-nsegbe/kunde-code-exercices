from config import AWS_KEY_ID, AWS_KEY, AWS_REGION
from botocore.config import Config
import boto3



def get_answer(prompt, system_prompt="You are a helpful AI assistant.", output_folder=None):
    if not system_prompt:
        system_prompt = "You are a helpful AI assistant."

    bedrock = boto3.client(
        "bedrock-runtime",
        region_name=AWS_REGION,
        config=Config(read_timeout=120),
    )

    # Calling the model
    response = bedrock.converse(
        modelId="us.amazon.nova-2-lite-v1:0",
        messages=[
            {
                "role": "user",
                #^this is where we send your prompt to AWS
                "content": [{"text": prompt}],
            }
        ],
        system=[{"text": system_prompt}], 
    )

    # Extract the text response
    
    content_list = response["output"]["message"]["content"]
    for content in content_list:
        if "text" in content:
            print(content["text"])

    # Save output to the group's folder
    answer = content["text"]
    if output_folder:
        output_path = Path(output_folder) / "ai_output.md"
        output_path.write_text(answer, encoding="utf-8")
        print(f"\nSaved output to: {output_path}")

    return answer