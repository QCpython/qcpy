#include "qlog_optimize.h"
#include <stdio.h>

#define X(f) f,
void (*qlog_optimize_types_arr[])(struct qlog_def*, struct qlog_def*, qlog_optimize_def*) = {QLOG_OPTIMIZE_TYPES};
#undef X

int qlog_optimize_types_arr_cnt = sizeof(qlog_optimize_types_arr) / sizeof(qlog_optimize_types_arr[0]);

struct qlog_optimize_def* qlog_optimize_init() {
  struct qlog_optimize_def* qlog_optimize;
  qlog_optimize->fun_cc_counter = 0;
  return qlog_optimize;
}

struct qlog_def* qlog_optimize_set(struct qlog_def *qlog) {
  struct qlog_def* optimized_qlog = qlog_init(qlog->qlog_qubit_cnt); 
  struct qlog_optimize_def* qlog_optimize = qlog_optimize_init();
  for (int i = 0; i < qlog_optimize_types_arr_cnt; ++i) {
    qlog_optimize_types_arr[i](qlog, optimized_qlog, qlog_optimize);
    qlog = optimized_qlog;
  } 
  qlog_delete(qlog);
  return optimized_qlog;
}

void qlog_optimize_remove_identity_gates(struct qlog_def* qlog, struct qlog_def* optimized_qlog, struct qlog_optimize_def* qlog_optimize) {
  qlog_optimize->fun_cc_counter += 1;
  for (uint16_t i = 0; qlog->qlog_size; ++i) {
    qlog_entry_def* qlog_entry = qlog->qlog_entries[i];
    if (qlog_entry->qlog_entry_gate != QLOG_ENTRY_GATE_IDENTITY) {
      qlog_append_res append_res = qlog_append(optimized_qlog, 
                                               qlog_entry->qlog_entry_qubits,  
                                               qlog_entry->qlog_entry_qubit_cnt, 
                                               qlog_entry->qlog_entry_gate_type, 
                                               qlog_entry->qlog_entry_gate);
      if (append_res != QLOG_APPEND_SUCCESS) {
        return;
      }
    }
    qlog_entry_delete(qlog_entry);
  }
}
