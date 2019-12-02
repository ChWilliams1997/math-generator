import unittest
from backend.base_conversion import BaseConversion

class TestNumberConversion(unittest.TestCase):
  def setUp(self):
    self.converter = BaseConversion()

  def test_hex_to_bin(self):
    hex_num = 'A'
    actual = self.converter.hexToBinary(hex_num)
    expected = '1010'
    assert actual == expected

  def test_bin_to_hex(self):
    bin_num = '1010'
    actual = self.converter.binaryToHex(bin_num)
    expected = 'A'
    assert actual == expected

  def test_hex_to_oct(self):
    hex_num = 'A'
    actual = self.converter.hexToOctal(hex_num)
    expected = '12'
    assert actual == expected

  def test_oct_to_hex(self):
    oct_num = '12'
    actual = self.converter.octalToHex(oct_num)
    expected = 'A'
    assert actual == expected
  
  def test_bin_to_oct(self):
    bin_num = '1010'
    actual = self.converter.binaryToOctal(bin_num)
    expected = '12'
    assert actual == expected

  def test_oct_to_bin(self):
    oct_num = '12'
    actual = self.converter.octalToBinary(oct_num)
    expected = '1010'
    assert actual == expected

  def test_bin_to_dec(self):
    bin_num = '1010'
    actual = self.converter.binaryToDecimal(bin_num)
    expected = '10'
    assert actual == expected

  def test_dec_to_bin(self):
    dec_num = '10'
    actual = self.converter.decimalToBinary(dec_num)
    expected = bin(int(dec_num))
    assert actual == expected

  def test_hex_to_dec(self):
    hex_num = 'A'
    actual = self.converter.hexToDecimal(hex_num)
    expected = '10'
    assert actual == expected

  def test_dec_to_hex(self):
    dec_num = '10'
    actual = self.converter.decimalToHex(dec_num)
    expected = hex(int(dec_num))
    assert actual == expected

  def test_oct_to_dec(self):
    oct_num = '12'
    actual = self.converter.octalToDecimal(oct_num)
    expected = '10'
    assert actual == expected

  def test_dec_to_oct(self):
    dec_num = '10'
    actual = self.converter.decimalToOctal(dec_num)
    expected = oct(int(dec_num))
    assert actual == expected

  def test_base_three_to_decimal(self):
    base3_num = '12'
    actual = self.converter.anyToDecimal(base3_num, 3)
    expected = '5'
    assert actual == expected

  def test_dec_to_base_three(self):
    dec_num = '5'
    actual = self.converter.decimalToAny(dec_num, 3)
    expected = '12'
    assert actual == expected