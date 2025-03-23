Introduction
============

Overview
--------

Quantize is a simple Python library for quantizing floating point values to int4 values (4-bit integers). 
Quantization is a technique used to reduce the precision of numbers, which can be useful for:

- Reducing memory usage
- Improving computational efficiency
- Enabling deployment on hardware with limited precision

Int4 quantization specifically reduces floating point values to 4-bit integers, which can only represent 16 distinct values.

What is Quantization?
--------------------

Quantization is the process of mapping a large set of input values to a smaller set of output values. 
In the context of machine learning and numerical computing, it typically refers to reducing the precision 
of numbers (e.g., from 32-bit floating point to lower bit-width integers).

Benefits of Int4 Quantization
----------------------------

Memory Efficiency
~~~~~~~~~~~~~~~~

Int4 values require only 4 bits per value, compared to 32 bits for a standard float32. This represents 
an 8x reduction in memory usage. The library also provides functions to pack two int4 values into a 
single int8 value for even more efficient storage.

Computational Efficiency
~~~~~~~~~~~~~~~~~~~~~~~

Operations on lower-precision integers are often faster than operations on floating point values, 
especially on specialized hardware. Many modern processors and accelerators have optimized instructions 
for low-precision integer arithmetic.

Hardware Compatibility
~~~~~~~~~~~~~~~~~~~~~

Some specialized AI accelerators and edge devices are optimized for low-precision integer arithmetic. 
Int4 quantization enables deployment on these devices.

Limitations
----------

Precision Loss
~~~~~~~~~~~~~

The primary limitation of quantization is the loss of precision. Int4 values can only represent 16 distinct 
values (typically from -8 to 7), which means that fine-grained differences in the original floating point 
values may be lost.

Range Limitations
~~~~~~~~~~~~~~~~

Int4 values have a limited range. The library provides different scaling methods to map the original 
floating point range to the int4 range, but very large or very small values may not be represented accurately.

Use Cases
--------

Int4 quantization is particularly useful in:

- Machine learning model deployment, especially for inference
- Edge computing with limited resources
- Applications where memory efficiency is critical
- Scenarios where approximate values are acceptable