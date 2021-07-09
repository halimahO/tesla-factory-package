import pytest
from tesla import factory

def test_color():
  teslaY = factory.Tesla("Y", "White")
  assert teslaY.color == "White", "Count is wrong"

def test_color():
  teslaY = factory.Tesla("Y", "White")
  assert teslaY.color == "White", "Count is wrong"

def test_modelX():
    modelx = factory.ModelX("black")
    modelx.unlock()
    assert modelx.open_doors() == "Doors opens towards roof"