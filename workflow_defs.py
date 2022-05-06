#############################################
# © Copyright 2021-2022 Zapata Computing Inc.
#############################################

import orquestra.sdk.v2 as sdk

THIS_IMPORT = sdk.GitImport(
    repo_url="git@github.com:zapatacomputing/tutorial-0-welcome.git",
    git_ref="main",
)

@sdk.task(source_import=THIS_IMPORT)
def hello():
    return "Hello Orquestra!"

@sdk.workflow
def hello_workflow():
    return [hello()]
