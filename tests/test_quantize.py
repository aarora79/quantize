"""
Tests for the quantize package.
"""

import numpy as np
import pytest
from quantize import quantize_to_int4, dequantize_from_int4
from quantize.quantize import pack_int4_to_int8, unpack_int8_to_int4


def test_quantize_to_int4_minmax():
    """Test quantization using minmax scaling."""
    # Test with a range of values
    values = np.array([-10.0, -5.0, 0.0, 5.0, 10.0])
    quantized, scale, zero_point = quantize_to_int4(values, scale_method="minmax")
    
    # Check that quantized values are within int4 range
    assert np.all(quantized >= -8)
    assert np.all(quantized <= 7)
    
    # Check scale calculation
    expected_scale = 20.0 / 15  # (max - min) / 15
    assert np.isclose(scale, expected_scale)
    
    # Check zero point
    assert zero_point == 0
    
    # Check that extreme values map to extreme int4 values
    assert quantized[0] == -8  # min value should map to -8
    assert quantized[-1] == 7  # max value should map to 7


def test_quantize_to_int4_absmax():
    """Test quantization using absmax scaling."""
    # Test with a range of values
    values = np.array([-7.0, -3.5, 0.0, 3.5, 7.0])
    quantized, scale, zero_point = quantize_to_int4(values, scale_method="absmax")
    
    # Check that quantized values are within int4 range
    assert np.all(quantized >= -8)
    assert np.all(quantized <= 7)
    
    # Check scale calculation
    expected_scale = 7.0 / 7  # absmax / 7
    assert np.isclose(scale, expected_scale)
    
    # Check that extreme values map correctly
    assert quantized[0] == -7  # -7.0 should map to -7
    assert quantized[-1] == 7  # 7.0 should map to 7


def test_dequantize_from_int4():
    """Test dequantization."""
    # Create quantized values
    quantized = np.array([-8, -4, 0, 4, 7], dtype=np.int8)
    scale = 1.5
    
    # Dequantize
    dequantized = dequantize_from_int4(quantized, scale)
    
    # Check dequantized values
    expected = np.array([-12.0, -6.0, 0.0, 6.0, 10.5])
    assert np.allclose(dequantized, expected)


def test_pack_unpack_int4():
    """Test packing and unpacking int4 values."""
    # Create some int4 values
    int4_values = np.array([-8, -4, 0, 4, 7, -2, 3, 1], dtype=np.int8)
    
    # Pack to int8
    packed = pack_int4_to_int8(int4_values)
    
    # Check packed length
    assert len(packed) == len(int4_values) // 2
    
    # Unpack back to int4
    unpacked = unpack_int8_to_int4(packed)
    
    # Check that unpacked values match original (up to the original length)
    assert np.array_equal(unpacked[:len(int4_values)], int4_values)


def test_quantize_dequantize_roundtrip():
    """Test the full quantization and dequantization process."""
    # Original values
    original = np.array([-10.5, -5.2, 0.0, 5.2, 10.5])
    
    # Quantize
    quantized, scale, zero_point = quantize_to_int4(original)
    
    # Dequantize
    dequantized = dequantize_from_int4(quantized, scale)
    
    # Check that dequantized values are close to original
    # Note: We expect some loss due to quantization
    assert np.allclose(original, dequantized, rtol=0, atol=scale)  # Error should be at most one quantum


def test_zero_range():
    """Test quantization with a zero range."""
    # All zeros
    values = np.zeros(5)
    quantized, scale, zero_point = quantize_to_int4(values)
    
    # Check that all quantized values are 0
    assert np.all(quantized == 0)
    
    # Check that scale is 1.0 (to avoid division by zero)
    assert scale == 1.0


def test_single_value():
    """Test quantization with a single value."""
    # Single value
    values = np.array([42.0])
    quantized, scale, zero_point = quantize_to_int4(values)
    
    # Check that the quantized value is 0 (since there's no range)
    assert quantized[0] == 0
    
    # Check that scale is 1.0 (to avoid division by zero)
    assert scale == 1.0