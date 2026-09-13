# R25 immutable replay

Repair20 replayed R25 from persisted raw arguments only. It did not call a provider or write beneath E2E-RUN-25.

Current frozen artifact SHA-256 values:

- provider response: 2e6c07a43d6604a010b087311e61772cedc4541f48899b3784eca04e1ec61a04
- final wire record: 8fab899b027ff9f161d6578e4c74c7fb51a0e6689d4a3d7855404cd8951890e6
- truncation record: 4e95baf6afe1135e4413acc0bb7598d609b94a52f7f8d3e0381b56a703dd4fc5
- validation record: 5cf6b32d408fab76d6e80e9b37392da4da0ab1ffb29451f552e85061a120b898

The first failure remains unchanged. E2E-RUN-06 through E2E-RUN-25 were outside all Repair20 write targets.
