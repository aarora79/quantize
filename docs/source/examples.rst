Examples
========

Basic Example
------------

This example demonstrates the basic usage of the Quantize package:

.. code-block:: python

   import numpy as np
   from quantize import quantize_to_int4, dequantize_from_int4
   
   # Create some example floating point values
   float_values = np.array([0.1, 0.5, -1.3, 2.7, 3.9, -0.8, 5.2, -4.7])
   print("Original floating point values:")
   print(float_values)
   
   # Quantize to int4
   print("Quantizing to int4...")
   quantized, scale, zero_point = quantize_to_int4(float_values)
   print("Quantized values (int4):", quantized)
   print("Scale factor:", scale)
   print("Zero point:", zero_point)
   
   # Dequantize back to floating point
   print("Dequantizing back to floating point...")
   dequantized = dequantize_from_int4(quantized, scale)
   print("Dequantized values:", dequantized)
   
   # Calculate and display quantization error
   error = float_values - dequantized
   print("Quantization error analysis:")
   print("Error per value:", error)
   print("Mean absolute error:", np.mean(np.abs(error)))
   print("Max absolute error:", np.max(np.abs(error)))

Memory Optimization Example
-------------------------

This example demonstrates how to use the memory optimization functions:

.. code-block:: python

   import numpy as np
   from quantize import quantize_to_int4
   from quantize.quantize import pack_int4_to_int8, unpack_int8_to_int4
   
   # Create some example floating point values
   float_values = np.array([0.1, 0.5, -1.3, 2.7, 3.9, -0.8, 5.2, -4.7])
   
   # Quantize to int4
   quantized, scale, _ = quantize_to_int4(float_values)
   print("Quantized values (int4):", quantized)
   
   # Pack int4 values into int8 for storage efficiency
   packed = pack_int4_to_int8(quantized)
   print("Packed values (int8):", packed)
   print("Original size:", len(quantized), "bytes")
   print("Packed size:", len(packed), "bytes")
   print("Memory reduction:", (1 - len(packed) / len(quantized)) * 100, "%")
   
   # Unpack back to int4
   unpacked = unpack_int8_to_int4(packed)
   print("Unpacked values (int4):", unpacked[:len(quantized)])  # Trim any padding
   
   # Verify that unpacked values match original quantized values
   print("Unpacked values match original:", np.array_equal(unpacked[:len(quantized)], quantized))

Comparing Scaling Methods
-----------------------

This example compares the "minmax" and "absmax" scaling methods:

.. code-block:: python

   import numpy as np
   from quantize import quantize_to_int4, dequantize_from_int4
   
   # Create some example floating point values
   float_values = np.array([-10.0, -5.0, 0.0, 5.0, 10.0])
   print("Original values:", float_values)
   
   # Quantize using minmax scaling
   quantized_minmax, scale_minmax, _ = quantize_to_int4(float_values, scale_method="minmax")
   print("\nMinMax Scaling:")
   print("Quantized values:", quantized_minmax)
   print("Scale factor:", scale_minmax)
   
   # Dequantize minmax values
   dequantized_minmax = dequantize_from_int4(quantized_minmax, scale_minmax)
   print("Dequantized values:", dequantized_minmax)
   print("Mean absolute error:", np.mean(np.abs(float_values - dequantized_minmax)))
   
   # Quantize using absmax scaling
   quantized_absmax, scale_absmax, _ = quantize_to_int4(float_values, scale_method="absmax")
   print("\nAbsMax Scaling:")
   print("Quantized values:", quantized_absmax)
   print("Scale factor:", scale_absmax)
   
   # Dequantize absmax values
   dequantized_absmax = dequantize_from_int4(quantized_absmax, scale_absmax)
   print("Dequantized values:", dequantized_absmax)
   print("Mean absolute error:", np.mean(np.abs(float_values - dequantized_absmax)))
   
   # Compare results
   print("\nComparison:")
   print("MinMax error:", np.mean(np.abs(float_values - dequantized_minmax)))
   print("AbsMax error:", np.mean(np.abs(float_values - dequantized_absmax)))

Handling Edge Cases
-----------------

This example demonstrates how the library handles edge cases:

.. code-block:: python

   import numpy as np
   from quantize import quantize_to_int4, dequantize_from_int4
   
   # Test with all zeros
   zeros = np.zeros(5)
   print("Original zeros:", zeros)
   quantized_zeros, scale_zeros, _ = quantize_to_int4(zeros)
   print("Quantized zeros:", quantized_zeros)
   print("Scale factor:", scale_zeros)
   dequantized_zeros = dequantize_from_int4(quantized_zeros, scale_zeros)
   print("Dequantized zeros:", dequantized_zeros)
   
   # Test with a single value
   single_value = np.array([42.0])
   print("\nOriginal single value:", single_value)
   quantized_single, scale_single, _ = quantize_to_int4(single_value)
   print("Quantized single value:", quantized_single)
   print("Scale factor:", scale_single)
   dequantized_single = dequantize_from_int4(quantized_single, scale_single)
   print("Dequantized single value:", dequantized_single)
   
   # Test with extreme values
   extreme_values = np.array([-1e6, 1e6])
   print("\nOriginal extreme values:", extreme_values)
   quantized_extreme, scale_extreme, _ = quantize_to_int4(extreme_values)
   print("Quantized extreme values:", quantized_extreme)
   print("Scale factor:", scale_extreme)
   dequantized_extreme = dequantize_from_int4(quantized_extreme, scale_extreme)
   print("Dequantized extreme values:", dequantized_extreme)
   print("Relative error:", np.abs((extreme_values - dequantized_extreme) / extreme_values))