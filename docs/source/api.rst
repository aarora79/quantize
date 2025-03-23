API Reference
============

This page provides detailed documentation for the Quantize API.

quantize Module
--------------

.. automodule:: quantize
   :members:
   :undoc-members:
   :show-inheritance:

quantize.quantize Module
-----------------------

.. automodule:: quantize.quantize
   :members:
   :undoc-members:
   :show-inheritance:

Core Functions
-------------

quantize_to_int4
~~~~~~~~~~~~~~~

.. autofunction:: quantize.quantize_to_int4

The ``quantize_to_int4`` function converts floating point values to int4 values (4-bit integers). Int4 values range from -8 to 7, providing 16 distinct values.

Parameters:
    - **values** (*Union[List[float], np.ndarray]*): List or array of floating point values to quantize
    - **scale_method** (*str, optional*): Method to determine scaling factor. Default is "minmax". Options are:
        - "minmax": Maps the min and max values to the int4 range
        - "absmax": Maps the absolute max value to the int4 range

Returns:
    - **Tuple[np.ndarray, float, float]**: A tuple containing:
        - **quantized_values**: numpy array of int4 values (stored as int8)
        - **scale**: scaling factor used for quantization
        - **zero_point**: zero point offset (usually 0 for symmetric quantization)

dequantize_from_int4
~~~~~~~~~~~~~~~~~~~

.. autofunction:: quantize.dequantize_from_int4

The ``dequantize_from_int4`` function converts int4 values back to floating point.

Parameters:
    - **quantized_values** (*np.ndarray*): Array of quantized int4 values (stored as int8)
    - **scale** (*float*): Scaling factor used during quantization
    - **zero_point** (*float, optional*): Zero point offset. Default is 0.

Returns:
    - **np.ndarray**: Array of dequantized floating point values

Memory Optimization Functions
---------------------------

pack_int4_to_int8
~~~~~~~~~~~~~~~~

.. autofunction:: quantize.quantize.pack_int4_to_int8

The ``pack_int4_to_int8`` function packs two int4 values into each int8 value to save memory.

Parameters:
    - **int4_values** (*np.ndarray*): Array of int4 values (stored as int8)

Returns:
    - **np.ndarray**: Array of packed int8 values (half the length of input)

unpack_int8_to_int4
~~~~~~~~~~~~~~~~~~

.. autofunction:: quantize.quantize.unpack_int8_to_int4

The ``unpack_int8_to_int4`` function unpacks int8 values back into int4 values.

Parameters:
    - **packed_values** (*np.ndarray*): Array of packed int8 values

Returns:
    - **np.ndarray**: Array of unpacked int4 values (twice the length of input)

Example Function
--------------

example
~~~~~~

.. autofunction:: quantize.quantize.example

The ``example`` function demonstrates the quantization process with sample values.

Returns:
    - **Tuple[np.ndarray, np.ndarray, np.ndarray]**: A tuple containing:
        - Original floating point values
        - Quantized int4 values
        - Dequantized floating point values