from .service import Service

import pytest


@pytest.fixture
def service():
    service = Service()
    yield service
    service._scape_action_center()


def test_open_action_center(service):
    service._open_action_center()
    assert service.action_center_is_open


def test_locate_hotspot_button_fail(service):
    location = service.locate_hotspot_button()
    assert location is None
    assert service.hotspot_button_location is None


def test_locate_hotspot_button_success(service):
    service._open_action_center()
    location = service.locate_hotspot_button()
    assert location is not None
    assert service.hotspot_button_location is not None


def test_click_hotspot_button(service):
    service._open_action_center()
    service.locate_hotspot_button()
    service.click_hotspot_button()
    assert service.hotspot_turned_on
