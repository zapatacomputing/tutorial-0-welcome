#############################################
# © Copyright 2021-2022 Zapata Computing Inc.
#############################################
import os
import orquestra.sdk.v2 as sdk

THIS_IMPORT = sdk.GitImport(
    repo_url="git@github.com:zapatacomputing/tutorial-0-welcome.git",
    git_ref="master",
)

dependency_imports = [
    sdk.GitImport(
        repo_url="git@github.com:zapatacomputing/orquestra-workflow.git",
        git_ref="v0.19.0",
    ),
    sdk.GitImport(
        repo_url="git@github.com:zapatacomputing/orquestra-sdk.git",
        git_ref="v0.28.0",
    ),
]
@sdk.task(source_import=THIS_IMPORT, dependency_imports=dependency_imports)
def hello(message):
    return f"Hello {message}!"

@sdk.workflow
def hello_workflow():
    message = os.environ["MESSAGE"]
    print(f"Message: {message}")
    return [hello(message)]