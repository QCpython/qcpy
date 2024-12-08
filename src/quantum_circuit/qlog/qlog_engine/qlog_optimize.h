#include "qlog.h"
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define QLOG_OPTIMIZE_TYPES \
  X(qlog_optimize_remove_identity_gates)                       

typedef enum {
  REMOVE_IDENTITY_GATES
} qlog_opt_track_types;

typedef struct qlog_optimize_def {
  int fun_cc_counter;
} qlog_optimize_def;

qlog_optimize_def* qlog_optimize_init();
void qlog_optimize_delete();

void qlog_optimize_remove_identity_gates(struct qlog_def* qlog, struct qlog_def* optimized_qlog, qlog_optimize_def* qlog_optimize);

struct qlog_def* qlog_optimize_set(struct qlog_def* qlog);


