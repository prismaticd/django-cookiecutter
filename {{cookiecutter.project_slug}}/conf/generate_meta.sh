#!/usr/bin/env bash

mkdir -p .meta
rm .meta/*
date --utc +%s > .meta/ts
date --utc > .meta/date
echo ${CI_COMMIT_SHA} > .meta/commit
echo ${CI_COMMIT_REF_NAME} > .meta/ref;
echo ${CI_PIPELINE_ID} > .meta/pipelineid;
echo ${CI_PIPELINE_IID} > .meta/pipelineiid;
cat .meta/* > .meta/info

