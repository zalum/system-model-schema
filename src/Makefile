generate_stubs:
		python3 -m stubs.generate

clean:
		rm -rf build
		rm -rf dist
		rm -rf system_model_schema.egg-info

include-schema:
		cp ../schema/*.yaml  sms

test: include-schema
		nose2

build: clean test
		python3 setup.py bdist_wheel egg_info -d -v

get-artifact-name:
		@ls dist/*.whl

