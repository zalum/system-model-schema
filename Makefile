version := $(shell cat version.txt)
pwd := $(shell pwd)
artifact_name := system-model-schema
artifact_file := target/$(artifact_name)-$(version).zip

build-spec:
	mkdir -p target
	zip -r -j $(artifact_file) ./schema/*

get-artifact-name:
	@ls $(pwd)/$(artifact_file)
