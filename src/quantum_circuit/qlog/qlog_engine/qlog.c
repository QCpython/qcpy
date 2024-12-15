#include "qlog.h"

#define MAX_QLOG_LENGTH (1000)
#define EMPTY_QLOG (MAX_QLOG_LENGTH + 1000)
#define MAX_QLOG_QUBITS (256)

struct qlog_def* qlog_init(uint8_t qubits) {
  struct qlog_def* qlog = (struct qlog_def*)malloc(sizeof(struct qlog_def));
  if (qlog == NULL) {
    return NULL;
  }
  qlog->qlog_qubit_cnt = qubits;
  qlog->qlog_size = 0;
  qlog->qlog_entries = (qlog_entry_def**)malloc(MAX_QLOG_LENGTH * sizeof(qlog_entry_def*));
  if (qlog->qlog_entries == NULL) {
    free(qlog);
    return NULL;
  }
  struct qlog_stats_def qlog_stat = {0};
  qlog->qlog_stat = qlog_stat;
  return qlog;
}

void qlog_delete(struct qlog_def* qlog) {
  // free qlog_stat
  // set qlog_stat to null;
  for (uint16_t i = 0; i < qlog->qlog_size; ++i) {
    qlog_entry_delete(qlog->qlog_entries[i]);
  }
  free(qlog->qlog_entries);
  qlog->qlog_entries = NULL;
  free(qlog);
  qlog = NULL;
  return; 
}

uint16_t qlog_size(struct qlog_def *qlog) {
  return !qlog ? (uint16_t)EMPTY_QLOG : qlog->qlog_size;
}

void qlog_clear(struct qlog_def *qlog) {
  if (!qlog) {
    return;
  }
  for (uint16_t i = 0; i < qlog->qlog_size; ++i) {
    qlog_entry_delete(qlog->qlog_entries[i]);
  }
  qlog->qlog_size = EMPTY_QLOG;
  return;
}

qlog_append_res qlog_append(struct qlog_def *qlog, uint8_t *qubits, uint8_t num_qubits, int type, int gate) {
  if (!qlog) {
    return QLOG_APPEND_ERROR;
  }
  if (qlog->qlog_size > MAX_QLOG_LENGTH) {
    return QLOG_APPEND_FULL; 
  }
  if (qlog->qlog_size == EMPTY_QLOG) {
    qlog->qlog_size = 0;
  }
  qlog->qlog_entries[qlog->qlog_size] = qlog_entry_init(qubits, num_qubits, type, gate, qlog->qlog_size);
  if (!qlog->qlog_entries[qlog->qlog_size]) {
    return QLOG_APPEND_ERROR;
  }
  qlog->qlog_size += 1;
  return QLOG_APPEND_SUCCESS;
}

struct qlog_entry_def* qlog_entry_init(uint8_t *qubits, uint8_t num_qubits, int type, int gate, uint8_t qlog_qubits) {
  struct qlog_entry_def* qlog_entry = (struct qlog_entry_def*)malloc(sizeof(struct qlog_entry_def));
  if (!qlog_entry) {
    return NULL;
  }
  qlog_entry->qlog_entry_qubits = (uint8_t*)malloc(num_qubits * sizeof(uint8_t));
  if (!qlog_entry->qlog_entry_qubits) {
    return NULL;
  }
  memcpy(qubits, qlog_entry->qlog_entry_qubits, num_qubits);
  for (uint8_t i = 0; i < num_qubits; ++i) {
    qlog_entry->qlog_entry_qubits[i] = qubits[i];
  }
  qlog_entry->qlog_entry_qubit_cnt = num_qubits;
  qlog_entry->qlog_entry_gate = gate;
  qlog_entry->qlog_entry_gate_type = type;
  // set type via function to enum, handle if it does not exist
  // set gate name via function to enum, handle if it does not exist
  // set qlog_entry stat
  return qlog_entry;
}

void qlog_entry_delete(struct qlog_entry_def *qlog_entry) {
  free(qlog_entry->qlog_entry_qubits); 
  qlog_entry->qlog_entry_qubits = NULL;
  free(qlog_entry);
  qlog_entry = NULL;
  // set stats to null
  return;
}

qlog_entry_gate qlog_entry_qg_name(struct qlog_entry_def *qlog_entry) {
  return qlog_entry->qlog_entry_gate;
}

qlog_entry_type qlog_entry_qg_type(struct qlog_entry_def *qlog_entry) {
  return qlog_entry->qlog_entry_gate_type;
}
