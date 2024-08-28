const kue = require('kue');

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, world!'
};

// Create a queue named push_notification_code
const pushNotificationQueue = queue.create('push_notification_code', jobData);

// When the job is created without error
pushNotificationQueue.on('enqueue', function (job, jobData) {
  console.log('Notification job created:', pushNotificationQueue.id);
});

// When the job is completed
pushNotificationQueue.on('complete', function (job) {
  console.log('Notification job completed');
});

// When the job is failing
pushNotificationQueue.on('failed', function (job, err) {
  console.log('Notification job failed');
});

// Save the job to the queue
pushNotificationQueue.save();
