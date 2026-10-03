# Hello-World

An experimental software and research archive maintained by DNA-Blockchain. This repository contains Python and JavaScript source files, research notes, and bundled examples. It is not a validated release or supported product.

## Verification status

The platform guidance in this repository has not been independently reproduced. Its run instructions do not currently match the tracked platform-checker filename, and the checker source needs repair and testing before it can support a platform claim. Do not rely on the listed operating-system or test status as a guarantee.

Review code and dependencies before running anything. Use a disposable environment and synthetic data only; do not submit genetic, biometric, EEG, health, or other personal data. Nothing here is a medical device, diagnosis, treatment, clinical recommendation, or validated assistive technology.

For the maintained research-software project, setup instructions, and available tests, see [DNA-Blockchain/Helloworld](https://github.com/DNA-Blockchain/Helloworld).

## Public vector index

`public_vector_index.py` reports the public object inventory beneath
`s3://amzn-s3-rabbit-software/vectors/`. It is read-only: local corpus,
research, and identity data are never uploaded by this adapter. Run
`python public_vector_index.py` to check its availability.

Set `RABBIT_VECTOR_BUCKET` or `RABBIT_VECTOR_PREFIX` to use another public
location. Do not publish genetic, biometric, health, or other identifying data
to this bucket.
