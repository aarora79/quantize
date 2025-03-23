Usage
=====

Basic Usage
----------

The Quantize package provides functions for quantizing floating point values to int4 values and back.

Quantizing Values
~~~~~~~~~~~~~~~~

To quantize floating point values to int4 values:

.. code-block:: python

   from quantize import quantize_to_int4
   
   # Example floating point values
   float_values = [0.1, 0.5, -1.3, 2.7, 3.9, -0.8]
   
   # Quantize to int4
   quantized_values, scale, zero_point = quantize_to_int4(float_values)
   
   print("Quantized values:", quantized_values)
   print("Scale factor:", scale)
   print("Zero point:", zero_point)

The ``quantize_to_int4`` function returns a tuple containing:

1. The quantized values as a numpy array of int8 values (containing int4 values in the range -8 to 7)
2. The scale factor used for quantization
3. The zero point offset (usually 0 for symmetric quantization)

Dequantizing Values
~~~~~~~~~~~~~~~~~~

To convert quantized int4 values back to floating point:

.. code-block:: python

   from quantize import dequantize_from_int4
   
   # Dequantize back to floating point
   dequantized_values = dequantize_from_int4(quantized_values, scale, zero_point)
   
   print("Dequantized values:", dequantized_values)

The ``dequantize_from_int4`` function takes the quantized values, scale factor, and zero point, and returns the dequantized floating point values.

Scaling Methods
--------------

The ``quantize_to_int4`` function supports two scaling methods:

MinMax Scaling
~~~~~~~~~~~~~

The default method is "minmax", which maps the minimum and maximum values of the input to the int4 range:

.. code-block:: python

   quantized_values, scale, zero_point = quantize_to_int4(float_values, scale_method="minmax")

This method ensures that the full range of the input values is represented in the quantized values.

AbsMax Scaling
~~~~~~~~~~~~~

The "absmax" method maps the maximum absolute value of the input to the int4 range:

.. code-block:: python

   quantized_values, scale, zero_point = quantize_to_int4(float_values, scale_method="absmax")

This method is useful when the input values are centered around zero and the positive and negative ranges are equally important.

Memory Optimization
-----------------

Packing Int4 Values
~~~~~~~~~~~~~~~~~~

To save memory, you can pack two int4 values into each int8 value:

.. code-block:: python

   from quantize.quantize import pack_int4_to_int8
   
   # Pack int4 values into int8 for storage efficiency
   packed_values = pack_int4_to_int8(quantized_values)
   
   print("Packed values (int8):", packed_values)
   print("Memory usage reduced by 50%")

Unpacking Int8 Values
~~~~~~~~~~~~~~~~~~~

To unpack int8 values back to int4 values:

.. code-block:: python

   from quantize.quantize import unpack_int8_to_int4
   
   # Unpack back to int4
   unpacked_values = unpack_int8_to_int4(packed_values)
   
   print("Unpacked values (int4):", unpacked_values)

Complete Example
--------------

Here's a complete example demonstrating the quantization process:

.. code-block:: python

   import numpy as np
   from quantize import quantize_to_int4, dequantize_from_int4
   from quantize.quantize import pack_int4_to_int8, unpack_int8_to_int4
   
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

Analyzing Quantization Error
--------------------------

When using quantization, it's important to understand the error introduced by the reduced precision:

.. code-block:: python

   # Calculate and display quantization error
   error = float_values - dequantized
   print("Error per value:", error)
   print("Mean absolute error:", np.mean(np.abs(error)))
   print("Max absolute error:", np.max(np.abs(error)))

The error will depend on the range and distribution of the original values, as well as the scaling method used.