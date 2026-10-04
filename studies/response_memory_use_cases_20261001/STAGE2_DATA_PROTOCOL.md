# Stage2 fixed data preparation

Written before download, dataset inspection or stage2 training. This is a fixed
cross-domain mechanism test, not a benchmark or representative production-scale
workload. Both routes receive identical arrays; the coordination route takes the
first512 training rows by its separately frozen protocol.

Domains selected independently of any stage2 outcomes:

1. Fashion-MNIST official train/test data, classes0(T-shirt/top) and6(shirt).
   Labels are -1 and+1 respectively. Download the four gzip IDX files from
   the official zalandoresearch/fashion-mnist repository. Match official MD5s
   and record SHA256s. Retain raw bytes.
2. CaliforniaHousing from the exact archive used by installed sklearn1.5.1,
   https://ndownloader.figshare.com/files/5976036 . Require SHA256
   aaa5c9a6afe2225cc2aed2723682ae403280c4a3695a2ddda4ffb5d8215ea681.
   Parse only CaliforniaHousing/cal_housing.data, using sklearn's documented
   average-room/bedroom/occupancy transformation and target in100000-dollar units.
   A seeded random split is used; this is not geographic extrapolation.
   Learning target is tanh((house_value-training_mean)/training_std), a bounded
   regression problem explicitly different from raw-dollar RMSE prediction.
3. UCI Human Activity Recognition Using Smartphones, official dataset240 archive:
   https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip
   Use supplied561-dimensional features. Labels activities1,2,3 are+1(moving),
   4,5,6 are-1(stationary). Retain original six activity IDs and subject IDs.
   Official test subjects remain separate. Validation uses the largest four
   sorted training-subject IDs, before selecting individual rows; no training
   subject appears in validation. This tests the supplied engineered features,
   not end-to-end learning from raw accelerometer signals.

Seed20261002 initializes a separate NumPy generator for each dataset. Select
1024training,256validation,1024test rows without replacement; Fashion draws
training and validation from its official training pool, test from its official
test pool; California uses one permutation of all rows; HAR uses the declared
subject partitions. No class balancing, label-based selection or rerolling.

Use only the selected training rows to estimate each input-coordinate mean and
standard deviation. Divide by max(std,1e-3), clip each standardized coordinate
to[-5,5], append a constant1coordinate, and normalize each row to unit Euclidean
norm. This explicit input embedding preserves the paper's no-explicit-bias
architecture but supplies a constant input direction. Pass these rows directly
to the source API: raw mathematical x=sqrt(d)*row, so ||x||=sqrt(d).
Store all arrays in float64; a route may explicitly cast to its declared dtype.

NPZ schema: X_train,y_train,X_val,y_val,X_test,y_test; index_* indicates the
source row; group_* is original class/activity or0for housing; subject_* for
HAR. Input means/scales, target transforms, source pool labels, counts, exact
source hashes, preparation source hash and NPZ hashes are recorded in JSON.
All downloads and products live in this study's generated namespace. No files
are extracted to arbitrary archive paths. Stop if checksum or partition checks
fail. A network failure may be retried without changing the scientific protocol.
