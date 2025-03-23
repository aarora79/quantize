#!/usr/bin/env python3
"""
Example script demonstrating how to use the quantize package.
"""

import numpy as np
from quantize import quantize_to_int4, dequantize_from_int4


def main():
    # Create some example floating point values
    float_values = np.array([0.1, 0.5, -1.3, 2.7, 3.9, -0.8, 5.2, -4.7])
    print("\nOriginal floating point values:")
    print(float_values)
    
    # Quantize to int4
    print("\nQuantizing to int4...")
    quantized, scale, zero_point = quantize_to_int4(float_values)
    print("Quantized values (int4):", quantized)
    print("Scale factor:", scale)
    print("Zero point:", zero_point)
    
    # Dequantize back to floating point
    print("\nDequantizing back to floating point...")
    dequantized = dequantize_from_int4(quantized, scale)
    print("Dequantized values:", dequantized)
    
    # Calculate and display quantization error
    error = float_values - dequantized
    print("\nQuantization error analysis:")
    print("Error per value:", error)
    print("Mean absolute error:", np.mean(np.abs(error)))
    print("Max absolute error:", np.max(np.abs(error)))
    
    # Display value ranges
    print("\nValue ranges:")
    print(f"Original range: [{float_values.min()}, {float_values.max()}]")
    print(f"Quantized range: [{quantized.min()}, {quantized.max()}] (int4 range is [-8, 7])")
    print(f"Dequantized range: [{dequantized.min()}, {dequantized.max()}]")
    
    print("\nThis demonstrates basic int4 quantization, which reduces precision")
    print("but allows for significant memory savings (up to 8x compared to float32).")


if __name__ == "__main__":
    main()