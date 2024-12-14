# Image_Frequency_Analysis

## Project Overview

This project demonstrates image processing using Fourier Transform (FFT). Filter high and low frequencies, then reconstruct them back to normal images. Through this process, users can analyze and manipulate frequency components of visual data.

## What is Fourier Transform

The Fourier Transform (FFT) is a mathematical technique that decomposes an image into its different frequency components. In image processing:
* High frequencies represent rapid changes (edges, details, noise)
* Low frequencies represent gradual changes (smooth areas, background)
The process involves:
1. Converting the image to the frequency domain (FFT)
2. Manipulating frequencies using masks
3. Converting back to the image domain (Inverse FFT)

## Advantages

1. High-Frequency Filtering:
* Removes image noise and sharp transitions
* Creates smoother, more refined images

2. Low-Frequency Filtering:
* Enhances edge detection and fine details
* Highlights image boundaries and textures

The FFT image filtering benefits can be customized for different user needs. For example, Noise reduction in images or edge enhancement, enabling precise control over image processing outcomes.

## License

MIT

## Acknowledgements

Thanks to Naratanant Photonics Research Lab for providing technical support and knowledge throughout this project.
