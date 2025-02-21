#!/bin/bash

# Variables
GENERATOR_JAR="openapi-generator-cli.jar"
INPUT_FILE="open_api.yml"
OUTPUT_FOLDER="./tmp/generated"
FINAL_FOLDER="./code/generated_api"
PACKAGE_NAME="generated_api"
MAIN_FILE="$OUTPUT_FOLDER/generated_api/main.py"
INIT_FILE="$OUTPUT_FOLDER/generated_api/__init__.py"

# Step 1: Generate the API files in the temporary folder
java -jar $GENERATOR_JAR generate \
    -g python-fastapi \
    -i $INPUT_FILE \
    -o $OUTPUT_FOLDER \
    --package-name $PACKAGE_NAME \
    --additional-properties sourceFolder="/"

# Check if the generation succeeded
if [ $? -ne 0 ]; then
    echo "Failed to generate API files."
    exit 1
fi

# Step 2: Remove the existing content in the final folder if it exists
rm -rf $FINAL_FOLDER/*

# Step 3: Remove the main.py file from the generated content
if [ -f "$MAIN_FILE" ]; then
    rm "$MAIN_FILE"
fi

# Step 4: Move the generated content to the final destination
# Ensure the final folder exists
mkdir -p $FINAL_FOLDER

# Copy the generated_api folder content to the final destination
cp -r $OUTPUT_FOLDER/generated_api/* $FINAL_FOLDER/

# Step 5: Replace 'import openapi_server.impl' with nothing in all Python files in FINAL_FOLDER
find $FINAL_FOLDER -type f -name "*.py" -exec sed -i 's/openapi_server/recommender/g' {} \;

# Step 6: Create __init__.py in the final folder
touch $INIT_FILE

# Step 7: Clean up the temporary folder
rm -rf $OUTPUT_FOLDER

echo "API files successfully generated, main.py removed, __init__.py added, imports cleaned, and moved to $FINAL_FOLDER."
