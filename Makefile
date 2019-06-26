SETTINGS := postgres
ALGONAUT_SETTINGS_D := algonaut/settings:algonaut/tests/settings/$(SETTINGS)
PYTHONPATH := $(PYTHONPATH):contact

test: test-contact

test-contact:
	PYTHONPATH=$(PYTHONPATH) ALGONAUT_SETTINGS_D=$(ALGONAUT_SETTINGS_D):contact/settings:contact/tests/settings pytest $(testargs) contact/tests

