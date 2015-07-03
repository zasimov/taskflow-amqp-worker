AMQP Worker for TaskFlow
========================

You can run worker

   taskflow-amqp-worker --config-file=your-worker.conf


You can configure logging

   taskflow-amqp-worker --config-file=your-worker.conf --logging-config=your-logging.yaml


You can create RPM package

   make clean rpm
