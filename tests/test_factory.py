import pytest
from tesla import fabric

def test_color():
  teslaY = fabric.Tesla("Y", "White")
  assert teslaY.color == "White", "Count is wrong"

def test_color():
  teslaY = fabric.Tesla("Y", "White")
  assert teslaY.color == "White", "Count is wrong"

def test_modelX():
    modelx = fabric.ModelX("black")
    modelx.unlock()
    assert modelx.open_doors() == "Doors opens towards roof"