# R01 Recorded Argument Regression

`E2E-RUN-06` remains immutable. Its failure was reproduced as raw compiled-schema replacement omitting `format`; no persisted arguments or response were modified. The new composed schema restores transport-owned `format` before future request construction.
