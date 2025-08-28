# Data-efficient Visual Place Recognition Using Low-Resolution Image

This repository contains the techniques utilised in the following paper:

**Title:** Sequence-Based Filtering for Visual Route-Based Navigation: Analyzing the Benefits, Trade-Offs and Design Choices <br>
**Authors:** Mihnea-Alexandru Tomita, Bruno Ferrarini, Michael J. Milford, Klaus D. McDonald-Maier and Shoaib Ehsan

Published in 2023 IEEE International Conference on Robotics and Automation (ICRA) Workshop on Active Methods in Autonomous Navigation, London, UK.

Paper available [here](https://robotics.pme.duth.gr/workshop_active2/wp-content/uploads/2023/05/05.-Visual-place-recognition.pdf).

Visual Place Recognition (VPR) enables a robot to recognise previously visited places using visual information from a camera. While state-of-the-art systems often rely on high-resolution images and high-end hardware, many real-world applications must operate with low-resolution, resource-constrained cameras.

In this work, we investigate how image resolution impacts the accuracy, robustness, and efficiency of several well-established handcrafted VPR techniques. Handcrafted methods are computationally lightweight and adaptable to flexible image resolutions, making them suitable for deployment on low-end commercial devices.

Our study shows that:

- **Global feature descriptors** remain robust at lower image resolutions, whereas **local feature descriptors** struggle on very small images.

- **Lowering image resolution reduces computation time**, making VPR more efficient without requiring high-end hardware.

- This trade-off between resolution and performance demonstrates the feasibility of deploying VPR on low-end consumer products.

The handcrafted VPR techniques implemented in this repository are HOG, ORB and GIST. Another VPR technique used in the paper, CoHOG, is not included here as we did not modify its implementation. Instead, please refer to the original [CoHOG](https://github.com/MubarizZaffar/CoHOG_Results_RAL2019) repository.

The code is structured so that it outputs the results required to reproduce the experiments described in our paper.
