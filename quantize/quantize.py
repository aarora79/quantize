"""
Implementation of quantization functions for converting between floating point and int4 values.
"""

import numpy as np
from typing import List, Union, Tuple


def quantize_to_int4(
    values: Union[List[float], np.ndarray], 
    scale_method: str = "minmax"
) -> Tuple[np.ndarray, float, float]:
    """
    Quantize floating point values to int4 values (4-bit integers).
    
    Int4 values range from -8 to 7 (16 distinct values).
    
    Args:
        values: List or array of floating point values to quantize
        scale_method: Method to determine scaling factor ('minmax' or 'absmax')
        
    Returns:
        Tuple of (quantized_values, scale, zero_point)
        - quantized_values: numpy array of int4 values (stored as int8)
        - scale: scaling factor used for quantization
        - zero_point: zero point offset (usually 0 for symmetric quantization)
    """
    values = np.asarray(values, dtype=np.float32)
    
    # Determine scaling parameters based on the method
    if scale_method == "minmax":
        # Map the min and max values to the int4 range
        data_min = values.min()
        data_max = values.max()
        
        # Calculate scale and zero_point
        scale = (data_max - data_min) / 15  # 15 = 2^4 - 1
        zero_point = 0  # For simplicity, we use symmetric quantization
        
    elif scale_method == "absmax":
        # Map the absolute max value to the int4 range
        abs_max = np.max(np.abs(values))
        
        # Calculate scale (zero_point is 0 for symmetric quantization)
        scale = abs_max / 7  # 7 is the max positive value for int4
        zero_point = 0
        
    else:
        raise ValueError(f"Unknown scale_method: {scale_method}")
    
    # Avoid division by zero
    if scale == 0:
        scale = 1.0
    
    # Quantize the values
    quantized = np.round(values / scale).astype(np.int8)
    
    # Clip to int4 range [-8, 7]
    quantized = np.clip(quantized, -8, 7)
    
    return quantized, scale, zero_point


def dequantize_from_int4(
    quantized_values: np.ndarray, 
    scale: float, 
    zero_point: float = 0
) -> np.ndarray:
    """
    Dequantize int4 values back to floating point.
    
    Args:
        quantized_values: Array of quantized int4 values (stored as int8)
        scale: Scaling factor used during quantization
        zero_point: Zero point offset (usually 0 for symmetric quantization)
        
    Returns:
        Array of dequantized floating point values
    """
    # Convert to float and apply scaling
    return (quantized_values.astype(np.float32)) * scale


def pack_int4_to_int8(int4_values: np.ndarray) -> np.ndarray:
    """
    Pack two int4 values into each int8 value to save memory.
    
    Args:
        int4_values: Array of int4 values (stored as int8)
        
    Returns:
        Array of packed int8 values (half the length of input)
    """
    # Ensure we have an even number of elements by padding if necessary
    if len(int4_values) % 2 != 0:
        int4_values = np.pad(int4_values, (0, 1), 'constant')
    
    # Reshape to pairs of values
    pairs = int4_values.reshape(-1, 2)
    
    # Pack two int4 values into each int8
    # First value goes in the lower 4 bits, second in the upper 4 bits
    packed = (pairs[:, 0] & 0xF) | ((pairs[:, 1] & 0xF) << 4)
    
    return packed.astype(np.int8)


def unpack_int8_to_int4(packed_values: np.ndarray) -> np.ndarray:
    """
    Unpack int8 values back into int4 values.
    
    Args:
        packed_values: Array of packed int8 values
        
    Returns:
        Array of unpacked int4 values (twice the length of input)
    """
    # Extract lower 4 bits for first value
    lower = packed_values & 0xF
    
    # Extract upper 4 bits for second value and shift down
    upper = (packed_values >> 4) & 0xF
    
    # Convert to signed int4 (-8 to 7)
    # For values 8-15, subtract 16 to get the negative representation
    lower = np.where(lower > 7, lower - 16, lower)
    upper = np.where(upper > 7, upper - 16, upper)
    
    # Interleave the values
    unpacked = np.empty(len(packed_values) * 2, dtype=np.int8)
    unpacked[0::2] = lower
    unpacked[1::2] = upper
    
    return unpacked


# Example usage function
def example():
    """
    Example demonstrating the quantization process.
    """
    # Example floating point values
    float_values = np.array([0.1, 0.5, -1.3, 2.7, 3.9, -0.8, 5.2, -4.7])
    print("Original values:", float_values)
    
    # Quantize to int4
    quantized, scale, zero_point = quantize_to_int4(float_values)
    print("Quantized values (int4):", quantized)
    print("Scale factor:", scale)
    
    # Pack int4 values into int8 for storage efficiency
    packed = pack_int4_to_int8(quantized)
    print("Packed values (int8):", packed)
    print("Memory usage reduced by 50%")
    
    # Unpack back to int4
    unpacked = unpack_int8_to_int4(packed)
    print("Unpacked values (int4):", unpacked[:len(float_values)])  # Trim any padding
    
    # Dequantize back to floating point
    dequantized = dequantize_from_int4(quantized, scale)
    print("Dequantized values:", dequantized)
    
    # Calculate error
    error = float_values - dequantized
    print("Quantization error:", error)
    print("Mean absolute error:", np.mean(np.abs(error)))
    
    return float_values, quantized, dequantized


if __name__ == "__main__":
    example()