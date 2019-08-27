version := $(shell cat version.txt)
artifact_name := system-model-schema

build-spec:
	mkdir -p target
	zip -r -j target/$(artifact_name)-$(version).zip ./schema/*