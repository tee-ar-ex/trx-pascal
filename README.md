# trx-python

TRX (tee-ar-ex) is a community-oriented unified tractography
[file format with a minimal specification](https://github.com/tee-ar-ex/trx-spec/blob/master/specifications.md). This is a Pascal implementation TRX reader. This code is used to provide TRX support for the [Surfice cross platform visualization tool for meshes, connectomes, and tractography data](https://www.nitrc.org/plugins/mwiki/index.php/surfice:MainPage).


Assuming you have [FreePascal](https://www.freepascal.org/) installed you can download, compile and test this repository with the following commands:

```
git clone https://github.com/tee-ar-ex/trx-pascal.git
cd trx-python
fpc main.pas
./main ./small.trx
```

The repository includes a simple trx format file named `small.trk`created by Anibal Solon Heinsfeld and shared under the [CC BY 4.0 ](https://brainlife.io/pub/628eb34bd0697cf1eaf2c56d#license). For additional samples visit [brainlife](https://brainlife.io/pub/628eb34bd0697cf1eaf2c56d).

# Limitations

This library was created to provide TRX support for [Surfice](https://www.nitrc.org/plugins/mwiki/index.php/surfice:MainPage) and leverages existing support for the [TRK format](https://trackvis.org/docs/?subsect=fileformat). This imposed several limitations that simplify the design, but could be extended in future.

 - Only supports TRX reading, not writing.
 - All floating-point values are imported as 32-bit floats regardless of input precision (16, 32, or 64 bit precision). Note that most contemporary CPUs have optimal performance for this precision (while GPUs might show better performance for 16-bit floats).
 - All integers are imported as signed 32-bit integers, regardless of input format. Note that this limits the number of unique vertices to 2Gb. This limit matches the limits of most graphics languages (like OpenGL). While huge datasets are unlikely to be useful for visualization, raw processing pipelines may want to handle a larger number of indices.
 - While this class can support an unlimited number of data_per_vertex and data_per_streamline properties, they are always imported as 32-bit floats regardless of input format (integer, float, precision).
 - Groups are not supported (there is no TRK equivalent).

# Pascal?

TRX support is provided in numerous languages, allowing developers to choose the best solution for their tool. Pascal is no longer a popular language. Popular languages benefit from thriving community support, deep library support, numerous job opportunities and open source projects can benefit from the contributions of many developers. For these reasons, new developers may be wise to avoid legacy languages like Pascal, Fortran and COBOL. On the other hand, Pascal has several attributes that make it a pragmatic solution for some problems:

 - Pascal lends itself to one-pass compiling, meaning that [Delphi](https://www.embarcadero.com/products/delphi), [Lazarus](https://www.lazarus-ide.org/) and [FPC](https://www.freepascal.org/) can rapidly prototype large projects (dramatically faster than C).
 - Pascal can use the highly-optimized [LLVM](https://llvm.org/) to get similar numerical performance to highly optimized C code.
 - Pascal string handling is simpler than C.
 - In my opinion, the object-oriented and memory management features of Pascal are seamless relative to Objective-C and C++.
 - Pascal is write-once, compile anywhere. Providing native performance on any operating system (Linux, MacOS, Windows) and most architectures (x86-64, ARM, PowerPC).
 - [Lazarus](https://www.lazarus-ide.org/) allows write-once, compile-anywhere graphical applications that use the native user interface of each operating system: MacOS (Cocoa), Windows (Windows API), and Linux (QT or GTK). In contrast, many cross-platform solutions create applications that require a lot of disk space and do not look native.